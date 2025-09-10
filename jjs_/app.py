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
        # Construct an absolute path based on the current script's directory
        # 스크립트의 현재 디렉터리를 기준으로 절대 경로를 구성합니다.
        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_dir, file_path)

        with open(full_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        return html_content
    except FileNotFoundError:
        st.error(f"Error: The file '{file_path}' was not found.")
        st.info(f"Please make sure the file is located at '{full_path}'.")
        return None

if __name__ == "__main__":
    # You can now specify a relative path to the HTML file.
    # 이제 HTML 파일의 상대 경로를 지정할 수 있습니다.
    html_file_path = "index2.html"
    html_content = read_html_file(html_file_path)

    if html_content:
        # Render the HTML content
        # HTML 콘텐츠를 렌더링합니다.
        st.components.v1.html(html_content, height=800, scrolling=True)
