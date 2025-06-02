#create a Dictinary in python
dict1={"id":28,"name":"Ramakant","age":21,"marks":(98,25,45)}
print(dict1)

# Using Update Method
dict2={"email":"ram@gmail.com"}
dict1.update(dict2)
print(dict1)

# Using Keys Method
print(dict1.keys())

# Using Values Method
print(dict1.values())

# Using Items Method
print(dict1.items())

# Using Get Method
print(dict1.get("name"))
print(dict1.get("div"))

# Using Pop Method
print(dict1.pop("age"))
print(dict1)

# Using Del Method 
del dict1["email"]
print(dict1)

del dict1
print(dict1)

