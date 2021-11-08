from api import BumbleAPI

session = ""

api = BumbleAPI(session)
for photo in api.getUser("zAhMACTc0NzA1NzY2NgjGPf5jAAAAACCUM4f3jmPyWNFLwU30cacn8dH_P4WgbdkzUftws9iF9w").photos:
    print(photo.largeURL)

api.getChat("zAhMACTc0NzA1NzY2NgjGPf5jAAAAACCUM4f3jmPyWNFLwU30cacn8dH_P4WgbdkzUftws9iF9w").printChat()