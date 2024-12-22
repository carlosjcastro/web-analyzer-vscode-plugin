from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from typing import Optional
from fastapi.responses import FileResponse
import requests
from bs4 import BeautifulSoup
import pdfkit
import os
from colour import Color 

app = FastAPI()

class AuditRequest(BaseModel):
    url: Optional[HttpUrl] = None
    html_content: Optional[str] = None
    level: str = "AA"

latest_report = None

# Function to check color contrast (level AA) | Función para verificar el contraste de colores (nivel AA)
def check_contrast(color1, color2, level):
    color1_rgb = Color(color1).rgb
    color2_rgb = Color(color2).rgb

    luminance1 = 0.2126 * color1_rgb[0] + 0.7152 * color1_rgb[1] + 0.0722 * color1_rgb[2]
    luminance2 = 0.2126 * color2_rgb[0] + 0.7152 * color2_rgb[1] + 0.0722 * color2_rgb[2]
    
    contrast_ratio = (luminance1 + 0.05) / (luminance2 + 0.05) if luminance1 > luminance2 else (luminance2 + 0.05) / (luminance1 + 0.05)

    if level == "AAA":
        return contrast_ratio >= 7.0
    else:
        return contrast_ratio >= 4.5

# WCAG Validations | Validaciones WCAG
def audit_html(html_content: str, url: Optional[str] = None, level: str = "AA"):
    soup = BeautifulSoup(html_content, "html.parser")
    issues = []

    # Rule 1: alt attribute in images (Level A) | Regla 1: Atributo alt en imágenes (Nivel A)
    if level in ["A", "AA", "AAA"]:
        images = soup.find_all("img")
        for img in images:
            if not img.get("alt"):
                issues.append({
                    "issue": "Missing alt attribute in <img> tag.",
                    "element": str(img),
                    "severity": "High",
                    "description": "Images must have an 'alt' attribute to provide alternative text for screen readers. This helps visually impaired users understand the content of the image."
                })

    # Rule 2: <a> links must have text or aria-label attribute (Level A) | Regla 2: Enlaces <a> deben tener texto o atributo aria-label (Nivel A)
    if level in ["A", "AA", "AAA"]:
        links = soup.find_all("a")
        for link in links:
            if not link.text.strip() and not link.get("aria-label"):
                issues.append({
                    "issue": "Empty <a> tag without aria-label.",
                    "element": str(link),
                    "severity": "Medium",
                    "description": "Links must have descriptive text or an 'aria-label' attribute to provide context for screen readers. This ensures that users understand the purpose of the link."
                })

    # Rule 3: Headings in logical order (Level A) | Regla 3: Encabezados en orden lógico (Nivel A)
    if level in ["A", "AA", "AAA"]:
        headers = [tag.name for tag in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])]
        for i in range(1, len(headers)):
            if headers[i] < headers[i - 1]:
                issues.append({
                    "issue": "Header tags are not in logical order.",
                    "element": headers,
                    "severity": "Medium",
                    "description": "Headers must follow a logical order (e.g., h1 > h2 > h3) to provide a clear structure for screen readers and improve navigation for all users."
                })

    # Rule 4: Color contrast (level AA) | Regla 4: Contraste de colores (nivel AA)
    if level in ["AA", "AAA"]:
        texts = soup.find_all(text=True)
        for text in texts:
            color = text.parent.get('style', '').lower()
            if 'color' in color and 'background-color' in color:
                color1 = color.split('color:')[1].split(';')[0].strip()
                color2 = color.split('background-color:')[1].split(';')[0].strip()
                if not check_contrast(color1, color2, level):
                    issues.append({
                        "issue": "Low contrast between text and background color.",
                        "element": str(text),
                        "severity": "High",
                        "description": "Text and background colors must have sufficient contrast to be readable by users with visual impairments. This is crucial for users with low vision or color blindness."
                    })

    # Rule 5: Form validation (Level A) | Regla 5: Verificación de formulario (Nivel A)
    if level in ["A", "AA", "AAA"]:
        forms = soup.find_all("form")
        for form in forms:
            inputs = form.find_all(["input", "textarea", "select"])
            for element in inputs:
                if not element.get("id"):
                    issues.append({
                        "issue": f"Form input element <{element.name}> lacks id.",
                        "element": str(element),
                        "severity": "Medium",
                        "description": "Form input elements must have an 'id' attribute to associate them with labels. This helps screen readers identify the purpose of the input."
                    })
                if not element.get("aria-label") and not element.get("label"):
                    issues.append({
                        "issue": f"Form input element <{element.name}> lacks aria-label or label.",
                        "element": str(element),
                        "severity": "Medium",
                        "description": "Form input elements must have an 'aria-label' or 'label' to provide context for screen readers. This ensures that users understand the purpose of the input."
                    })

    # Rule 6: Text size and scalability (Level AA) | Regla 6: Tamaño de texto y escalabilidad (Nivel AA)
    if level in ["AA", "AAA"]:
        body = soup.find("body")
        if body:
            styles = body.get("style", "")
            if "font-size" not in styles or "px" in styles:
                issues.append({
                    "issue": "Text size may not be scalable (use relative units like em or rem).",
                    "element": str(body),
                    "severity": "Low",
                    "description": "Text size should be defined using relative units (e.g., em, rem) to allow users to scale text according to their preferences. This improves readability for users with visual impairments."
                })

    # Rule 7: Keyboard navigation (ARIA roles and tabindex) (Level A, AA) | Regla 7: Navegación por teclado (ARIA roles y tabindex) (Nivel A, AA)
    if level in ["A", "AA", "AAA"]:
        interactive_elements = soup.find_all(["a", "button", "input", "textarea", "select", "form", "area", "iframe"])
        for element in interactive_elements:
            if not element.get("tabindex"):
                issues.append({
                    "issue": f"Interactive element <{element.name}> lacks tabindex.",
                    "element": str(element),
                    "severity": "Medium",
                    "description": "Interactive elements must have a 'tabindex' attribute to ensure they are accessible via keyboard navigation. This is essential for users who cannot use a mouse."
                })
            if element.get("role") and element["role"] not in ["link", "button", "checkbox", "textbox"]:
                issues.append({
                    "issue": f"Element <{element.name}> uses inappropriate ARIA role {element['role']}.",
                    "element": str(element),
                    "severity": "Low",
                    "description": "Elements must use appropriate ARIA roles to provide context for screen readers. This ensures that users understand the purpose and behavior of the element."
                })

    # Rule 8: Links must be accessible without color (Level AA) | Regla 8: Enlaces deben ser accesibles sin color (Nivel AA)
    if level in ["AA", "AAA"]:
        for link in links:
            if "color" in link.get('style', ''):
                issues.append({
                    "issue": "Links should be accessible without relying on color.",
                    "element": str(link),
                    "severity": "Medium",
                    "description": "Links must be distinguishable without relying solely on color. This ensures that users with color blindness or low vision can identify links."
                })

    # Rule 9: Form elements must have clear labels (Level A) | Regla 9: Elementos de formulario deben tener etiquetas claras (Nivel A)
    if level in ["A", "AA", "AAA"]:
        for form in forms:
            if not form.find("label"):
                issues.append({
                    "issue": "Form elements must have clear labels.",
                    "element": str(form),
                    "severity": "High",
                    "description": "Form elements must have clear labels to provide context for screen readers. This ensures that users understand the purpose of each form element."
                })

    # Rule 10: Text contrast in images (Level AAA)
    if level == "AAA":
        for img in images:
            if img.get("style") and "background-color" in img.get("style"):
                issues.append({
                    "issue": "Image background should have sufficient contrast with text.",
                    "element": str(img),
                    "severity": "High",
                    "description": "Text over images must have sufficient contrast with the background to be readable by users with visual impairments. This is crucial for users with low vision or color blindness."
                })

    # Return an overview of the issues found | Devuelve una descripción general de los problemas encontrados
    summary = f"Found {len(issues)} accessibility issues. High severity: {sum(1 for i in issues if i['severity'] == 'High')}."
    compliance_score = max(0, 100 - len(issues))

    return {
        "url": url,
        "issues": issues,
        "summary": summary,
        "compliance_score": compliance_score
    }

def fetch_html(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Error fetching URL: {str(e)}")

# Allows to perform a web accessibility audit | Permite realizar una auditoría de accesibilidad web
@app.post("/audit")
async def audit(request: AuditRequest):
    global latest_report
    if not request.url and not request.html_content:
        raise HTTPException(status_code=400, detail="Either 'url' or 'html_content' must be provided.")

    try:
        if request.url:
            html_content = fetch_html(request.url)
        else:
            html_content = request.html_content

        latest_report = audit_html(html_content, request.url, request.level)
        return {"success": True, "report": latest_report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

# Allows to save the audit report | Permite guardar el informe de auditoría
def save_report(report: dict, format: str = "txt") -> str:
    filename = f"audit_report.{format}"

    if format == "txt":
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Accessibility Audit Report\n\n")
            file.write(f"URL: {report['url']}\n")
            file.write(f"Summary: {report['summary']}\n\n")
            if report['issues']:
                file.write("Issues:\n")
                for issue in report['issues']:
                    file.write(f"- {issue['issue']} (Severity: {issue['severity']})\n")
                    file.write(f"  Description: {issue['description']}\n")
            else:
                file.write("No issues found.\n")

    elif format == "pdf":
        html = f"""
        <h1>Accessibility Audit Report</h1>
        <p><strong>URL:</strong> {report['url']}</p>
        <p><strong>Summary:</strong> {report['summary']}</p>
        <h2>Issues</h2>
        <ul>
        {''.join([f'<li>{issue["issue"]} (Severity: {issue["severity"]})<br>Description: {issue["description"]}</li>' for issue in report['issues']])}
        </ul>
        """
        pdfkit.from_string(html, filename)

    return filename

# Allows to download the audit report | Permite descargar el informe de auditoría
@app.get("/download-report")
async def download_report(format: str = "txt"):
    global latest_report
    if not latest_report:
        raise HTTPException(status_code=404, detail="No report available. Perform an audit first.")

    if format not in ["txt", "pdf"]:
        raise HTTPException(status_code=400, detail="Invalid format. Choose 'txt' or 'pdf'.")

    report_path = save_report(latest_report, format)

    if os.path.exists(report_path):
        return FileResponse(report_path, media_type="application/octet-stream", filename=f"audit_report.{format}")
    else:
        raise HTTPException(status_code=404, detail="Report not found.")