from datetime import datetime

class Message:
    id = None
    dateModified = None
    fromID = None
    toID = None
    text = None
    offensive = None
    dateCreated = None
    isLiked = None
    emojisCount = None
    hasEmojiCharactersOnly = None
    isEdited = None
    isReported = None
    isLikelyOffensive = None

    def __init__(self, id = None, dateModified = None, fromID = None, toID = None, text = None, offensive = None, dateCreated = None, isLiked = None, emojisCount = None, hasEmojiCharactersOnly = None, isEdited = None, isReported = None, isLikelyOffensive = None) -> None:
        self.id = id
        if dateModified == None:
            self.dateModified = None
        else:
            self.dateModified = datetime.fromtimestamp(dateModified)
        self.fromID = fromID
        self.toID = toID
        self.text = text
        self.offensive = offensive
        if dateCreated == None:
            self.dateCreated = None
        else:
            self.dateCreated = datetime.fromtimestamp(dateCreated)
        self.isLiked = isLiked
        self.emojisCount = emojisCount
        self.hasEmojiCharactersOnly = hasEmojiCharactersOnly
        self.isEdited = isEdited
        self.isReported = isReported
        self.isLikelyOffensive = isLikelyOffensive

    def messageFromJSON(self, message):
        m = Message(message["uid"], message["date_modified"], message["from_person_id"], message["to_person_id"], message["mssg"], message["offensive"], message["date_created"], message["is_liked"], message["emojis_count"], message["has_emoji_characters_only"], message["is_edited"], message["is_reported"], message["is_likely_offensive"])
        return m