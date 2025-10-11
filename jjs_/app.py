import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="HTML 탭 뷰어",
    page_icon="📑",
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

# HTML 파일 목록 및 탭 이름 설정
HTML_FILE_MAP = {
    "개요 📊": "htmls/index.html",
    "분석 결과 📈": "htmls/index2.html",
    "상세 보고서 📑": "htmls/index3.html",
    "시스템 구성 ⚙️": "htmls/index4.html",
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
    
    st.markdown("## 📑 프로젝트 문서 탭 뷰어")
    
    tab_names = list(HTML_FILE_MAP.keys())
    tabs = st.tabs(tab_names) # 탭 생성
    
    # 각 탭에 콘텐츠를 배치
    for i, tab_name in enumerate(tab_names):
        file_path_to_display = HTML_FILE_MAP[tab_name]
        
        with tabs[i]: # 해당 탭 컨테이너 내부에 콘텐츠 작성 시작
            html_content = read_html_file(file_path_to_display)
            
            # 파일 이름 추출 (예: '개요 📊' -> 'index.html')
            file_base_name = os.path.basename(file_path_to_display)
            current_height = FILE_HEIGHTS.get(file_base_name, DEFAULT_HEIGHT)

            if html_content:
                st.info(f"파일 경로: `{file_path_to_display}` | 지정 높이: {current_height}px")
                
                # 파일별로 지정된 height를 사용하여 잘림을 방지
                st.components.v1.html(
                    html_content, 
                    height=current_height, 
                    scrolling=True
                )
