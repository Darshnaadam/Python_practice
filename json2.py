import json

input = '''
[
    {
        "id" : "001",
        "x" : "2",
        "name" : "Darshna"
    },
    {
        "id" : "007",
        "x" : "7",
        "name" : "Rahul"
    }
]
'''

info = json.loads(input)
print('user count:', len(info))

for item in info:
    print('Name:', item['name'])
    print("Id:" , item["id"])
    print("Attribute:", item["x"])