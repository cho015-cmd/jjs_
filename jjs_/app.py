from flask import Flask, render_template

# Flask 애플리케이션 생성
# 'template_folder'를 현재 폴더(.)로 설정하여 HTML 파일을 바로 찾도록 합니다.
app = Flask(__name__, template_folder='.')

# 기본 URL('/')에 대한 라우트 설정
@app.route('/')
def index():
    """
    'index2.html' 파일을 렌더링하는 함수입니다.
    """
    return render_template('index2.html')

# 이 스크립트가 직접 실행될 때 웹 서버를 시작합니다.
if __name__ == '__main__':
    # 디버그 모드로 애플리케이션을 실행합니다.
    # 코드를 변경하면 서버가 자동으로 재시작됩니다.
    app.run(debug=True)
