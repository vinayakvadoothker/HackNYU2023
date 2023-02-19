from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/phone-number', methods=['GET', 'POST'])
def phone_number():
    if request.method == "GET":
        return render_template('pages-login.html')
    else:
        phone_number = request.form['phone-number']
        with open('phone_numbers.txt', 'a') as f:
            f.write(phone_number + '\n')

    return redirect('home.html')

@app.route('/submit_trade', methods=['POST'])
def submit_trade():
    stock_price = request.form['stock_price']
    with open('trades.txt', 'a') as f:
        f.write(f'Stock price: {stock_price}\n')
    return 'Trade submitted successfully!'

    return redirect('home.html')

if __name__ == '__main__':
    app.run()
