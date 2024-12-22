const vscode = require("vscode");
const apiClient = require("../utils/apiClient");
const fs = require("fs");
const path = require("path");

async function downloadReport() {
  const format = await vscode.window.showQuickPick(["txt", "pdf"], {
    placeHolder: "Select the report format"
  });

  if (!format) {
    vscode.window.showInformationMessage("Operation cancelled.");
    return;
  }

  try {
    const response = await apiClient.get(`/download-report?format=${format}`, {
      responseType: "stream"
    });

    const filePath = path.join(vscode.workspace.rootPath || __dirname, `audit_report.${format}`);
    const writer = fs.createWriteStream(filePath);

    response.data.pipe(writer);

    writer.on("finish", () => {
      vscode.window.showInformationMessage(`Report downloaded: ${filePath}`);
    });
    writer.on("error", () => {
      vscode.window.showErrorMessage("Error saving the report.");
    });
  } catch (error) {
    vscode.window.showErrorMessage(`Error downloading the report: ${error.message}`);
  }
}

module.exports = downloadReport;
