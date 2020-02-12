import requests

parameter = input("Enter Parameter: ")
response = requests.get('https://jsonplaceholder.typicode.com/todos/' + parameter).json()

print('userId    : ' + str(response['userId']))
print('id        : ' + str(response['id']))
print('title     : ' + str(response['title']))
print('completed : ' + str(response['completed']))