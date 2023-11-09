# create a user class with properties ie name,age,location.
# detials
class user:
    def __init__(self, name ,age ,location):
        self.name = name
        self.age = age
        self.location = location
        
# creat a new instance of the user class(a new object) 
user = user("Taaka Esther", 20, "Busia Boarda")  

# access the users name and age.
print(user.name)
print(user.age)

# create a function for the user class the prints a users location
def print_location(self):
    print("users location:" ,self)

 # print the users location usins the function
print_location("Busia Boarda")    













    



