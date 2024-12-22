from bs4 import BeautifulSoup
import requests

def fetch_html(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_html(html_content: str):
    return BeautifulSoup(html_content, "lxml")
