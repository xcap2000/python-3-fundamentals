import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
print(json)

print("The people currently in space are:")
for person in json['people']:
    # print(person)
     print(person['name'])

# Sample result:
# Jasmin Moghbeli
# Andreas Mogensen
# Satoshi Furukawa
# Konstantin Borisov
# Oleg Kononenko
# Nikolai Chub
# Loral O'Hara