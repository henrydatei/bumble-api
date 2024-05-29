from api import BumbleAPI

session = ""

api = BumbleAPI(session)
for searchResult in api.getMatchQueue():
    print(searchResult.user.name)