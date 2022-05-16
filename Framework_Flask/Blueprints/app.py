from flask import Flask
from routers import router_1
from routers import router_2

app = Flask(__name__)

app.register_blueprint(router_1.router1) # /money
app.register_blueprint(router_2.router2) # /greet

### ================ Main ================
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)  # 기본포트값 5000으로 설정
