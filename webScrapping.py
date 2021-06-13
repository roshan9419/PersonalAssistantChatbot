import wikipedia
import webbrowser
import requests
from bs4 import BeautifulSoup
import threading
import smtplib
import urllib.request
import os
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

class COVID:
	def __init__(self):
		self.total = 'Not Available'
		self.deaths = 'Not Available'
		self.recovered = 'Not Available'
		self.totalIndia = 'Not Available'
		self.deathsIndia = 'Not Available'
		self.recoveredIndia = 'Not Available'

	def covidUpdate(self):
		URL = 'https://www.worldometers.info/coronavirus/'
		result = requests.get(URL)
		src = result.content
		soup = BeautifulSoup(src, 'html.parser')

		temp = []
		divs = soup.find_all('div', class_='maincounter-number')
		for div in divs:
			temp.append(div.text.strip())
		self.total, self.deaths, self.recovered = temp[0], temp[1], temp[2]

	def covidUpdateIndia(self):
		URL = 'https://www.worldometers.info/coronavirus/country/india/'
		result = requests.get(URL)
		src = result.content
		soup = BeautifulSoup(src, 'html.parser')

		temp = []
		divs = soup.find_all('div', class_='maincounter-number')
		for div in divs:
			temp.append(div.text.strip())
		self.totalIndia, self.deathsIndia, self.recoveredIndia = temp[0], temp[1], temp[2]

	def totalCases(self,india_bool):
		if india_bool: return self.totalIndia
		return self.total

	def totalDeaths(self,india_bool):
		if india_bool: return self.deathsIndia
		return self.deaths

	def totalRecovery(self,india_bool):
		if india_bool: return self.recoveredIndia
		return self.recovered

	def symptoms(self):
		symt = ['1. Fever',
				'2. Coughing',
				'3. Shortness of breath',
				'4. Trouble breathing',
				'5. Fatigue',
				'6. Chills, sometimes with shaking',
				'7. Body aches',
				'8. Headache',
				'9. Sore throat',
				'10. Loss of smell or taste',
				'11. Nausea',
				'12. Diarrhea']
		return symt

	def prevention(self):
		prevention = ['1. Clean your hands often. Use soap and water, or an alcohol-based hand rub.',
						'2. Maintain a safe distance from anyone who is coughing or sneezing.',
						'3. Wear a mask when physical distancing is not possible.',
						'4. Don’t touch your eyes, nose or mouth.',
						'5. Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.',
						'6. Stay home if you feel unwell.',
						'7. If you have a fever, cough and difficulty breathing, seek medical attention.']
		return prevention

def wikiResult(query):
	query = query.replace('wikipedia','')
	query = query.replace('search','')
	if len(query.split())==0: query = "wikipedia"
	try:
		return wikipedia.summary(query, sentences=2)
	except Exception as e:
		return "Desired Result Not Found"

class WEATHER:
	def __init__(self):
		#Currently in Lucknow, its 26 with Haze
		self.tempValue = ''
		self.city = ''
		self.currCondition = ''
		self.speakResult = ''

	def updateWeather(self):
		res = requests.get("https://ipinfo.io/")
		data = res.json()
		# URL = 'https://weather.com/en-IN/weather/today/l/'+data['loc']
		URL = 'https://weather.com/en-IN/weather/today/'
		result = requests.get(URL)
		src = result.content

		soup = BeautifulSoup(src, 'html.parser')

		city = ""
		for h in soup.find_all('h1'):
			cty = h.text
			cty = cty.replace('Weather','')
			self.city = cty[:cty.find(',')]
			break

		spans = soup.find_all('span')
		for span in spans:
			try:
				if span['data-testid']=="TemperatureValue":
					self.tempValue = span.text[:-1]
					break
			except Exception as e:
				pass

		divs = soup.find_all('div', class_='CurrentConditions--phraseValue--2xXSr')
		for div in divs:
			self.currCondition = div.text
			break

	def weather(self):
		from datetime import datetime
		today = datetime.today().strftime('%A')
		self.speakResult = "Currently in " + self.city + ", its " + self.tempValue + " degree, with a " + self.currCondition 
		return [self.tempValue, self.currCondition, today, self.city, self.speakResult]

c = COVID()
w = WEATHER()

def dataUpdate():
	c.covidUpdate()
	c.covidUpdateIndia()
	w.updateWeather()

##### WEATHER #####
def weather():
	return w.weather()

### COVID ###
def covid(query):
	
	if "india" in query: india_bool = True
	else: india_bool = False

	if "statistic" in query or 'report' in query:
		return ["Here are the statistics...", ["Total cases: " + c.totalCases(india_bool), "Total Recovery: " + c.totalRecovery(india_bool), "Total Deaths: " + c.totalDeaths(india_bool)]]

	elif "symptom" in query:
		return ["Here are the Symptoms...", c.symptoms()]

	elif "prevent" in query or "measure" in query or "precaution" in query:
		return ["Here are the some of preventions from COVID-19:", c.prevention()]
	
	elif "recov" in query:
		return "Total Recovery is: " + c.totalRecovery(india_bool)
	
	elif "death" in query:
		return "Total Deaths are: " + c.totalDeaths(india_bool)
	
	else:
		return "Total Cases are: " + c.totalCases(india_bool)

def latestNews(news=5):
	URL = 'https://indianexpress.com/latest-news/'
	result = requests.get(URL)
	src = result.content

	soup = BeautifulSoup(src, 'html.parser')

	headlineLinks = []
	headlines = []

	divs = soup.find_all('div', {'class':'title'})

	count=0
	for div in divs:
		count += 1
		if count>news:
			break
		a_tag = div.find('a')
		headlineLinks.append(a_tag.attrs['href'])
		headlines.append(a_tag.text)

	return headlines,headlineLinks

def maps(text):
	text = text.replace('maps', '')
	text = text.replace('map', '')
	text = text.replace('google', '')
	openWebsite('https://www.google.com/maps/place/'+text)

def giveDirections(startingPoint, destinationPoint):

	geolocator = Nominatim(user_agent='assistant')
	if 'current' in startingPoint:
		res = requests.get("https://ipinfo.io/")
		data = res.json()
		startinglocation = geolocator.reverse(data['loc'])
	else:
		startinglocation = geolocator.geocode(startingPoint)

	destinationlocation = geolocator.geocode(destinationPoint)
	startingPoint = startinglocation.address.replace(' ', '+')
	destinationPoint = destinationlocation.address.replace(' ', '+')

	openWebsite('https://www.google.co.in/maps/dir/'+startingPoint+'/'+destinationPoint+'/')

	startinglocationCoordinate = (startinglocation.latitude, startinglocation.longitude)
	destinationlocationCoordinate = (destinationlocation.latitude, destinationlocation.longitude)
	total_distance = great_circle(startinglocationCoordinate, destinationlocationCoordinate).km #.mile
	return str(round(total_distance, 2)) + 'KM'

def openWebsite(url='https://www.google.com/'):
	webbrowser.open(url)

def jokes():
	URL = 'https://icanhazdadjoke.com/'
	result = requests.get(URL)
	src = result.content

	soup = BeautifulSoup(src, 'html.parser')

	try:
		p = soup.find('p')
		return p.text
	except Exception as e:
		raise e


def youtube(query):
	from youtube_search import YoutubeSearch
	query = query.replace('play',' ')
	query = query.replace('on youtube',' ')
	query = query.replace('youtube',' ')
	print("Pahuch Gya")
	results = YoutubeSearch(query,max_results=1).to_dict()
	print("Link mil gya")
	webbrowser.open('https://www.youtube.com/watch?v=' + results[0]['id'])
	return "Enjoy Sir..."


def googleSearch(query):
	if 'image' in query:
		query += "&tbm=isch"
	query = query.replace('images','')
	query = query.replace('image','')
	query = query.replace('search','')
	query = query.replace('show','')
	webbrowser.open("https://www.google.com/search?q=" + query)
	return "Here you go..."

def sendWhatsapp(phone_no='',message=''):
	phone_no = '+91' + str(phone_no)
	webbrowser.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+message)
	import time
	from pynput.keyboard import Key, Controller
	time.sleep(10)
	k = Controller()
	k.press(Key.enter)

def email(rec_email=None, text="Hello, It's F.R.I.D.A.Y. here...", sub='F.R.I.D.A.Y.'):
	if '@gmail.com' not in rec_email: return
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login("senderEmail", "senderPassword") # eg, abc@gmail.com (email) and ****(pass)
	message = 'Subject: {}\n\n{}'.format(sub, text)
	s.sendmail("senderEmail", rec_email, message)
	print("Sent")
	s.quit()


def downloadImage(query, n=4):
	query = query.replace('images','')
	query = query.replace('image','')
	query = query.replace('search','')
	query = query.replace('show','')
	URL = "https://www.google.com/search?tbm=isch&q=" + query
	result = requests.get(URL)
	src = result.content

	soup = BeautifulSoup(src, 'html.parser')
	imgTags = soup.find_all('img', class_='t0fcAb')

	if os.path.exists('Downloads')==False:
		os.mkdir('Downloads')

	count=0
	for i in imgTags:
		if count==n: break
		try:
			urllib.request.urlretrieve(i['src'], 'Downloads/' + str(count) + '.jpg')
			count+=1
			print('Downloaded', count)
		except Exception as e:
			raise e
