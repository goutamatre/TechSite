from pymongo import MongoClient

with open("/media/goutam/projects/TechSite (1)/app/DB/my_credentials", "r") as file:
    username = file.readline().strip()
    password=file.readline().strip()
# client=MongoClient( f"mongodb+srv://{username}:{password}@cluster0.xnjfjzj.mongodb.net/")
# client=MongoClient(f"mongodb+srv://{username}:{password}@cluster0.byjpf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
client=MongoClient(f"mongodb+srv://{username}:{password}@cluster0.byjpf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db=client["Sign_in"]
collection=db["users"]


def signin(user_name,user_password,email):
    # print(f"SIgnin sucessfull")
    db.collection.insert_one({ #find_one returns single value or none,not a cursor but find returns curser(true if no results are there)
        "user_name":user_name, 
        "user_password":user_password,
        "email":email
        
        })
    