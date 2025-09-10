import streamlit as st
import streamlit.components.v1 as components

# 페이지 제목 설정
st.title("⚽ 축구팀 구성 시뮬레이터 (Streamlit)")
st.markdown("---")

# index2.html 파일 경로 설정
html_file_path = "index2.html"

try:
    # 파일 경로를 열고 내용을 읽어옵니다.
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Streamlit에 HTML 내용을 표시합니다.
    components.html(html_content, height=900, scrolling=True)

except FileNotFoundError:
    st.error(f"Error: The file '{html_file_path}' was not found.")
    st.info("Please make sure 'index2.html' is in the same directory as this Python script.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")
