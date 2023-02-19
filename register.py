import hashlib

def register_user(name, email, username, password):
    # Hash the password using SHA-256 algorithm
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Store user data in a text file
    with open('users.txt', 'a') as file:
        file.write(f'{name},{email},{username},{hashed_password}\n')
