from bs4 import BeautifulSoup
import csv
import pandas as pd
import re

df = pd.read_csv("basketballref2020.csv")

soup = BeautifulSoup(open("NBA 2K21 All Player Ratings _ NBA 2KW _ NBA 2K22 Locker Codes _ NBA 2K22 News _ NBA 2K22 MyPLAYER Builder _ NBA 2K22 Tips _ NBA 2K22 Ratings _ NBA 2K Community _ NBA 2K23 News _ NBA 2K23 Wishlist.mhtml"), features="lxml")


with open('readme.txt', 'w') as f:
    f.write(soup.prettify())
    f.close()

#each object in this playerrows resultobject holds one player in our dataset, this is totally uncleaned though.
playerrows=soup.find_all('tr')
# print(playerrows[1])

 #Now work on splitting up the stuff in the resultobject into the different things we want like name, height, etc.
 #possibly using this anoymous function to help us find the player entries we want:
##soup.find_all(lambda tag: tag.name == 'tr' and
#                           tag.get('class') == ['product']

#idea: use soup.findall with the anonymous functions to isolate the individual parts, ie the name, the team players for, overall, etc into there
#own things like playerrows above
#try getting the player ovrs in a resultobject using this method below:
overallrows=soup.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['3D"data-ovr"'])
i=0
for ovr in overallrows:
   # print(ovr)
   text = ovr.renderContents()
   overallrows[i]=text
   i=i+1

for ovr in overallrows:
    ovr=str(ovr)
    ovr=ovr.replace("b", "")
    ovr = ovr.replace("'", "")
    #now need to write a regex to get rid of leading and trailing stuff around the two #'s
    regex=r"[0-9]*\w[0-9]"
    ovr=re.search(regex,ovr).group(0)
    print(ovr)
    #we'll have to either alter the regex, as some of the digits came in as n's. alternatively,
    # we could go through and manually change them, there aren't that many.

#now work on getting height into a resultobject
heightrows=soup.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['3D"data-height"'])
i=0
for height in heightrows:
   # print(height)
   text = height.renderContents()
   heightrows[i]=text
   i=i+1

# for height in heightrows:
#     print(height)

#now work on getting name into a resultobject
namerows=soup.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['3D"data-name'])
#need to find a way to get the 'a' tag from the td.

for name in namerows:
    # name=name.find('a')
    # name=name.find('span')
    # name=name.contents[0]
    name=name.renderContents()
    # print(name)

# links = soup.find_all('a')
# for link in links:
#     names = link.contents[0]
#     fullLink = link.get('href')
#     print(names)


#the code below would make a df from the overallrows resultobject.
# df2k = pd.DataFrame(overallrows);
# print(df2k.head())