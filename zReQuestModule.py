import requests

# r  = requests.get("https://xkcd.com/353/")
# print(r) # prints object
# print(dir(r))
# print(help(r))
# print(r.text) #  gives content of page in unicode

# r  = requests.get("https://source.unsplash.com/random")
# print(r.content) # prints content of the page in bytes

# with open("Unsplash.jpg","wb") as f:
#     f.write(r.content)
#

# print(r.status_code) # prints the status code ex; 200, 300,400,500
#
# print(r.ok) # Prints true if status code is less than 400

# print(r.headers)  # indepth response headers as dictionary

##


# r = requests.get("https://httpbin.org/get")
# print(r.text)

##
# payload = {'username':'jeevan','password':'testing'}
# r = requests.post("https://httpbin.org/post",data=payload)
# print(r.text)

##
# r = requests.get("https://httpbin.org/basic-auth/jeevan/testing",auth=('jeevan','testing'))
# print(r.text)

# r = requests.get("https://httpbin.org/delay/6",timeout= 7)
# print(r.status_code)