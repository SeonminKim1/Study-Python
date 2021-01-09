from flask import Flask, render_template, send_from_directory, request, redirect,send_file

# Flask 객체 생성
app = Flask(__name__)

@app.route('/')
def database():
    # generate some file name
    # save the file in the `database_reports` folder used below
    stored_file_name = 'rf_iris.onnx'
    return render_template('database.html', filename=stored_file_name)

@app.route('/database_download/<filename>')
def database_download(filename):
    return send_from_directory('db', filename)


#서버 실행
if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5070, debug = True)