import requests as req
import colorama; from colorama import *
colorama.init()

class Main:	

	url = 'https://ipinfo.io/json'

	def __init__(self):
			self.response = req.get(Main.url)
			self.ip = self.response.json()['ip']
			self.city = self.response.json()['city']
			self.region = self.response.json()['region']
			self.country = self.response.json()['country']
			self.loc = self.response.json()['loc']
			self.org = self.response.json()['org']
			self.timezone = self.response.json()['timezone']

	def display(self):
		print (f'{Fore.LIGHTBLUE_EX}IP : {Fore.LIGHTRED_EX}{self.ip}')
		print (f'{Fore.LIGHTBLUE_EX}city : {Fore.LIGHTRED_EX}{self.city}')
		print (f'{Fore.LIGHTBLUE_EX}region : {Fore.LIGHTRED_EX}{self.region}')
		print (f'{Fore.LIGHTBLUE_EX}country : {Fore.LIGHTRED_EX}{self.country}')
		print (f'{Fore.LIGHTBLUE_EX}loc : {Fore.LIGHTRED_EX}{self.loc}')
		print (f'{Fore.LIGHTBLUE_EX}org : {Fore.LIGHTRED_EX}{self.org}')
		print (f'{Fore.LIGHTBLUE_EX}timezone : {Fore.LIGHTRED_EX}{self.timezone}')

try:

	op1 = Main().display()

except:

	print (f'{Fore.LIGHTRED_EX}There is a error, Please check your network connection...')