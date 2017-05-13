#List of TOR Exit Nodes from
#https://check.torproject.org/exit-addresses
#Developer: Bill Shaw

link = "https://check.torproject.org/exit-addresses"
import urllib.request
import json

#import MySQLdb
#conn = MySQLdb.connect(host= "<hostname>",
#                  user="<username>",
#                  passwd="<password>",
#                  db="<database>")
#x = conn.cursor()

with urllib.request.urlopen(link) as response:
   html = response.read()

lines = str(html).split('ExitAddress ')

i=1
ip = []
for l in lines:
    i=1-i #flip a bit
    if (i == 0):
        continue
    else:
        output = l.split(' ')
        ip.append(output[0])
#        print (output[0])
#        try:
#            sql = "INSERT INTO table `src`='TOR', `ip`='" + output[0] + "';"
#            x.execute(sql)
#            conn.commit()
#        except:
#            conn.rollback()
jsonString = '{"TOR Exit Node":' + str(ip) + '}'
json = json.JSONEncoder().encode(jsonString)
print(json)
#conn.close()
