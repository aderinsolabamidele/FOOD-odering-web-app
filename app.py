from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Menus with Images for different cuisines
menus = {
    'african': {
        '1': {'name': 'Jollof Rice', 'price': 12, 'image': 'static/jollof.jpg'},
        '2': {'name': 'Pounded Yam & Egusi', 'price': 15, 'image': 'static/pounded_yam.jpg'},
        '3': {'name': 'Suya', 'price': 10, 'image': 'static/suya.jpg'}
    },
    'chinese': {
        '1': {'name': 'Fried Rice', 'price': 10, 'image': 'static/fried_rice.jpg'},
        '2': {'name': 'Kung Pao Chicken', 'price': 14, 'image': 'static/kung_pao.jpg'},
        '3': {'name': 'Spring Rolls', 'price': 7, 'image': 'static/spring_rolls.jpg'}
    },
    'continental': {
        '1': {'name': 'Steak & Fries', 'price': 18, 'image': 'static/steak_fries.jpg'},
        '2': {'name': 'Pasta Alfredo', 'price': 13, 'image': 'static/pasta_alfredo.jpg'},
        '3': {'name': 'Caesar Salad', 'price': 9, 'image': 'static/caesar_salad.jpg'}
    }
}

cart = {}
selected_cuisine = None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/menu', methods=['POST'])
def menu():
    global selected_cuisine
    selected_cuisine = request.form['cuisine']
    return render_template('menu.html', menu=menus[selected_cuisine], cuisine=selected_cuisine)


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    global selected_cuisine
    item_id = request.form['item_id']
    
    if selected_cuisine and item_id in menus[selected_cuisine]:
        if item_id in cart:
            cart[item_id]['quantity'] += 1
        else:
            cart[item_id] = {
                'name': menus[selected_cuisine][item_id]['name'],
                'price': menus[selected_cuisine][item_id]['price'],
                'image': menus[selected_cuisine][item_id]['image'],
                'quantity': 1,
                'cuisine': selected_cuisine
            }
    
    return redirect(url_for('show_cart'))


@app.route('/cart')
def show_cart():
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render_template('cart.html', cart=cart, total_price=total_price)


@app.route('/clear_cart')
def clear_cart():
    cart.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
