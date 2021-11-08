from datetime import datetime

class Chat:
    dateModified = None
    isNew = None
    feelsLikeChatting = None
    myUnreadMessages = None
    theirUnreadMessages = None
    isMatch = None
    messages = []
    user = None

    def __init__(self, dateModified, isNew, feelsLikeChatting, myUnreadMessages, theirUnreadMessages, isMatch, user):
        self.dateModified = datetime.fromtimestamp(dateModified)
        self.isNew = isNew
        self.feelsLikeChatting = feelsLikeChatting
        self.myUnreadMessages = myUnreadMessages
        self.theirUnreadMessages = theirUnreadMessages
        self.isMatch = isMatch
        self.user = user

    def addMessage(self, message):
        self.messages.append(message)

    def printChat(self):
        print("=== Chat with " + self.user.name + " ===")
        for message in self.messages:
            if self.user.id == message.fromID:
                print(self.user.name + ": " + message.text)
            else:
                print("Me: " + message.text)