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

    def __init__(self, id, dateModified, fromID, toID, text, offensive, dateCreated, isLiked, emojisCount, hasEmojiCharactersOnly, isEdited, isReported, isLikelyOffensive) -> None:
        self.id = id
        self.dateModified = datetime.fromtimestamp(dateModified)
        self.fromID = fromID
        self.toID = toID
        self.text = text
        self.offensive = offensive
        self.dateCreated = datetime.fromtimestamp(dateCreated)
        self.isLiked = isLiked
        self.emojisCount = emojisCount
        self.hasEmojiCharactersOnly = hasEmojiCharactersOnly
        self.isEdited = isEdited
        self.isReported = isReported
        self.isLikelyOffensive = isLikelyOffensive