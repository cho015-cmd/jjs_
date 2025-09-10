import streamlit as st
import os

st.set_page_config(
    page_title="Football Team Builder",
    page_icon="⚽",
    layout="wide",
)

def read_html_file(file_path):
    """
    Reads an HTML file and returns its content.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        return html_content
    except FileNotFoundError:
        st.error(f"Error: The file '{file_path}' was not found.")
        st.info(f"Please make sure '{file_path}' is in the correct directory.")
        return None

if __name__ == "__main__":
    html_file_path = "index2.html"
    html_content = read_html_file(html_file_path)

    if html_content:
        # Render the HTML content
        st.components.v1.html(html_content, height=800, scrolling=True)
