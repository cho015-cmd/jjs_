import streamlit as st
import streamlit.components.v1 as components
import os

# 페이지 제목 설정
st.title("⚽ 축구팀 구성 시뮬레이터 (Streamlit)")
st.markdown("---")

# index2.html 파일 경로 설정
html_file_path = "index2.html"

try:
    # 파일이 존재하는지 확인합니다.
    if not os.path.exists(html_file_path):
        raise FileNotFoundError

    # 파일 경로를 열고 내용을 읽어옵니다.
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Streamlit에 HTML 내용을 표시합니다.
    components.html(html_content, height=900, scrolling=True)

except FileNotFoundError:
    st.error(f"오류: '{html_file_path}' 파일을 찾을 수 없습니다.")
    st.info(f"'{os.getcwd()}' 경로에 해당 파일이 있는지 확인해 주세요.")
except Exception as e:
    st.error(f"예상치 못한 오류가 발생했습니다: {e}")
