class Photo:
    id = None
    previewURL = None
    largeURL = None

    def __init__(self, id, previewURL, largeURL):
        self.id = id
        self.previewURL = "https:" + str(previewURL)
        self.largeURL = "https:" + str(largeURL)

    def printPhoto(self):
        print(self.largeURL)