from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    parameter = 'parameter~~1'
    condition = 20 
    return render_template("index.html", params = parameter, condition=condition)

if __name__ == '__main__':
    app.run(debug=True)