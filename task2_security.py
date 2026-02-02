def save_user(name, email, password):
    with open("users.txt", "a") as f:
        # RISK: Storing password in plain text
        f.write(f"{name},{email},{password}\n")

save_user("Suraj", "suraj@example.com", "password123")

import hashlib

def save_user_secure(name, email, password):
    # SECURE: Hash the password before storing
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    
    with open("users_secure.txt", "a") as f:
        f.write(f"{name},{email},{hashed_pw}\n")

save_user_secure("Suraj", "suraj@example.com", "password123")