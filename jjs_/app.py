import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="HTML 뷰어",
    page_icon="📄",
    layout="wide",
)

# (open_new_tab 함수는 그대로 유지)
def open_new_tab(url):
    open_script = f"""<script>window.open('{url}', '_blank').focus();</script>"""
    components.html(open_script, height=0)

# (read_html_file 함수는 그대로 유지)
def read_html_file(file_path):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_dir, file_path)
        
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"❌ '{file_path}' 파일을 찾을 수 없습니다. 경로를 확인해 주세요.")
        return None

if __name__ == "__main__":
    
    # (새 탭 열기 부분 생략)
    st.header("새 탭에서 페이지 열기")
    new_tab_url = "https://www.google.com" 
    if st.button("Google 열기 🚀"):
        open_new_tab(new_tab_url)
    st.markdown("---")

    # 2. HTML 파일 선택 및 표시
    st.header("HTML 콘텐츠 선택")
    
    html_files = {
        "index.html (첫 번째 페이지)": "htmls/index.html",
        "index2.html (두 번째 페이지)": "htmls/index2.html",
        "index3.html (세 번째 페이지)": "htmls/index3.html",
        "index4.html (네 번째 페이지)": "htmls/index4.html",
    }
    
    selected_name = st.selectbox(
        "표시할 HTML 페이지 선택:",
        options=list(html_files.keys())
    )
    
    file_path_to_display = html_files[selected_name]
    html_content = read_html_file(file_path_to_display)

    if html_content:
        st.subheader(f"파일: `{file_path_to_display}`")
        
        # 🌟 핵심: height 매개변수를 완전히 제거합니다. 🌟
        # HTML 파일에 위에서 설명한 JavaScript 코드를 추가했다면, 
        # Streamlit이 자동으로 높이를 동적으로 조정합니다.
        st.components.v1.html(
            html_content, 
            scrolling=True
        )
