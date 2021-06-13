import pickle

class UserData:
	def __init__(self):
		self.name = 'None'
		self.gender = 'None'
		self.userphoto = 0

	def extractData(self):
		with open('userData/userData.pck', 'rb') as file:
			details = pickle.load(file)
			self.name, self.gender, self.userphoto = details['name'], details['gender'], details['userphoto']

	def updateData(self, name, gender, userphoto):
		with open('userData/userData.pck', 'wb') as file:
			details = {'name': name, 'gender': gender, 'userphoto': userphoto}
			pickle.dump(details, file)

	def getName(self):
		return self.name

	def getGender(self):
		return self.gender

	def getUserPhoto(self):
		return self.userphoto

def UpdateUserPhoto(avatar):
	u = UserData()
	u.extractData()
	u.updateData(u.getName(), u.getGender(), avatar)
