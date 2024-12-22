from pydantic import BaseModel
from typing import List, Optional

class AccessibilityIssue(BaseModel):
    guideline: str
    description: str
    severity: str
    element: Optional[str]

class AuditReport(BaseModel):
    url: Optional[str]
    issues: List[AccessibilityIssue]
    summary: str
    compliance_score: float
