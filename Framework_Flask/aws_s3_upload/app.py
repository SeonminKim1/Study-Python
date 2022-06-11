import boto3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/fileupload', methods=['POST'])
def file_upload():
    file = request.files['file']
    print(file)
    s3 = boto3.client('s3')
    # s3 = 	boto3.client('s3', aws_access_key_id = AWS_ACCESS_KEY, aws_secret_access_key = AWS_SECRET_KEY)
    s3.put_object(
        ACL="public-read",
        Bucket= "smkimtestbucket", # "{버킷이름}",
        Body=file, # 업로드할 파일 객체
        Key=file.filename, # S3에 업로드할 파일의 경로
        ContentType=file.content_type # 메타데이터 설정
    ) 
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run()