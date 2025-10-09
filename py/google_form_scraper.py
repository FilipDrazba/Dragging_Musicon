import requests
from bs4 import BeautifulSoup

def get_google_form_options(url: str) -> list[str]:
    """
    Pobiera wszystkie unikalne odpowiedzi z publicznego formularza Google,
    pomija puste odpowiedzi i opcję 'Wybierz'.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    option_elements = soup.select('[role="option"]')

    seen = set()
    options = []

    for elem in option_elements:
        text = elem.get_text(strip=True)
        if text and text not in seen and text != "Wybierz":
            seen.add(text)
            options.append(text)

    return options
