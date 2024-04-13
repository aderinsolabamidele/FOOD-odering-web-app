from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy menu items
menu = {
    '1': {'name': 'Pizza', 'price': 10},
    '2': {'name': 'Burger', 'price': 5},
    '3': {'name': 'Salad', 'price': 8}
}

# Empty cart
cart = {}


@app.route('/')
def index():
    return render_template('index.html', menu=menu)


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item_id = request.form['item_id']
    if item_id in menu:
        if item_id in cart:
            cart[item_id]['quantity'] += 1
        else:
            cart[item_id] = {'name': menu[item_id]['name'], 'price': menu[item_id]['price'], 'quantity': 1}
    return redirect(url_for('index'))


@app.route('/cart')
def show_cart():
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render_template('cart.html', cart=cart, total_price=total_price)


if __name__ == '__main__':
    app.run(debug=True,port=5000)