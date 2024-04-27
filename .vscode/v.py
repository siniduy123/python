import random

# reference of a dict and copy of a dict
new_dict = {
    "name": "hello",
}

second_dict = new_dict.copy()

new_dict["name"] = "bye"

print(second_dict["name"])


user = {
    "name": "Yared",
    "age": 23,
    "username": "yared",
    "email": "jaredyared83@gmail.com"
}

users = []
names = ["Yared", "Sinidu", "Helina", "Abebe", "Kebede"]
status = {}

for name in names:
    activity = ["inactive", "active"]
    index = random.randint(0, 1)
    status[name] = activity[index]
    
print(status)

"""
[{
    "name": "Yared",
    "age": "23",
    "username": "yared",
    "email": "jaredyared83@gmail.com"
},
{
    "name": "Yared",
    "age": "23",
    "username": "yared",
    "email": "jaredyared83@gmail.com"
},
{
    "name": "Yared",
    "age": "23",
    "username": "yared",
    "email": "jaredyared83@gmail.com"
},
{
    "name": "Yared",
    "age": "23",
    "username": "yared",
    "email": "jaredyared83@gmail.com"
},
{
    "name": "Yared",
    "age": "23",
    "username": "yared",
    "email": "jaredyared83@gmail.com",
}]
"""

for i in range(5):
    users.append(user.copy())

for user, name in zip(users, names):
    print(user, name)
    user["name"] = name

print(users)
status = {}
for user in users:
    user["status"]=status[user["names"]]
print(user)
