from DB.SignIn import db


def login(email, user_password):
    result = db.collection.find_one({
        "email": email,
        "user_password": user_password
    })
    if result:
        return True
    else:
        return False

