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

    def __init__(self, id, name, age, gender, verificationStatus, profilePhoto, work, aboutMe, height, exercise, zodiacSign, education, drinking, smoking, datingIntensions, familyPlans, religion, politics, profileSummary, hometown, residence):
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

    def addPhoto(self, photo):
        self.photos.append(photo)

    def printUser(self):
        print(self.name + " (" + self.age + ")")