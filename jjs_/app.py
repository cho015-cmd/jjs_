import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="HTML 뷰어",
    page_icon="📄",
    layout="wide",
)

def read_html_file(file_path):
    try:
        # 파일 경로 설정 (Streamlit 환경 변수 고려)
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
    
    # 🌟 상단 제목 영역 간결화 🌟
    st.markdown("## HTML 콘텐츠 뷰어")
    
    html_files = {
        "index.html": "htmls/index.html",
        "index2.html": "htmls/index2.html",
        "index3.html": "htmls/index3.html",
        "index4.html": "htmls/index4.html",
    }
    
    # 🌟 Selectbox 영역 🌟
    selected_name = st.selectbox(
        "표시할 HTML 페이지 선택:",
        options=list(html_files.keys()),
        # selectbox 위에 공간을 더 줄이고 싶다면 label_visibility="collapsed" 사용 가능
        # label_visibility="collapsed" 
    )
    
    file_path_to_display = html_files[selected_name]
    html_content = read_html_file(file_path_to_display)

    if html_content:
        # 파일 경로 정보를 st.info로 변경하여 시각적으로 덜 강조
        st.info(f"선택된 파일: `{file_path_to_display}`")
        
        # 🌟 HTML 콘텐츠 표시: 높이 설정을 제거하여 자동으로 전체를 띄움 (JavaScript 수정 필수) 🌟
        st.components.v1.html(
            html_content, 
            scrolling=True
        )
