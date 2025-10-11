import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="HTML 고급 뷰어",
    page_icon="✨",
    layout="wide",
)

# 파일별 예상 높이 사전 정의 (이 값은 실제 콘텐츠에 맞춰 조정해야 함)
FILE_HEIGHTS = {
    "index.html": 1000,
    "index2.html": 800,
    "index3.html": 1500,
    "index4.html": 1200,
}
DEFAULT_HEIGHT = 1000

# 🌟 HTML 파일 목록 및 고급스러운 설명 🌟
# 사용자에게 보여줄 이름과 실제 파일 경로를 분리합니다.
HTML_FILE_MAP = {
    "📊 프로젝트 개요 (index.html)": "htmls/index.html",
    "📈 데이터 분석 결과 (index2.html)": "htmls/index2.html",
    "📑 상세 보고서 (index3.html)": "htmls/index3.html",
    "⚙️ 시스템 구성도 (index4.html": "htmls/index4.html",
}

def read_html_file(file_path):
    try:
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
    
    # 🌟 상단 제목과 선택 영역을 분리하여 깔끔하게 배치 🌟
    st.markdown("## ✨ 프로젝트 문서 고급 뷰어")
    
    # 1. 파일 선택 (고급진 옵션 이름 사용)
    selected_option = st.selectbox(
        "표시할 문서를 선택하세요:",
        options=list(HTML_FILE_MAP.keys())
    )
    
    # 선택된 옵션에서 실제 파일 경로를 가져옵니다.
    file_path_to_display = HTML_FILE_MAP[selected_option]
    
    # 2. 파일 내용 로드 및 표시
    html_content = read_html_file(file_path_to_display)
    
    # 선택된 옵션 이름에서 실제 파일 이름만 추출하여 높이 맵에서 찾습니다.
    # 예: "📊 프로젝트 개요 (index.html)" -> "index.html"
    import re
    match = re.search(r'\((.*?)\)', selected_option)
    file_key = match.group(1) if match else None

    current_height = FILE_HEIGHTS.get(file_key, DEFAULT_HEIGHT)

    st.markdown("---")
    
    if html_content:
        st.subheader(f"선택된 문서: {selected_option}")
        st.info(f"파일 경로: `{file_path_to_display}` | 지정 높이: {current_height}px")
        
        # 파일별로 지정된 height를 사용하여 잘림을 방지
        st.components.v1.html(
            html_content, 
            height=current_height, 
            scrolling=True
        )
