import json

users = json.load(open("users.json"))
users_archive = json.load(open("users_archive.json"))

users_archive["users"].update(users["users"])
users["users"] = {}

json.dump(users, open("users.json", "w"), indent=1)
json.dump(users_archive, open("users_archive.json", "w"), indent=1, sort_keys=True)
