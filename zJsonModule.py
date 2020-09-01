import json

data = '{"var1":"jeevan","var2":120}'

parsed =json.loads(data)
print(parsed["var1"])

data2 = {"name":"jeevan","age":20,"college":"jssate","bool":False,"None":None}  # in JS false starts with small letter
x = json.dumps(data2) # Converts python object into json string
print(x)

y = json.dumps(data2,indent=4,separators=(". "," = "))  # default (", ",": ")
print(y)


#sort_keys : Its a parameter ,if True is given then the data gets sorted, (first caps and then small)

z = json.dumps(data2,indent=4,sort_keys=True)
print(z)