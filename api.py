from classes.chat import Chat
from classes.message import Message
from classes.user import User
from classes.photo import Photo
from classes.location import Location
import requests
import hashlib
from requests.structures import CaseInsensitiveDict

class BumbleAPI:
    session = None

    def __init__(self, session):
        self.session = session

    def __signRequest(self, body):
        # idea from https://www.joyk.com/dig/detail/1629959520338869
        # https://web.archive.org/web/20211107103928/https://www.joyk.com/dig/detail/1629959520338869
        # see also https://github.com/NDrong/bumble_request_signer
        body = body.replace("True", "true").replace("False", "false").replace(" ", "").replace("\'", "\"")
        string = body + "whitetelevisionbulbelectionroofhorseflying"
        result = hashlib.md5(string.encode())
        return result.hexdigest()

    def __getValueOfProfileField(self, data, needle):
        for field in data:
            if field["id"] == needle:
                return field["display_value"]
        return None

    def getUser(self, userID):
        url = "https://bumble.com/mwebapi.phtml?SERVER_GET_USER"

        data = '{"$gpb":"badoo.bma.BadooMessage","body":[{"message_type":403,"server_get_user":{"user_id":"' + userID + '","user_field_filter":{"game_mode":0,"projection":[200,340,230,310,370,762,890,493,530,540,291,490,1160,1161,210,380],"request_music_services":{"top_artists_limit":10,"supported_services":[29]},"request_albums":[{"person_id":"' + userID + '","album_type":2,"offset":1},{"person_id":"' + userID + '","album_type":12,"external_provider":12}]},"client_source":10}}],"message_id":44,"message_type":403,"version":1,"is_background":false}'

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0"
        headers["Accept"] = "*/*"
        headers["Accept-Language"] = "de,en-US;q=0.7,en;q=0.3"
        headers["Referer"] = "https://bumble.com/app/connections"
        headers["Content-Type"] = "application/json"
        headers["X-Pingback"] = self.__signRequest(data)
        headers["X-Message-type"] = "403"
        headers["x-use-session-cookie"] = "1"
        headers["Origin"] = "https://bumble.com"
        headers["DNT"] = "1"
        headers["Connection"] = "keep-alive"
        headers["Cookie"] = "session=" + self.session + "; session_cookie_name=session"
        headers["Sec-Fetch-Dest"] = "empty"
        headers["Sec-Fetch-Mode"] = "cors"
        headers["Sec-Fetch-Site"] = "same-origin"
        headers["Pragma"] = "no-cache"
        headers["Cache-Control"] = "no-cache"

        resp = requests.post(url, headers=headers, data=data)
        json = resp.json()["body"][0]["user"]

        try:
            photo = Photo(json["profile_photo"]["id"], json["profile_photo"]["preview_url"], json["profile_photo"]["large_url"])
        except:
            photo = None
        work = self.__getValueOfProfileField(json["profile_fields"], "work")
        aboutMe = self.__getValueOfProfileField(json["profile_fields"], "aboutme_text")
        height = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_height")
        exercise = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_exercise")
        zodiacSign = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_zodiak")
        education = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_education")
        drinking = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_drinking")
        smoking = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_smoking")
        datingIntensions = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_dating_intensions")
        familyPlans = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_family_plans")
        religion = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_religion")
        politics = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_politics")
        try:
            hometown = Location(json["hometown"]["country"]["name"], json["hometown"]["region"]["name"], json["hometown"]["city"]["name"])
        except:
            hometown = None
        try:
            residence = Location(json["residence"]["country"]["name"], json["residence"]["region"]["name"], json["residence"]["city"]["name"])
        except:
            residence = None
        try:
            id = json["user_id"]
        except:
            id = None
        try:
            name = json["name"]
        except:
            name = None
        try:
            age = json["age"]
        except:
            age = None
        try:
            gender = json["gender"]
        except:
            gender = None
        try:
            verfication = json["verification_status"]
        except:
            verfication = None
        try:
            summary = json["profile_summary"]["primary_text"]
        except:
            summary = None
        u = User(id, name, age, gender, verfication, photo, work, aboutMe, height, exercise, zodiacSign, education, drinking, smoking, datingIntensions, familyPlans, religion, politics, summary, hometown, residence)

        for album in json["albums"]:
            # test if album is blocked
            try:
                album["photos"]
            except:
                continue
            for photo in album["photos"]:
                p = Photo(photo["id"], photo["preview_url"], photo["large_url"])
                u.addPhoto(p)
        return u

    def getChat(self, userID):
        url = "https://bumble.com/mwebapi.phtml?SERVER_OPEN_CHAT"

        data = '{"$gpb":"badoo.bma.BadooMessage","body":[{"message_type":102,"server_open_chat":{"user_field_filter":{"projection":[200,210,340,230,640,580,300,860,280,590,591,250,700,762,592,880,582,930,585,583,305,330,763,1423,584,1262,911,912],"request_albums":[{"count":10,"offset":1,"album_type":2,"photo_request":{"return_preview_url":true,"return_large_url":true}}]},"chat_instance_id":"' + userID + '","message_count":50}}],"message_id":30,"message_type":102,"version":1,"is_background":false}'

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
        headers["Accept"] = "*/*"
        headers["Accept-Language"] = "de,en-US;q=0.7,en;q=0.3"
        headers["Referer"] = "https://bumble.com/app/connections"
        headers["Content-Type"] = "application/json"
        headers["X-Pingback"] = self.__signRequest(data)
        headers["X-Message-type"] = "102"
        headers["x-use-session-cookie"] = "1"
        headers["Origin"] = "https://bumble.com"
        headers["DNT"] = "1"
        headers["Connection"] = "keep-alive"
        headers["Cookie"] = "session=" + self.session + "; session_cookie_name=session"
        headers["Sec-Fetch-Dest"] = "empty"
        headers["Sec-Fetch-Mode"] = "cors"
        headers["Sec-Fetch-Site"] = "same-origin"
        headers["Pragma"] = "no-cache"
        headers["Cache-Control"] = "no-cache"

        resp = requests.post(url, headers=headers, data=data)
        json = resp.json()["body"][0]["client_open_chat"]

        c = Chat(json["chat_instance"]["date_modified"], json["chat_instance"]["is_new"], json["chat_instance"]["feels_like_chatting"], json["chat_instance"]["my_unread_messages"], json["chat_instance"]["their_unread_messages"], json["chat_instance"]["is_match"], self.getUser(userID))

        for message in json["chat_messages"]:
            m = Message(message["uid"], message["date_modified"], message["from_person_id"], message["to_person_id"], message["mssg"], message["offensive"], message["date_created"], message["is_liked"], message["emojis_count"], message["has_emoji_characters_only"], message["is_edited"], message["is_reported"], message["is_likely_offensive"])
            c.addMessage(m)

        return c