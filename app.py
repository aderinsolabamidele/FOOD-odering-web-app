from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Menus with Images for different cuisines
menus = {
    'african': [
        {'id': '1', 'name': 'Jollof Rice', 'price': 12, 'image': 'static/jollof.jpg'},
        {'id': '2', 'name': 'Pounded Yam & Egusi', 'price': 15, 'image': 'static/pounded_yam.jpg'},
        {'id': '3', 'name': 'Suya', 'price': 10, 'image': 'static/suya.jpg'}
    ],
    'chinese': [
        {'id': '4', 'name': 'Fried Rice', 'price': 10, 'image': 'static/fried_rice.jpg'},
        {'id': '5', 'name': 'Kung Pao Chicken', 'price': 14, 'image': 'static/kung_pao.jpg'},
        {'id': '6', 'name': 'Spring Rolls', 'price': 7, 'image': 'static/spring_rolls.jpg'}
    ],
    'continental': [
        {'id': '7', 'name': 'Steak & Fries', 'price': 18, 'image': 'static/steak_fries.jpg'},
        {'id': '8', 'name': 'Pasta Alfredo', 'price': 13, 'image': 'static/pasta_alfredo.jpg'},
        {'id': '9', 'name': 'Caesar Salad', 'price': 9, 'image': 'static/caesar_salad.jpg'}
    ]
}

cart = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/menu')
def menu():
    return render_template('menu.html', menus=menus)


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item_id = request.form['item_id']
    
    for cuisine, items in menus.items():
        for item in items:
            if item['id'] == item_id:
                if item_id in cart:
                    cart[item_id]['quantity'] += 1
                else:
                    cart[item_id] = {**item, 'quantity': 1, 'cuisine': cuisine}
                break
    
    return redirect(url_for('show_cart'))


@app.route('/cart')
def show_cart():
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render_template('cart.html', cart=cart, total_price=total_price)


@app.route('/clear_cart')
def clear_cart():
    cart.clear()
    return redirect(url_for('menu'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)


