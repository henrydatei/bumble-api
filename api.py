from classes.chat import Chat
from classes.message import Message
from classes.user import User
from classes.photo import Photo
from classes.location import Location
import requests
import hashlib
from requests.structures import CaseInsensitiveDict
import time

class BumbleAPI:
    session = None
    myID = None

    def __init__(self, session):
        self.session = session
        self.myID = self.getMyUserID()

    def __signRequest(self, body):
        # idea from https://www.joyk.com/dig/detail/1629959520338869
        # https://web.archive.org/web/20211107103928/https://www.joyk.com/dig/detail/1629959520338869
        # see also https://github.com/NDrong/bumble_request_signer
        string = body + "whitetelevisionbulbelectionroofhorseflying"
        result = hashlib.md5(string.encode())
        return result.hexdigest()

    def getMyUserID(self):
        url = "https://bumble.com/mwebapi.phtml?SERVER_APP_STARTUP"

        data = '{"$gpb":"badoo.bma.BadooMessage","body":[{"message_type":2,"server_app_startup":{"app_build":"MoxieWebapp","app_name":"moxie","app_version":"1.0.0","can_send_sms":false,"user_agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0","screen_width":1680,"screen_height":1050,"language":0,"is_cold_start":true,"external_provider_redirect_url":"https://bumble.com/static/external-auth-result.html?","locale":"en-us","system_locale":"de","app_platform_type":5,"app_product_type":400,"device_info":{"webcam_available":false,"form_factor":3},"build_configuration":2,"build_fingerprint":"25621","supported_features":[141,145,11,15,1,2,13,46,4,248,6,18,155,70,160,140,130,189,187,220,223,180,197,161,232,29,227,237,239,254,190,290,291,296,250,264,294,295,310,148,262],"supported_minor_features":[472,317,2,216,244,232,19,130,225,246,31,125,183,114,254,8,9,83,41,427,115,288,420,477,93,226,413,267,39,290,398,453,180,281,40,455,280,499,471,397,411,352,447,146,469,118,63,391,523,293,431,620,574,405,547,451,571,319,297,558,394,593,628,603,602,537,305,561,324,554,505,696,576,707,726,309,329,307,553],"supported_notifications":[83,73,3,72,49,46,109,81,44,96,89],"supported_payment_providers":[26,100,35,100001],"supported_promo_blocks":[{"context":92,"position":13,"types":[71]},{"context":45,"position":21,"types":[148]},{"context":89,"position":5,"types":[160,358]},{"context":8,"position":13,"types":[111,112,113]},{"context":53,"position":18,"types":[136,93,12]},{"context":45,"position":18,"types":[327]},{"context":45,"position":15,"types":[410,93,134,135,136,137,327,308,309,334,187,61,422,423]},{"context":10,"position":1,"types":[265,266,286]},{"context":148,"position":21,"types":[179,180,283]},{"context":26,"position":13,"types":[354]},{"context":26,"position":4,"types":[355,356]},{"context":26,"position":1,"types":[354]},{"context":26,"position":18,"types":[357]},{"context":130,"position":13,"types":[268,267]},{"context":113,"position":1,"types":[228]},{"context":3,"position":1,"types":[80,423]},{"context":3,"position":4,"types":[80,228,423]},{"context":119,"position":1,"types":[80,282,81,90,422]},{"context":43,"position":1,"types":[96,307]},{"context":43,"position":18,"types":[369]},{"context":119,"position":18,"types":[369]},{"context":10,"position":18,"types":[358,174]},{"context":10,"position":8,"types":[358]},{"context":26,"position":16,"types":[286,371]},{"context":10,"position":6,"types":[286,373,372]},{"context":246,"position":13,"types":[404]}],"supported_user_substitutes":[{"context":1,"types":[3]}],"supported_onboarding_types":[9],"user_field_filter_client_login_success":{"projection":[210,220,230,200,91,890,340,10,11,231,71,93,100]},"a_b_testing_settings":{"tests":[{"test_id":"bumble__gifs_with_old_input"}]},"dev_features":["bumble_bizz","bumble_snooze","bumble_questions","bumble__pledge","bumble__request_photo_verification","bumble_moves_making_impact_","bumble__photo_verification_filters","bumble_gift_cards","bumble__antighosting_xp_dead_chat_followup","bumble_private_detector","bumble_distance_expansion","bumble_live_in_the_hive"],"device_id":"a73a8108-8108-08be-be64-6445e1892362","supported_screens":[{"type":23,"version":4},{"type":26,"version":0},{"type":13,"version":0},{"type":14,"version":0},{"type":15,"version":0},{"type":16,"version":0},{"type":18,"version":0},{"type":19,"version":0},{"type":20,"version":0},{"type":21,"version":0},{"type":25,"version":0},{"type":27,"version":0},{"type":28,"version":0},{"type":57,"version":0},{"type":29,"version":1},{"type":69,"version":0},{"type":92,"version":0}],"supported_landings":[{"source":25,"params":[20,3],"search_settings_types":[3]}],"app_domain":"com.bumble"}}],"message_id":1,"message_type":2,"version":1,"is_background":false}'

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0"
        headers["Accept"] = "*/*"
        headers["Accept-Language"] = "de,en-US;q=0.7,en;q=0.3"
        headers["Referer"] = "https://bumble.com/get-started"
        headers["Content-Type"] = "application/json"
        headers["X-Pingback"] = self.__signRequest(data)
        headers["X-Message-type"] = "2"
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
        return resp.headers["X-User-id"]

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
        return User().userFromJSON(json)

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
            c.addMessage(Message().messageFromJSON(message))

        return c

    def sendMessage(self, toID, message, messageID = 2147483647):
        url = "https://bumble.com/mwebapi.phtml?SERVER_SEND_CHAT_MESSAGE"

        data = '{"$gpb":"badoo.bma.BadooMessage","body":[{"message_type":104,"chat_message":{"mssg":"' + message.replace(" ", "_") + '","message_type":1,"uid":"' + str(int(time.time() * 1000)) + '","from_person_id":"' + self.myID + '","to_person_id":"' + toID +'","read":false}}],"message_id":' + str(messageID) + ',"message_type":104,"version":1,"is_background":false}'

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0"
        headers["Accept"] = "*/*"
        headers["Accept-Language"] = "de,en-US;q=0.7,en;q=0.3"
        headers["Referer"] = "https://bumble.com/app/connections"
        headers["Content-Type"] = "application/json"
        headers["X-Pingback"] = self.__signRequest(data)
        headers["X-Message-type"] = "104"
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
        return resp.json()

    def getMatchQueue(self, numberUsers = 10): # max is 20 users in match queue
        matchqueue = []

        url = "https://bumble.com/mwebapi.phtml?SERVER_GET_ENCOUNTERS"

        data = '{"$gpb":"badoo.bma.BadooMessage","body":[{"message_type":81,"server_get_encounters":{"number":' + str(numberUsers) + ',"context":1,"user_field_filter":{"projection":[210,370,200,230,490,540,530,560,291,732,890,930,662,570,380,493,1140,1150,1160,1161],"request_albums":[{"album_type":7},{"album_type":12,"external_provider":12,"count":8}],"game_mode":0,"request_music_services":{"top_artists_limit":8,"supported_services":[29],"preview_image_size":{"width":120,"height":120}}}}}],"message_id":7,"message_type":81,"version":1,"is_background":false}'

        headers = CaseInsensitiveDict()
        headers["Connection"] = "keep-alive"
        headers["X-Pingback"] = self.__signRequest(data)
        headers["X-Message-type"] = "81"
        headers["sec-ch-ua-mobile"] = "?0"
        headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        headers["x-use-session-cookie"] = "1"
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "*/*"
        headers["Origin"] = "https://bumble.com"
        headers["Sec-Fetch-Site"] = "same-origin"
        headers["Sec-Fetch-Mode"] = "cors"
        headers["Sec-Fetch-Dest"] = "empty"
        headers["Referer"] = "https://bumble.com/app"
        headers["Accept-Language"] = "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
        headers["Cookie"] = "session=" + self.session + "; session_cookie_name=session"

        resp = requests.post(url, headers=headers, data=data)

        for user in resp.json()["body"][0]["client_encounters"]["results"]:
            u = User().userFromJSON(user["user"])
            matchqueue.append(u)

        return matchqueue

    def voteUser(self, userID, vote):
        url = "https://bumble.com/mwebapi.phtml?SERVER_ENCOUNTERS_VOTE"

        data = '{"$gpb":"badoo.bma.BadooMessage","body":[{"message_type":80,"server_encounters_vote":{"person_id":"' + userID + '","vote":' + str(vote) + ',"vote_source":1,"game_mode":0}}],"message_id":13,"message_type":80,"version":1,"is_background":false}'

        headers = CaseInsensitiveDict()
        headers["Connection"] = "keep-alive"
        headers["X-Pingback"] = self.__signRequest(data)
        headers["X-Message-type"] = "80"
        headers["sec-ch-ua-mobile"] = "?0"
        headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        headers["x-use-session-cookie"] = "1"
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "*/*"
        headers["Origin"] = "https://bumble.com"
        headers["Sec-Fetch-Site"] = "same-origin"
        headers["Sec-Fetch-Mode"] = "cors"
        headers["Sec-Fetch-Dest"] = "empty"
        headers["Referer"] = "https://bumble.com/app"
        headers["Accept-Language"] = "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
        headers["Cookie"] = "session=" + self.session + "; session_cookie_name=session"

        resp = requests.post(url, headers=headers, data=data)
        return resp

    def dislikeUser(self, userID):
        self.voteUser(userID, 3)

    def likeUser(self, userID):
        self.voteUser(userID, 2)