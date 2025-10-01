import streamlit as st
import os

st.set_page_config(
    page_title="내 페이지",
    page_icon="📂",
    layout="wide",
)

# Streamlit 환경에서 정적 파일의 경로를 가져옵니다.
streamlit_static_path = os.getenv("STREAMLIT_STATIC_PATH", "")

def read_html_file(file_path):
    """
    Reads an HTML file and returns its content.
    """
    try:
        # Construct an absolute path based on the current script's directory
        # 스크립트의 현재 디렉터리를 기준으로 절대 경로를 구성합니다.
        # Streamlit 환경 변수를 활용하여 경로를 보정합니다.
        if streamlit_static_path:
            full_path = os.path.join(streamlit_static_path, file_path)
        else:
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
    html_file_path = "htmls/index.html"
    html_content = read_html_file(html_file_path)

    if html_content:
        # Render the HTML content
        # HTML 콘텐츠를 렌더링합니다.
        st.components.v1.html(html_content, height=800, scrolling=True)


