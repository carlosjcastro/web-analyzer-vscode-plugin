const vscode = require("vscode");
const apiClient = require("../utils/apiClient");

async function auditHtml() {
  const editor = vscode.window.activeTextEditor;

  if (!editor) {
    vscode.window.showErrorMessage("There is no file open.");
    return;
  }

  const htmlContent = editor.document.getText();
  const level = await vscode.window.showQuickPick(["A", "AA", "AAA"], {
    placeHolder: "Select the WCAG audit level"
  });

  if (!level) {
    vscode.window.showInformationMessage("Operation cancelled.");
    return;
  }

  try {
    const response = await apiClient.post("/audit", { html_content: htmlContent, level });
    const issues = response.data.report.issues;

    if (issues.length === 0) {
      vscode.window.showInformationMessage("No accessibility issues found!");
    } else {
      const issueList = issues.map(issue => `- ${issue.issue} (${issue.severity})`).join("\n");
      vscode.window.showInformationMessage(`Accessibility issues found:\n\n${issueList}`);
    }
  } catch (error) {
    vscode.window.showErrorMessage(`Error performing the audit: ${error.message}`);
  }
}

module.exports = auditHtml;
