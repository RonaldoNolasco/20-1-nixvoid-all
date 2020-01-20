# Documentation on https://fakerestapi.azurewebsites.net/Help
import requests as r
import json
urlBase = "https://gorest.co.in"
k = "YGBDiXn" + "Pubk"
k+= "lcFXDzBh4bu" +"MnqNzVwx"+"vZUclx"

# Obtener users

response = r.get(urlBase+"/public-api/users?access-token="+k)
users = response.json()

#Tenerlo como json (todo)
print(json.dumps(users, indent=2, sort_keys=True))

#Tenerlo como csv (id, nombres y email)
"""
for user in users["result"]:
    print(user["id"], user["first_name"], user["last_name"], user["email"], sep=",")
"""

# Obtener nombres de usuarios completos y correo
"""
response = r.get(urlBase+"/public-api/posts?access-token="+k)
posts = response.json()
print(json.dumps(posts, indent=2, sort_keys=True))
"""

#/public-api/comments
#/public-api/albums
#/public-api/photos