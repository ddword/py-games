#import urllib.request as ur
#response = ur.urlopen('http://www.python.org')
#html = response.read().decode().split('/n')

#print(response.info())

#for line in html:
    #if 'tag' in line:
        #print(line, end =' ')

#import urllib.request
#from bs4 import BeautifulSoup

#url ='http://www.groupce.com/python/html/thejourney.html'
#response = urllib.request.urlopen(url)
#html = response.read()

##soup = BeautifulSoup(html,"html.parser")
#parserHtml = BeautifulSoup(html,"html.parser")
##a_tags = soup('a')
#a_tags = parserHtml('a')


#for rows in a_tags:
    #print(rows)
##https://www.crummy.com/software/BeautifulSoup/bs4/doc/ - docs for  BeautifulSoup
#import urllib.request
#from bs4 import BeautifulSoup

#url ='http://www.groupce.com/python/html/thejourney.html'
#response = urllib.request.urlopen(url)
#html = response.read()

##soup = BeautifulSoup(html,"html.parser")
#parserHtml = BeautifulSoup(html,"html.parser")
##a_tags = soup('a')
#a_tags = parserHtml('a')

#for rows in a_tags:
    #if 'ins' in rows.the_contents:
        #print(rows)
    #print(rows.get('href'))
    #print(rows.contents[0])

#import urllib.request
#import json
#url = "http://www.groupce.com/python/json/json_comments.json"
#jsondata = urllib.request.urlopen(url).read().decode()
#print(jsondata)

#serialize - save in JSON /unserialize - from JSON format to user
#sorting dictionaries - method sorted()
#https://www.pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/

#1)
#import urllib.request as ur
#response = ur.urlopen('http://www.bbc.com/news')
#Html = response.read()
#print(len(Html))
#html = Html.decode().split('/n')
#i = 0
#for line in html:
    #i = i + 1
    #print(line, end =' ')
#print(i)
#2)
# import urllib.request
# from bs4 import BeautifulSoup
# url = 'http://www.meteomedia.com'
# response = urllib.request.urlopen(url)
# html = response.read()
#
# parserHtml = BeautifulSoup(html,"html.parser")
# a_tags = parserHtml('a')
#
# for rows in a_tags:
#     if rows.get('href') != '':
#         print(rows)
#         print(rows.get('href'))
#4)
import urllib.request
import json
url = 'http://www.groupce.com/python/json/json_comments.json'
jsondata = urllib.request.urlopen(url).read().decode()
info = json.loads(jsondata)
#print(info['comments'])
for row in info['comments']:
    if 'A' in row['name']:
        print(row['name'], row['count'])
#5)