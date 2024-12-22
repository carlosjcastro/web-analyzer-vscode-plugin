# WCAG Auditor

**English** | [Español](#auditor-wcag)

---

## Description

WCAG Auditor is a Visual Studio Code plugin designed to audit web accessibility based on the Web Content Accessibility Guidelines (WCAG). It utilizes a FastAPI microservice to analyze HTML content and identify accessibility issues.

---

## Features

- **Audit HTML Accessibility:** Analyze HTML files and detect accessibility issues based on WCAG standards.
- **Display Results in the Terminal:** View detected issues directly in the VS Code terminal.
- **Interactive Commands:** Trigger accessibility audits using VS Code commands.
- **FastAPI Microservice Integration:** Communicates with a locally running FastAPI server for audits.

---

## Requirements

- Visual Studio Code (v1.80.0 or higher).
- Node.js and npm installed.
- A locally running FastAPI microservice at `http://127.0.0.1:8000/audit`.

---

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd wcag_vscode_plugin
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. Package the extension using `vsce`:
   ```bash
   vsce package
   ```
5. Install the generated `.vsix` file in Visual Studio Code.

---

## Usage

1. Open an HTML file in Visual Studio Code.
2. Press `Ctrl+Shift+P` and run the command:
   - `WCAG: Audit HTML Accessibility` to analyze the file.
3. View the results in the terminal or as a notification.

---

## Commands

| Command                        | Description                                           |
|--------------------------------|-------------------------------------------------------|
| `WCAG: Audit HTML Accessibility` | Audits the open HTML file for accessibility issues.   |
| `WCAG: Download WCAG Report`   | Downloads a detailed WCAG report.                    |

---

## Development

### File Structure

```plaintext
wcag_vscode_plugin/
├── .vscode/        # Configuration for debugging
├── src/            # Source files for the extension
│   ├── extension.js  # Main file for the extension logic
├── package.json    # Extension metadata and dependencies
└── README.md       # Documentation
```

### Debugging

1. Open the project folder in Visual Studio Code.
2. Press `F5` to launch the extension in a new VS Code window.
3. Check the terminal for accessibility audit results.

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

# Auditor WCAG

**Español** | [English](#wcag-auditor)

---

## Descripción

Auditor WCAG es un plugin para Visual Studio Code diseñado para auditar la accesibilidad web basado en las Pautas de Accesibilidad al Contenido en la Web (WCAG). Utiliza un microservicio FastAPI para analizar contenido HTML e identificar problemas de accesibilidad.

---

## Características

- **Auditar accesibilidad en HTML:** Analiza archivos HTML y detecta problemas de accesibilidad según los estándares WCAG.
- **Mostrar resultados en la terminal:** Visualiza los problemas detectados directamente en la terminal de VS Code.
- **Comandos interactivos:** Inicia auditorías de accesibilidad utilizando comandos de VS Code.
- **Integración con microservicio FastAPI:** Se comunica con un servidor FastAPI local para realizar las auditorías.

---

## Requisitos

- Visual Studio Code (v1.80.0 o superior).
- Node.js y npm instalados.
- Un microservicio FastAPI corriendo localmente en `http://127.0.0.1:8000/audit`.

---

## Instalación

1. Clona este repositorio:
   ```bash
   git clone <repository-url>
   ```
2. Ve al directorio del proyecto:
   ```bash
   cd wcag_vscode_plugin
   ```
3. Instala las dependencias:
   ```bash
   npm install
   ```
4. Empaqueta la extensión utilizando `vsce`:
   ```bash
   vsce package
   ```
5. Instala el archivo `.vsix` generado en Visual Studio Code.

---

## Uso

1. Abre un archivo HTML en Visual Studio Code.
2. Presiona `Ctrl+Shift+P` y ejecuta el comando:
   - `WCAG: Audit HTML Accessibility` para analizar el archivo.
3. Revisa los resultados en la terminal o en una notificación.

---

## Comandos

| Comando                          | Descripción                                          |
|----------------------------------|------------------------------------------------------|
| `WCAG: Audit HTML Accessibility` | Audita el archivo HTML abierto para problemas de accesibilidad. |
| `WCAG: Download WCAG Report`     | Descarga un reporte detallado de WCAG.              |

---

## Desarrollo

### Estructura de Archivos

```plaintext
wcag_vscode_plugin/
├── .vscode/        # Configuración para depuración
├── src/            # Archivos fuente de la extensión
│   ├── extension.js  # Archivo principal con la lógica de la extensión
├── package.json    # Metadatos y dependencias de la extensión
└── README.md       # Documentación
```

### Depuración

1. Abre la carpeta del proyecto en Visual Studio Code.
2. Presiona `F5` para lanzar la extensión en una nueva ventana de VS Code.
3. Revisa los resultados de la auditoría en la terminal.

---

## License and Copyright

Copyright (c) 2024 Carlos José Castro Galante. All rights reserved.

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Licencia y Copyright

Copyright (c) 2024 Carlos José Castro Galante. Todos los derechos reservados.

Este proyecto está bajo la licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
