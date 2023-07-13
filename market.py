from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '7812357216541', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '256486145874', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '3131268786132', 'price': 50}
    ]
    return render_template('market.html', items=items)
