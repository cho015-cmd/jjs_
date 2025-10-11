import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="내 페이지",
    page_icon="📂",
    layout="wide",
)

def open_new_tab(url):
    """새 브라우저 탭에 URL을 엽니다."""
    open_script = f"""
        <script>
        window.open('{url}', '_blank').focus();
        </script>
    """
    components.html(open_script, height=0)

def read_html_file(file_path):
    try:
        streamlit_static_path = os.getenv("STREAMLIT_STATIC_PATH", "")
        if streamlit_static_path:
            full_path = os.path.join(streamlit_static_path, file_path)
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            full_path = os.path.join(base_dir, file_path)

        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"Error: File '{file_path}' not found at '{full_path}'.")
        return None

if __name__ == "__main__":
    
    # 1. 새 탭(창) 열기 버튼
    # 이 기능은 'htmls/index4.html' 파일 자체가 웹에서 접근 가능한 URL로 존재할 때 사용합니다.
    # 예시로 구글 URL을 사용합니다. 실제 URL로 변경하세요.
    new_tab_url = "https://www.google.com" 
    
    st.header("새 탭에서 외부 페이지 열기")
    if st.button("새 탭 열기 (Google 예시) 🚀"):
        open_new_tab(new_tab_url)

    st.markdown("---")

    # 2. 기존 HTML 파일 내용을 현재 Streamlit 페이지 내부에 표시
    st.header("현재 페이지에 HTML 파일 내용 표시")
    
    html_file_path = "htmls/index4.html"
    html_content = read_html_file(html_file_path)

    if html_content:
        st.components.v1.html(html_content, height=800, scrolling=True)
