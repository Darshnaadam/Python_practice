import json

data = '''
{
    "name" : "Darshna",
    "phone" : {
        "type" : "intl",
        "number" : "+1 34 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}
'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
print('Phone:', info["phone"])