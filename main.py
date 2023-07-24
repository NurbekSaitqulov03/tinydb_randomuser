from tinydb import TinyDB
from api import r
db = TinyDB('data.json', indent=4)

if r.status_code == 200:
    user = r.json()

    for i in user['results']:
        db.insert({
            "first_name":i["name"]['first'],
            "last_name": i['name']['last'],
            "age": i['dob']['age'],
        })

