from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin

session = HTMLSession()

def get_all_forms(url):
    res = session.get(url)
    soup = BeautifulSoup(res.html.html, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value =input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


url = input("[?] Enter url: ")
forms = get_all_forms(url)
for i, form in enumerate(forms, start=1):
    form_details = get_form_details(form)
    print("="*50, f"form #{i}", "="*50)
    print(form_details)