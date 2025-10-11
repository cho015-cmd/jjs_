import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="HTML 뷰어",
    page_icon="📄",
    layout="wide",
)

# 🌟 파일별 예상 높이 사전 정의 🌟
# (이 값을 실제 콘텐츠 길이에 맞춰 조정해야 합니다.)
FILE_HEIGHTS = {
    "index.html": 1000,   # 예시 높이
    "index2.html": 800,   # 예시 높이
    "index3.html": 1500,  # 예시 높이 (긴 콘텐츠 가정)
    "index4.html": 1200,  # 예시 높이
}
# 기본값 (사전에 정의되지 않은 파일 대비)
DEFAULT_HEIGHT = 1000

def read_html_file(file_path):
    try:
        # 파일 경로 설정
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
    
    # 상단 제목 영역 간결화
    st.markdown("## HTML 콘텐츠 뷰어")
    
    html_files = {
        "index.html": "htmls/index.html",
        "index2.html": "htmls/index2.html",
        "index3.html": "htmls/index3.html",
        "index4.html": "htmls/index4.html",
    }
    
    # Selectbox 영역
    selected_name = st.selectbox(
        "표시할 HTML 페이지 선택:",
        options=list(html_files.keys())
    )
    
    file_path_to_display = html_files[selected_name]
    html_content = read_html_file(file_path_to_display)
    
    # 🌟 선택된 파일 이름에 맞는 높이를 가져옵니다. 🌟
    # 파일명에서 'htmls/' 경로를 제거하여 딕셔너리 키로 사용합니다.
    file_key = selected_name 
    current_height = FILE_HEIGHTS.get(file_key, DEFAULT_HEIGHT)

    if html_content:
        st.info(f"선택된 파일: `{file_path_to_display}` (지정 높이: {current_height}px)")
        
        # 🌟 파일별로 지정된 height를 사용합니다. 🌟
        st.components.v1.html(
            html_content, 
            height=current_height, 
            scrolling=True
        )
