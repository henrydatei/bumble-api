from requests.sessions import extract_cookies_to_jar
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
        try:
            work = self.__getValueOfProfileField(json["profile_fields"], "work")
        except:
            work = None
        try:
            aboutMe = self.__getValueOfProfileField(json["profile_fields"], "aboutme_text")
        except:
            aboutMe = None
        try:
            height = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_height")
        except:
            height = None
        try:
            exercise = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_exercise")
        except:
            exercise = None
        try:
            zodiacSign = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_zodiak")
        except:
            zodiacSign = None
        try:
            education = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_education")
        except:
            education = None
        try:
            drinking = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_drinking")
        except:
            drinking = None
        try:
            smoking = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_smoking")
        except:
            smoking = None
        try:
            datingIntensions = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_dating_intensions")
        except:
            datingIntensions = None
        try:
            familyPlans = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_family_plans")
        except:
            familyPlans = None
        try:
            religion = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_religion")
        except:
            religion = None
        try:
            politics = self.__getValueOfProfileField(json["profile_fields"], "lifestyle_politics")
        except:
            politics = None
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

        try:
            for album in json["albums"]:
            # test if album is blocked
                try:
                    album["photos"]
                except:
                    continue
                for photo in album["photos"]:
                    p = Photo(photo["id"], photo["preview_url"], photo["large_url"])
                    u.addPhoto(p)
        except:
            pass
        return u


    def addPhoto(self, photo):
        self.photos.append(photo)

    def printUser(self):
        print(self.name + " (" + str(self.age) + ")")

    def toCSV(self, separator = ";"):
        #csv = ""
        #for att in [o for o in dir(self) if not o.startswith("_")]:
        #    if not (isinstance(getattr(self, att), list) or hasattr(getattr(self, att), '__call__')):
        #        if isinstance(getattr(self, att), Photo) or isinstance(getattr(self, att), Location):
        #            csv = csv + separator + getattr(self, att).toCSV(separator = separator)
        #        else:
        #            csv = csv + separator + str(getattr(self,att)).replace("\n", " ").replace("None", "")
        #return csv[1:]
        csv = str(self.id) + separator + str(self.name) + separator + str(self.age) + separator + str(self.gender) + separator + str(self.verificationStatus) + separator + str(self.work) + separator + str(self.aboutMe).replace("\n", " ").replace(";", ",") + separator + str(self.height).split(" ")[0] + separator + str(self.exercise) + separator + str(self.zodiacSign) + separator + str(self.education) + separator + str(self.drinking) + separator + str(self.smoking) + separator + str(self.datingIntensions) + separator + str(self.familyPlans) + separator + str(self.religion) + separator + str(self.politics) + separator + str(self.profileSummary)
        if not self.hometown is None:
            csv = csv + separator + str(self.hometown.country) + separator + str(self.hometown.region) + separator + str(self.hometown.city)
        else:
            csv = csv + separator + separator + separator
        if not self.residence is None:
            csv = csv + separator + str(self.residence.country) + separator + str(self.residence.region) + separator + str(self.residence.city)
        else:
            csv = csv + separator + separator + separator
        if not self.profilePhoto is None:
            csv = csv + separator + str(self.profilePhoto.largeURL)
        else:
            csv = csv + separator
        return csv.replace("None", "")

    def CSVHeader(self):
        return "id;name;age;gender;verificationStatus;work;aboutMe;height;exercise;zodiacSign;education;drinking;smoking;datingIntensions;familyPlans;religion;politics;profileSummary;hometown.country;hometown.region;hometown.city;residence.country;residence.region;residence.city;profilePhoto.largeURL"