# WCAG Auditor Extension Documentation

## English Version

### Overview
The **WCAG Auditor** is a Visual Studio Code extension developed by **Carlos José Castro Galante** that helps developers audit HTML content for accessibility compliance with the WCAG (Web Content Accessibility Guidelines) standards. This extension interacts with a FastAPI microservice to provide real-time feedback and generate reports. 

---

### Features
- **HTML Accessibility Auditing**: Evaluate HTML content against WCAG Levels A, AA, and AAA.
- **Customizable Report Generation**: Export reports in TXT or PDF formats.
- **FastAPI Integration**: Leverages a microservice backend for real-time analysis and reporting.
- **Developer-Friendly**: Simple commands accessible directly from the VS Code Command Palette.

---

### Installation
1. Clone the repository:
   ```bash
   git clone ()
   ```
2. Open the folder in Visual Studio Code.
3. Install the required dependencies:
   ```bash
   npm install
   ```
4. Launch the extension in development mode:
   - Press `F5` in VS Code.
   - Select the `Run Extension` environment.

---

### Usage

#### HTML Auditing
1. Open an HTML file in Visual Studio Code.
2. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS).
3. Select the `WCAG: Audit HTML` command.
4. Choose the desired WCAG compliance level (A, AA, AAA).
5. View the results:
   - If no issues are found, a success message is displayed.
   - If issues are detected, a list of problems with severity levels is shown.

#### Downloading Reports
1. Open the Command Palette and select `WCAG: Download Report`.
2. Choose the report format (TXT or PDF).
3. The report is saved in the current workspace directory.

---

### Tools and Technologies
- **Visual Studio Code API**: For creating and managing extension commands.
- **FastAPI**: Backend microservice for analyzing HTML content.
- **Axios**: HTTP client for seamless API interactions.
- **Node.js**: JavaScript runtime environment.
- **JavaScript**: Provides dynamic and versatile development capabilities.

---

### Code Structure

#### Key Files
- `.vscode/launch.json`: Configuration for debugging the extension.
- `src/commands/auditHtml.js`: Handles the WCAG auditing process.
- `src/commands/downloadReport.js`: Manages report downloads in various formats.
- `utils/apiClient.js`: Contains Axios client configuration for API communication.
- `config.js`: Stores application configurations, such as API URLs.
- `extension.js`: Entry point of the extension, registers commands with VS Code.
- `package.json`: Metadata, dependencies, and commands for the extension.

#### Commands
- **`WCAG: Audit HTML`**: Audits the currently open HTML file for WCAG compliance.
- **`WCAG: Download Report`**: Exports the accessibility report in the chosen format.

---

### How It Works
1. **Auditing**:
   - Sends the HTML content to the FastAPI backend via a POST request.
   - The backend analyzes the content and returns a report with detected issues.
2. **Report Generation**:
   - Sends a GET request to the FastAPI backend specifying the desired format.
   - The report is downloaded and saved locally.

---

### Contribution
- Submit issues or feature requests via GitHub.
- Create pull requests to contribute to the project.

---

### License
This extension is licensed under the **MIT License**.

---

### Contact
- **Carlos José Castro Galante**

---

## Versión en Español

### Resumen
La extensión **WCAG Auditor** es una herramienta para Visual Studio Code desarrollada por **Carlos José Castro Galante**, que permite a los desarrolladores auditar contenido HTML para verificar su cumplimiento con las pautas WCAG (Web Content Accessibility Guidelines). Esta extensión interactúa con un microservicio FastAPI para proporcionar retroalimentación en tiempo real y generar informes.

---

### Funcionalidades
- **Auditoría de Accesibilidad HTML**: Evalúa contenido HTML en base a los niveles A, AA y AAA de las pautas WCAG.
- **Generación Personalizada de Informes**: Exporta informes en formatos TXT o PDF.
- **Integración con FastAPI**: Utiliza un microservicio backend para análisis y reportes en tiempo real.
- **Amigable para Desarrolladores**: Comandos simples accesibles desde el Command Palette de VS Code.

---

### Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/your-repo-url/wcag-auditor.git
   ```
2. Abre la carpeta en Visual Studio Code.
3. Instala las dependencias necesarias:
   ```bash
   npm install
   ```
4. Inicia la extensión en modo desarrollo:
   - Presiona `F5` en VS Code.
   - Selecciona el entorno `Run Extension`.

---

### Uso

#### Auditoría de HTML
1. Abre un archivo HTML en Visual Studio Code.
2. Abre el Command Palette (`Ctrl+Shift+P` o `Cmd+Shift+P` en macOS).
3. Selecciona el comando `WCAG: Auditar HTML`.
4. Escoge el nivel de cumplimiento WCAG (A, AA, AAA).
5. Revisa los resultados:
   - Si no se encuentran problemas, se muestra un mensaje de éxito.
   - Si se detectan problemas, se muestra una lista con el nivel de severidad.

#### Descarga de Informes
1. Abre el Command Palette y selecciona `WCAG: Descargar Informe`.
2. Escoge el formato del informe (TXT o PDF).
3. El informe se guarda en el directorio del workspace actual.

---

### Herramientas y Tecnologías
- **API de Visual Studio Code**: Para crear y gestionar comandos de extensión.
- **FastAPI**: Microservicio backend para analizar contenido HTML.
- **Axios**: Cliente HTTP para interacciones con la API.
- **Node.js**: Entorno de ejecución para JavaScript.
- **JavaScript**: Proporciona desarrollo dinámico y versátil.

---

### Estructura del Código

#### Archivos Clave
- `.vscode/launch.json`: Configuración para depuración de la extensión.
- `src/commands/auditHtml.js`: Maneja el proceso de auditoría WCAG.
- `src/commands/downloadReport.js`: Administra la descarga de informes en diversos formatos.
- `utils/apiClient.js`: Contiene la configuración del cliente Axios para la comunicación con la API.
- `config.js`: Almacena configuraciones de la aplicación, como URLs de la API.
- `extension.js`: Punto de entrada de la extensión, registra comandos en VS Code.
- `package.json`: Metadatos, dependencias y comandos de la extensión.

#### Comandos
- **`WCAG: Auditar HTML`**: Audita el archivo HTML abierto actualmente para verificar cumplimiento WCAG.
- **`WCAG: Descargar Informe`**: Exporta el informe de accesibilidad en el formato elegido.

---

### Cómo Funciona
1. **Auditoría**:
   - Envía el contenido HTML al backend FastAPI mediante una solicitud POST.
   - El backend analiza el contenido y devuelve un informe con los problemas detectados.
2. **Generación de Informes**:
   - Envía una solicitud GET al backend FastAPI especificando el formato deseado.
   - El informe se descarga y guarda localmente.

---

### Contribución
- Envía problemas o solicitudes de características a través de GitHub.
- Crea pull requests para contribuir al proyecto.

---

### Licencia
Esta extensión está licenciada bajo la **Licencia MIT**.

---

### Contacto
- **Carlos José Castro Galante**

## License and Copyright

Copyright (c) 2024 Carlos José Castro Galante. All rights reserved.

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Licencia y Copyright

Copyright (c) 2024 Carlos José Castro Galante. Todos los derechos reservados.

Este proyecto está bajo la licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.