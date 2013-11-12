import json
import unicodecsv as csv
import urllib

url = "https://www.publicstuff.com/api/2.0/requests_list?return_type=json&limit=100&lat=35.62336&request_type_id=11339&lon=-82.561531&nearby=250&api_key=58j013k159vpqz87xd85df0uy7epvl"
response = urllib.urlopen(url);
data = json.loads(response.read())

def walkDict(d):

	for k,v in d.items():
		if not(isinstance(v,dict)) and not(isinstance(v,list)):
			print k,v
		if isinstance(v,dict):
			walkDict(v)
		if isinstance(v,list):
			walkList(v)

def walkList(d):
	for v in d:
		
		if isinstance(v,dict):
			walkDict(v)
		if isinstance(v,list):
			walkList(v)
			

walkDict(data)

