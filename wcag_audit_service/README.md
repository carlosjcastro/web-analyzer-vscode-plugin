**Web Accessibility Audit API Documentation**

---

### English Version

#### **Overview**
This project implements a RESTful API using FastAPI to audit web pages for compliance with Web Content Accessibility Guidelines (WCAG). It provides automated validation of HTML content against accessibility standards, identifies potential issues, and generates actionable reports. Designed for use in accessibility audits, hackathons, or for enhancing user experience, this API addresses inclusivity for users with disabilities.

---

#### **Key Features**
- **WCAG Levels Supported**: Validates against Levels A, AA, and AAA.
- **Comprehensive Audits**:
  - Checks for image alt attributes, link text, and logical heading structure.
  - Ensures proper color contrast and form labels.
  - Verifies ARIA roles, keyboard navigation, and scalable text.
- **Detailed Reporting**:
  - Descriptions, severity levels, and resolution suggestions for issues.
  - JSON-formatted reports for easy integration.
- **Input Flexibility**: Accepts either URLs or raw HTML content.

---

#### **Endpoints**

1. **`POST /audit`**  
   - **Request Payload**:
     ```json
     {
       "url": "https://example.com",
       "level": "AA"
     }
     ```
   - **Response Example**:
     ```json
     {
       "success": true,
       "report": {
         "url": "https://example.com",
         "issues": [
           {
             "issue": "Missing alt attribute in <img> tag.",
             "element": "<img src=\"image.jpg\" />",
             "severity": "High",
             "description": "Images must have an 'alt' attribute to provide alternative text for screen readers."
           }
         ],
         "summary": "Found 1 accessibility issue. High severity: 1.",
         "compliance_score": 99
       }
     }
     ```

2. **`GET /docs`**  
   - Access interactive API documentation powered by FastAPI's auto-generated OpenAPI specification.

---

#### **Core Functionalities**

##### **1. WCAG Compliance Validation**
The API validates HTML against WCAG standards, including:
- **Alt Attributes**: Ensures all `<img>` tags have `alt` attributes for screen readers.
- **Link Accessibility**: Checks if `<a>` tags have descriptive text or ARIA attributes.
- **Header Structure**: Verifies logical hierarchy (e.g., `<h1>` > `<h2>`).
- **Color Contrast**: Confirms text and background colors meet WCAG contrast ratios.
- **Form Labels**: Validates labels for input fields via `for` or ARIA attributes.
- **Keyboard Navigation**: Ensures interactive elements are navigable using `tabindex`.

##### **2. Customizable Audits**
Users can specify WCAG levels (`A`, `AA`, or `AAA`) to align with compliance goals.

##### **3. Scoring and Suggestions**
- **Compliance Score**: Rates accessibility on a scale of 0–100.
- **Actionable Insights**: Provides solutions to address each issue.

---

#### **Installation and Usage**

1. **Install Dependencies**:
   ```bash
   pip install fastapi uvicorn beautifulsoup4 pdfkit requests colour

2. Start the API Server: 
 ´´´ uvicorn main:app --reload ´´´

3. Testing the API:
- Use tools like Postman or cURL.
- Send a POST request to /audit.

4. Generate Reports:
- Reports are returned in JSON format.
- Download TXT report
- Optional PDF report generation using the pdfkit library.

### Additional Tools
- **FastAPI**: Framework for building RESTful APIs.
- **BeautifulSoup**: Parses HTML for compliance checks.
- **pdfkit**: Converts reports into PDFs.
- **requests**: Fetches web content via URLs.
- **colour**: Calculates color contrast ratios.

---

### Roadmap
- **Integration with third-party tools**: Streamline automated testing pipelines.
- **Expanded ARIA attribute coverage**: Improve validation for accessibility roles and properties.
- **User interaction simulations**: Test accessibility features like keyboard navigation and focus management.

---

### Versión en Español  

#### **Descripción General**  
Este proyecto implementa una API RESTful utilizando FastAPI para auditar páginas web y verificar su cumplimiento con las Pautas de Accesibilidad para el Contenido Web (WCAG). Proporciona validación automática del contenido HTML frente a estándares de accesibilidad, identifica posibles problemas y genera informes con sugerencias accionables. Diseñada para auditorías de accesibilidad, hackatones o para mejorar la experiencia del usuario, esta API fomenta la inclusión para usuarios con discapacidades.  

---  

#### **Características Principales**  
- **Niveles de WCAG Soportados**: Validación contra los niveles A, AA y AAA.  
- **Auditorías Exhaustivas**:  
  - Verifica atributos `alt` en imágenes, texto descriptivo en enlaces y estructura lógica de encabezados.  
  - Asegura contraste adecuado de colores y etiquetas en formularios.  
  - Valida roles ARIA, navegación por teclado y texto escalable.  
- **Informes Detallados**:  
  - Incluye descripciones, niveles de severidad y sugerencias para resolver problemas.  
  - Informes en formato JSON para fácil integración.  
- **Flexibilidad de Entrada**: Acepta URLs o contenido HTML crudo.  

---  

#### **Endpoints**  

1. **`POST /audit`**  
   - **Cuerpo de la Solicitud**:  
     ```json
     {
       "url": "https://example.com",
       "level": "AA"
     }
     ```  
   - **Ejemplo de Respuesta**:  
     ```json
     {
       "success": true,
       "report": {
         "url": "https://example.com",
         "issues": [
           {
             "issue": "Falta el atributo alt en la etiqueta <img>.",
             "element": "<img src=\"image.jpg\" />",
             "severity": "Alta",
             "description": "Las imágenes deben tener un atributo 'alt' para proporcionar texto alternativo a los lectores de pantalla."
           }
         ],
         "summary": "Se encontró 1 problema de accesibilidad. Severidad alta: 1.",
         "compliance_score": 99
       }
     }
     ```  

2. **`GET /docs`**  
   - Accede a la documentación interactiva de la API generada automáticamente con OpenAPI de FastAPI.  

---  

#### **Funciones Principales**  

##### **1. Validación de Cumplimiento WCAG**  
La API valida HTML según los estándares WCAG, incluyendo:  
- **Atributos Alt**: Verifica que todas las etiquetas `<img>` tengan atributos `alt` para lectores de pantalla.  
- **Accesibilidad de Enlaces**: Comprueba que las etiquetas `<a>` tengan texto descriptivo o atributos ARIA.  
- **Estructura de Encabezados**: Garantiza una jerarquía lógica (e.g., `<h1>` > `<h2>`).  
- **Contraste de Colores**: Confirma que los colores de texto y fondo cumplan con las proporciones de contraste de WCAG.  
- **Etiquetas en Formularios**: Valida etiquetas para campos de entrada mediante `for` o atributos ARIA.  
- **Navegación por Teclado**: Garantiza que los elementos interactivos sean navegables mediante `tabindex`.  

##### **2. Auditorías Personalizables**  
Los usuarios pueden especificar niveles de WCAG (`A`, `AA` o `AAA`) para alinearse con sus metas de cumplimiento.  

##### **3. Puntuación y Sugerencias**  
- **Puntuación de Cumplimiento**: Evalúa la accesibilidad en una escala de 0–100.  
- **Sugerencias Accionables**: Proporciona soluciones para cada problema identificado.  

---  

#### **Instalación y Uso**  

1. **Instalar Dependencias**:  
   ```bash
   pip install fastapi uvicorn beautifulsoup4 pdfkit requests colour

2. Iniciar el servidor API: 
 ´´´ uvicorn main:app --reload ´´´

3. Probar la API:
- Usa herramientas como Postman o cURL.
- Envía una solicitud POST a /audit.

4. Generar reportes:
- Los reportes se devuelven en formato JSON.
- Descargar reporte en formato TXT.
- Generación opcional de reporte en PDF utilizando la librería pdfkit.

### Additional Tools
- **FastAPI**: Framework para construir APIs RESTful.
- **BeautifulSoup**: Analiza HTML para la verificación de cumplimiento.
- **pdfkit**: Convierte los reportes en PDFs.
- **requests**: Recupera contenido web a través de URLs.
- **colour**: Calcula las proporciones de contraste de colores.

---

## License and Copyright

Copyright (c) 2024 Carlos José Castro Galante. All rights reserved.

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Licencia y Copyright

Copyright (c) 2024 Carlos José Castro Galante. Todos los derechos reservados.

Este proyecto está bajo la licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.