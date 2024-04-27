user = {
    "name": "Yared",
    "age": "23",
    "username": "yared",
    "email": "jaredyared83@gmail.com"
}

users = []
names = ["Yared", "Sinidu", "Helina", "Abebe", "Kebede"]

for i in range(5):
    users.append(user.copy)
    for i in range(5):
        users.append(user)
    users.append(user.copy())



for user, name in zip(users, names):
    print(user, name)
    user["name"] = name
    print(users)
print(users)
users.append("status inactive")
    