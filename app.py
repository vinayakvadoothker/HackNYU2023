from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']

    # Save the data to a text file
    with open('user_data.txt', 'a') as file:
        file.write(f'{name},{email},{username},{password}\n')

    return 'Registration successful!'

if __name__ == '__main__':
    app.run(debug=True)
