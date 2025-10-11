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
    """HTML 파일을 읽고 내용을 반환합니다."""
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
        st.error(f"❌ **파일을 찾을 수 없습니다!**")
        st.info(f"'{file_path}' 파일을 확인해 주세요. 예상 경로: `{full_path}`")
        return None

if __name__ == "__main__":
    
    # 1. 새 탭(창) 열기 기능
    st.header("새 탭에서 외부 페이지 열기")
    new_tab_url = "https://docs.streamlit.io/" 
    
    if st.button("새 탭 열기 (Streamlit 문서 예시) 🚀"):
        open_new_tab(new_tab_url)

    st.markdown("---")

    # 2. HTML 파일 선택 및 표시 (Selectbox 사용)
    st.header("HTML 파일 콘텐츠 선택 및 표시")
    
    html_files = {
        "index.html (첫 번째 페이지)": "htmls/index.html",
        "index2.html (두 번째 페이지)": "htmls/index2.html",
        "index3.html (세 번째 페이지)": "htmls/index3.html",
        "index4.html (네 번째 페이지)": "htmls/index4.html",
    }
    
    selected_name = st.selectbox(
        "표시할 HTML 페이지를 선택하세요:",
        options=list(html_files.keys())
    )
    
    file_path_to_display = html_files[selected_name]
    html_content = read_html_file(file_path_to_display)

    if html_content:
        st.subheader(f"선택된 파일: `{file_path_to_display}`")
        
        # 🌟 핵심 수정: height 매개변수를 제거하거나 매우 큰 값으로 설정합니다.
        # height를 제거하면 Streamlit이 콘텐츠 길이를 자동으로 감지하여 확장합니다.
        st.components.v1.html(
            html_content, 
            # height=None,  # height를 지정하지 않거나 None으로 설정합니다.
            scrolling=True  # Streamlit 페이지 자체의 스크롤은 허용합니다.
        )
