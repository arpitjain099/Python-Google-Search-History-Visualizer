import json
from pprint import pprint
import glob
import datetime
import codecs
import urllib
fi=codecs.open("Result.html","w",encoding='utf-8')
message = """<html>
<head></head>
<body>"""
fi.write(message)
fi.write('<table style="width:100%">')
a= sorted(glob.glob("Searches/*.json"))
#fi.write("<tr><td width='15%'>Timestamp</td><td>Query</td></tr>\n")
for i in a:
	
	with open(i) as data_file:    
		data = json.load(data_file)
		for k in range(len(data["event"])):
			try:
				 

			
				fi.write ("<tr><td width='15%'>"+(datetime.datetime.fromtimestamp(int(data["event"][k]['query']['id'][0]['timestamp_usec'])/1000000).strftime('%Y-%m-%d %H:%M:%S'))+"</td><td>"+"</td><td>"+"<a href='https://www.google.com/search?q="+urllib.quote_plus(data["event"][k]['query']['query_text'])+"' target='_blank'>"+data["event"][k]['query']['query_text']+"</a></td></tr>\n")
			except:
				continue
fi.write("</table>")
fi.write("</body></html>")
fi.close()