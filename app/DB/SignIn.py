from pymongo import MongoClient

with open("app/DB/my_credentials", "r") as file:
    username = file.readline().strip()
    password=file.readline().strip()
    print(f" Username : {username}, pass: {password}")

client=MongoClient(f"mongodb+srv://{username}:{password}@cluster0.byjpf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db=client["Sign_in"]
collection=db["users"]

def signin(user_name,user_password,confirm_password,email):
    if user_password != confirm_password:
        raise ValueError("Passwords do not match.")

    existing_user = db.collection.find_one({
        "$or": [
            {"user_name": user_name},
            {"email": email}
        ]
    })
    if existing_user:
        raise ValueError("User alredy exists")
    
    db.collection.insert_one({ #find_one returns single value or none,not a cursor but find returns curser(true if no results are there)
        "user_name":user_name, 
        "user_password":user_password,
        "email":email
        
        })
