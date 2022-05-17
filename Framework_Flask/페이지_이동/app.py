from flask import Flask, render_template, redirect, request, url_for
 
app = Flask(__name__)
 
@app.route('/')
def main():
    return render_template('main.html')

# a태그 / JS window.location.href 방식
@app.route('/test/basic', methods=['GET'])
def test_basic():
    print('test 수신')
    return "Simple TEST"

# a태그 + url_for()
@app.route('/test/name', methods=['GET'])
def test_name():
    name = request.args.get('name')
    return "이름은" + name + "입니다."
 
# Form submit 방식 
@app.route('/test/animals', methods=['GET', 'POST'])
def test_animals():
    name = request.form['nm']
    return render_template('test.html', name=name)
 
# Redirect 방식
@app.route('/test/redir', methods=['GET'])
def test_redirect():
    return redirect(url_for('test_name', name='리다이랙트임'))
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)  # 기본포트값 5000으로 설정
