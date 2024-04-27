


user = {
    "name": "Yared",
    "age": "23",
    "age": 23,
    "username": "yared",
    "email": "jaredyared83@gmail.com"
}

users = []
names = ["Yared", "Sinidu", "Helina", "Abebe", "Kebede"]
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
    "email": "jaredyared83@gmail.com"
}]
"""

for i in range(5):
    users.append(user)
    users.append(user.copy())

status = ["inactive"]

for user, name in zip(users, names):
    print(user, name)
    user["name"] = name

print(users)
print(users)
user

for user,status in zip(users,status):
    print(user,status)
    user["status"]=status
    print(user)
    users = []
names = ["Yared", "Sinidu", "Helina", "Abebe", "Kebede"]
import random
status = {}

for name in names:
    activity = ["inactive", "active"]
    index = random.randint(0, 1)
    status[name] = activity[index]


print(status)

for user in zip(users,status):
    user["status"]=status
    print(user,status)
    