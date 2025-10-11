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
        # Streamlit 환경 변수 또는 현재 스크립트 디렉터리를 기준으로 절대 경로를 구성합니다.
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
    st.header("새 탭에서 외부 페이지 열기")
    # 새 탭으로 열 페이지의 URL을 지정하세요.
    new_tab_url = "https://www.streamlit.io" 
    
    if st.button("새 탭 열기 (Streamlit 예시) 🚀"):
        open_new_tab(new_tab_url)

    st.markdown("---")

    # 2. 여러 HTML 파일 내용을 현재 Streamlit 페이지 내부에 표시 (탭 사용)
    st.header("HTML 파일 콘텐츠 표시")
    
    # 표시할 HTML 파일 목록
    html_files = {
        "페이지 1": "htmls/index.html",
        "페이지 2": "htmls/index2.html",
        "페이지 3": "htmls/index3.html",
        "페이지 4": "htmls/index4.html",
    }
    
    # Streamlit 탭 생성
    tabs = st.tabs(html_files.keys())

    # 각 탭에 해당하는 HTML 파일 내용 표시
    for tab_name, tab in zip(html_files.keys(), tabs):
        file_path = html_files[tab_name]
        
        with tab:
            st.subheader(f"파일: `{file_path}`")
            html_content = read_html_file(file_path)

            if html_content:
                # HTML 콘텐츠를 렌더링합니다. (현재 Streamlit 페이지 내의 iframe에 표시)
                st.components.v1.html(html_content, height=600, scrolling=True)
