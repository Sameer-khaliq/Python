import json

# JSON string → Python dict
raw_json = '{"name": "Sameer", "age": 22}'
data = json.loads(raw_json)

print(data["name"])   # Sameer
print(data["age"])    # 22
print(type(data))     # <class 'dict'>


# Accessing nested json data
import json

raw = '''
{
  "user": {
    "id": 1,
    "name": "Sameer",
    "address": {
      "city": "Gujrat",
      "country": "Pakistan"
    },
    "skills": ["Python", "HTTP", "JSON"]
  }
}
'''

data = json.loads(raw)

# Accessing nested values
print(data["user"]["name"])               # Sameer
print(data["user"]["address"]["city"])    # Gujrat
print(data["user"]["skills"][0])          # Python
print(data["user"]["skills"][1])          # HTTP
print(data["user"]["skills"][2])          # JSON

#Looping through a JSON array
import json

raw = '''
[
  {"id": 1, "name": "Ali", "email": "ali@test.com"},
  {"id": 2, "name": "Sara", "email": "sara@test.com"},
  {"id": 3, "name": "Usman", "email": "usman@test.com"}
]
'''
data  = json.loads(raw)
for user in data:
    print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")


# request types
# get, post, put, delete
# get → data retrieve karne ke liye
# post → data create karne ke liye
# put → data update karne ke liye
# delete → data delete karne ke liye
# status codes
# 200 → OK (success)
# 201 → Created (successfully created)
# 400 → Bad Request (client error)
# 404 → Not Found (client error)
# 500 → Internal Server Error (server error)
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/2")
print(response.json())
print(response.status_code)

import requests

# These two are identical:
# https://jsonplaceholder.typicode.com/posts?userId=1

params = {"userId": 1}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)

posts = response.json()
print(f"Found {len(posts)} posts")


#___post request___
import requests

new_post ={
    "name": "sameer",
     "age": 20,
      "userid": 1011
}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json = new_post)
print(response.status_code)
# print(response.json())

import requests

updated_data = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated body text",
    "userId": 1
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=updated_data
)

print(response.status_code)   # 200
print(response.json())


import requests

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)   # 200



#Challenge 1 — Fetch all users, print name and email

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    users = response.json()
    for user in users:
        print(f"Name: {user['name']}, || Email: {user['email']}")


#Challenge 2 — Fetch all posts, filter only posts by userId = 1

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

if response.status_code == 200:
    all_posts = response.json()
    
    # Filter using list comprehension
    user1_posts = [post for post in all_posts if post["userId"] == 1]
    
    print(f"User 1 has {len(user1_posts)} posts\n")
    
    for post in user1_posts:
        print(f"Title: {post['title']}")
        print(f"Body: {post['body'][:60]}...")
        print("---")



import requests

new_post = {
    "title": "My HTTP Day",
    "body": "Today I learned GET, POST, PUT, DELETE and status codes",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
)

print(f"Status: {response.status_code}")   # 201

created = response.json()
print(f"Created post with id: {created['id']}")
print(f"Title: {created['title']}")