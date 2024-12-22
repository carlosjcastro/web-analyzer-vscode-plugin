import requests

BASE_URL = "http://127.0.0.1:8000/audit"

response_url = requests.post(BASE_URL, json={"url": "https://www.w3.org/WAI/test-evaluate/conformance/"})
print("Response for URL test:", response_url.json())

html_content = """
<html>
<body>
    <img src="image.jpg">
    <form>
        <input id="username" type="text">
        <input type="password">
    </form>
</body>
</html>
"""
response_html = requests.post(BASE_URL, json={"html_content": html_content})
print("Response for HTML test:", response_html.json())
