def register_user(name, email, username, password):
    with open('users.txt', 'a') as file:
        file.write(f"{name},{email},{username},{password}\n")
