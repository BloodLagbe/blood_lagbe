
# import requests module
import requests
  
# Making a get request
response = requests.get('https://bdaddress.herokuapp.com/')
  
# print response
print(response)
  
# print url
print(response.url)