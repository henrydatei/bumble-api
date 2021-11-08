import requests
import hashlib
from requests.structures import CaseInsensitiveDict

session = ""

def signRequest(body):
    # idea from https://www.joyk.com/dig/detail/1629959520338869
    # https://web.archive.org/web/20211107103928/https://www.joyk.com/dig/detail/1629959520338869
    # see also https://github.com/NDrong/bumble_request_signer
    body = body.replace("True", "true").replace("False", "false").replace(" ", "").replace("\'", "\"")
    string = body + "whitetelevisionbulbelectionroofhorseflying"
    result = hashlib.md5(string.encode())
    return result.hexdigest()

def getChat(userID):
    url = "https://bumble.com/mwebapi.phtml?SERVER_OPEN_CHAT"

    data = '{"$gpb":"badoo.bma.BadooMessage","body":[{"message_type":102,"server_open_chat":{"user_field_filter":{"projection":[200,210,340,230,640,580,300,860,280,590,591,250,700,762,592,880,582,930,585,583,305,330,763,1423,584,1262,911,912],"request_albums":[{"count":10,"offset":1,"album_type":2,"photo_request":{"return_preview_url":true,"return_large_url":true}}]},"chat_instance_id":"' + userID + '","message_count":50}}],"message_id":30,"message_type":102,"version":1,"is_background":false}'

    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
    headers["Accept"] = "*/*"
    headers["Accept-Language"] = "de,en-US;q=0.7,en;q=0.3"
    headers["Referer"] = "https://bumble.com/app/connections"
    headers["Content-Type"] = "application/json"
    headers["X-Pingback"] = signRequest(data)
    headers["X-Message-type"] = "102"
    headers["x-use-session-cookie"] = "1"
    headers["Origin"] = "https://bumble.com"
    headers["DNT"] = "1"
    headers["Connection"] = "keep-alive"
    headers["Cookie"] = "session=" + session + "; session_cookie_name=session"
    headers["Sec-Fetch-Dest"] = "empty"
    headers["Sec-Fetch-Mode"] = "cors"
    headers["Sec-Fetch-Site"] = "same-origin"
    headers["Pragma"] = "no-cache"
    headers["Cache-Control"] = "no-cache"

    resp = requests.post(url, headers=headers, data=data)
    return resp.json()

def getUser(userID):
    url = "https://bumble.com/mwebapi.phtml?SERVER_GET_USER"

    data = '{"$gpb":"badoo.bma.BadooMessage","body":[{"message_type":403,"server_get_user":{"user_id":"' + userID + '","user_field_filter":{"game_mode":0,"projection":[200,340,230,310,370,762,890,493,530,540,291,490,1160,1161,210,380],"request_music_services":{"top_artists_limit":10,"supported_services":[29]},"request_albums":[{"person_id":"' + userID + '","album_type":2,"offset":1},{"person_id":"' + userID + '","album_type":12,"external_provider":12}]},"client_source":10}}],"message_id":44,"message_type":403,"version":1,"is_background":false}'

    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0"
    headers["Accept"] = "*/*"
    headers["Accept-Language"] = "de,en-US;q=0.7,en;q=0.3"
    headers["Referer"] = "https://bumble.com/app/connections"
    headers["Content-Type"] = "application/json"
    headers["X-Pingback"] = signRequest(data)
    headers["X-Message-type"] = "403"
    headers["x-use-session-cookie"] = "1"
    headers["Origin"] = "https://bumble.com"
    headers["DNT"] = "1"
    headers["Connection"] = "keep-alive"
    headers["Cookie"] = "session=" + session + "; session_cookie_name=session"
    headers["Sec-Fetch-Dest"] = "empty"
    headers["Sec-Fetch-Mode"] = "cors"
    headers["Sec-Fetch-Site"] = "same-origin"
    headers["Pragma"] = "no-cache"
    headers["Cache-Control"] = "no-cache"

    resp = requests.post(url, headers=headers, data=data)
    return resp.json()

print(getUser("zAhMACTg4NzAzNTcwOAjGPf5jAAAAACD5bENu8vZ48tyUC7ILKIx2hfigJfFhDDH6pb8duItL2Q"))