from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # List 
    animal_list = ['호랑이','사자','표범']
    fruit_dict = { # Dict
        '사과':35,
        '배':20,
        '귤':25
    }
    # List 내 Dicionary
    multi_list = [
        {'movie':'a', 'rating':30},
        {'movie':'b', 'rating':10},
        {'movie':'c', 'rating':20},
    ]
    return render_template("index.html", 
                            fruits = fruit_dict, 
                            animals = animal_list,
                            multis = multi_list)

if __name__ == '__main__':
    app.run(debug=True)