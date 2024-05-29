# bumble-api
Reverse engineering the API of bumble.com

# Usage
- Clone the repository
- Create a file in the repository
- Run the following code in the file
```python
from api import BumbleAPI

session = ""

api = BumbleAPI(session)
for searchResult in api.getMatchQueue():
    print(searchResult.user.name)
```