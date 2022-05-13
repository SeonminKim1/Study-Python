from flask import Flask, render_template

app = Flask(__name__)

# Page
@app.route('/')
def home():
    return render_template('modal.html')

### ================ Main ================
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)  # 기본포트값 5000으로 설정
