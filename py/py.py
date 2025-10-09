import streamlit as st
from streamlit_sortables import sort_items
from google_form_scraper import get_google_form_options

st.title("Przestaw kolejność uczestników")

url = st.text_input("Podaj link do publicznego formularza Google:")

if url:
    options = get_google_form_options(url)
    options.insert(0, "-----------------------------------------------------------------------------")

    if not options:
        st.error("Nie udało się znaleźć żadnych odpowiedzi. Formularz musi być publiczny i mieć wypełnione odpowiedzi.")
    else:
        st.subheader("Przeciągnij i zmień kolejność odpowiedzi")
        sorted_options = sort_items(options, direction="vertical")
