from bs4 import BeautifulSoup
from models import AccessibilityIssue, AuditReport
from utils import parse_html

def check_alt_tags(soup: BeautifulSoup):
    """Check if all images have alt attributes."""
    issues = []
    images = soup.find_all("img")
    for img in images:
        if not img.get("alt"):
            issues.append(AccessibilityIssue(
                guideline="1.1.1 Non-text Content",
                description="Image element missing 'alt' attribute",
                severity="high",
                element=str(img)
            ))
    return issues

def check_form_labels(soup: BeautifulSoup):
    """Check if all form inputs have associated labels."""
    issues = []
    inputs = soup.find_all("input")
    for input_tag in inputs:
        if not input_tag.get("id"):
            continue
        label = soup.find("label", {"for": input_tag.get("id")})
        if not label:
            issues.append(AccessibilityIssue(
                guideline="1.3.1 Info and Relationships",
                description="Input element missing an associated label",
                severity="medium",
                element=str(input_tag)
            ))
    return issues

def check_contrast(html_content: str):
    """Placeholder function for contrast checks."""
    return []

def audit_html(html_content: str, url: str = None):
    """Main audit function."""
    soup = parse_html(html_content)
    issues = []

    issues.extend(check_alt_tags(soup))
    issues.extend(check_form_labels(soup))

    compliance_score = max(0, 100 - len(issues) * 10)

    # Create summary
    summary = f"Found {len(issues)} accessibility issues. High severity: {sum(1 for i in issues if i.severity == 'high')}."

    return AuditReport(
        url=url,
        issues=issues,
        summary=summary,
        compliance_score=compliance_score
    )
