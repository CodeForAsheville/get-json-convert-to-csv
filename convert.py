import json
import unicodecsv as csv
import urllib

url = "https://www.publicstuff.com/api/2.0/requests_list?return_type=json&limit=100&lat=35.62336&request_type_id=11339&lon=-82.561531&nearby=250&api_key=58j013k159vpqz87xd85df0uy7epvl"
response = urllib.urlopen(url);
data = json.loads(response.read())


def main(data):
	rowkey="request"
	rowkey=rowkey.upper()
	rowData='start'
	print rowData		
	doHeaders = True

	def walkDict(d):
		
		for k,v in d.items():
			if checkrowkey(k):
				print v.keys()
				print v.values()
				print ''
				
			#if not(isinstance(v,dict)) and not(isinstance(v,list)):
			#	#rowData = rowData + k + '=' + str(v) +','
			#	if type(v) == unicode:
			##	v = str(v)
			#	
	 		#	#print k,v,type(v)
			if isinstance(v,dict):
				walkDict(v)
			if isinstance(v,list):
				walkList(v)
	print''
	
	
	def walkList(d):
		for v in d:
			
			if isinstance(v,dict):
				walkDict(v)
			if isinstance(v,list):
				walkList(v)
				
	def checkrowkey(k):
		
		if str(k).upper()==rowkey:
			#if type(v) == unicode:
			#	v = v.encode('UTF-8')
			# = str(v)
			#print v
			return True
		else:
			return False

	walkDict(data)
		

main(data)
