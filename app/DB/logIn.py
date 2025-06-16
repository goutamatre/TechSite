from DB.SignIn import db


def login(email, user_password):
    user=db.collection.find_one({
        "email": email,
        "user_password": user_password
    })
    return user