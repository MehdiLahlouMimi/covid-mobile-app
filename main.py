"""
test mobile app
author : @Crun (god)
"""

#importement : 
from kivy.app import App
from kivy.uix.label import Label
import requests
 
#vars : 
strApiUrl = "https://api.covid19api.com/summary"

#functions : 
def seek() : 
	dictJsonContent = requests.get(strApiUrl).json()    
	#finding Morocco : 
	for country in dictJsonContent["Countries"] :
		if country["CountryCode"] == "MA" : 
			maroc = country

	else : pass

	#returning the data : 
	return [maroc["NewConfirmed"], maroc["NewDeaths"], maroc["NewRecovered"]]   


	#classes : 
class mainApp(App): 
	"""
	A subclass of the pre-built App entity of kivy, IMPORTANT 		
	"""

	def build(self) : 

		label0 = Label(text = str(seek()[0]), pos_hint = {"center_x" : 0.5 , "center_y" : 0.5})
		return label0
		print("premier label")

		"""label1 = Label(text = str(seek()[1]), pos_hint = {"center_x" : 0.5 , "center_y" : 0.1})
								return label1
								print("deuxieme label")
						
								label2 = Label(text = str(seek()[2]), pos_hint = {"center_x" : 0.5 , "center_y" : 0.2})
								return label2
								print("troisieme label")"""


#program 
if __name__ == '__main__' : 
	app = mainApp()
	app.run()
