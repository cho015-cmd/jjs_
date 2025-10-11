import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="HTML 뷰어",
    page_icon="📄",
    layout="wide",
)

def open_new_tab(url):
    open_script = f"""<script>window.open('{url}', '_blank').focus();</script>"""
    components.html(open_script, height=0)

def read_html_file(file_path):
    try:
        # STREAMLIT_STATIC_PATH 환경 변수가 설정된 경우를 고려하여 경로를 찾습니다.
        streamlit_static_path = os.getenv("STREAMLIT_STATIC_PATH")
        if streamlit_static_path:
            full_path = os.path.join(streamlit_static_path, file_path)
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            full_path = os.path.join(base_dir, file_path)
        
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"❌ '{file_path}' 파일을 찾을 수 없습니다. 경로: `{full_path}`")
        return None

if __name__ == "__main__":
    
    # 1. 외부 URL 새 탭 열기
    st.header("새 탭에서 페이지 열기")
    new_tab_url = "https://www.google.com" 
    
    if st.button("Google 열기 🚀"):
        open_new_tab(new_tab_url)

    st.markdown("---")

    # 2. HTML 파일 선택 및 표시
    st.header("HTML 콘텐츠 선택")
    
    html_files = {
        "index.html": "htmls/index.html",
        "index2.html": "htmls/index2.html",
        "index3.html": "htmls/index3.html",
        "index4.html": "htmls/index4.html",
    }
    
    selected_name = st.selectbox(
        "표시할 HTML 페이지 선택:",
        options=list(html_files.keys())
    )
    
    file_path_to_display = html_files[selected_name]
    html_content = read_html_file(file_path_to_display)

    if html_content:
        st.subheader(f"파일: `{file_path_to_display}`")
        
        # 🌟 height를 명시적으로 지정하지 않아야 합니다. 🌟
        # HTML에 추가한 JavaScript가 높이를 동적으로 설정합니다.
        st.components.v1.html(
            html_content, 
            scrolling=True
        )
