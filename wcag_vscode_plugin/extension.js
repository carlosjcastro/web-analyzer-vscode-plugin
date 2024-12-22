const vscode = require("vscode");
const auditHtml = require("./commands/auditHtml");
const downloadReport = require("./commands/downloadReport");

function activate(context) {
  try {
      context.subscriptions.push(
          vscode.commands.registerCommand("wcag.auditHtml", auditHtml),
          vscode.commands.registerCommand("wcag.downloadReport", downloadReport)
      );
      console.log("Commands registered successfully.");
  } catch (error) {
      console.error("Error registering commands:", error);
  }
}

function deactivate() {}

module.exports = {
  activate,
  deactivate,
};
