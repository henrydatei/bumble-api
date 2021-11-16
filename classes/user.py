from .photo import Photo
from .location import Location

class User:
    id = None
    name = None
    age = None
    gender = None
    verificationStatus = None
    profilePhoto = None
    photos = []
    work = None
    aboutMe = None
    height = None
    exercise = None
    zodiacSign = None
    education = None
    drinking = None
    smoking = None
    datingIntensions = None
    familyPlans = None
    religion = None
    politics = None
    profileSummary = None
    hometown = None
    residence = None

    def __init__(self, id = None, name = None, age = None, gender = None, verificationStatus = None, profilePhoto = None, work = None, aboutMe = None, height = None, exercise = None, zodiacSign = None, education = None, drinking = None, smoking = None, datingIntensions = None, familyPlans = None, religion = None, politics = None, profileSummary = None, hometown = None, residence = None):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.verificationStatus = verificationStatus
        self.profilePhoto = profilePhoto
        self.work = work
        self.aboutMe = aboutMe
        self.height = height
        self.exercise = exercise
        self.zodiacSign = zodiacSign
        self.education = education
        self.drinking = drinking
        self.smoking = smoking
        self.datingIntensions = datingIntensions
        self.familyPlans = familyPlans
        self.religion = religion
        self.politics = politics
        self.profileSummary = profileSummary
        self.hometown = hometown
        self.residence = residence

    def __getValueOfProfileField(self, data, needle):
        for field in data:
            if field["id"] == needle:
                return field["display_value"]
        return None

    def userFromJSON(self, json):
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

    def addPhoto(self, photo):
        self.photos.append(photo)

    def printUser(self):
        print(self.name + " (" + self.age + ")")