import twitter, sqlite3, shutil, urllib2
from bs4 import BeautifulSoup
from random import randint

#random phrase in front of tweet
coolWords = ["WOW, ", "I Love ", "Go look at ", "I've just loaded ", "This is great: "]
coolWordLength = len(coolWords)-1
coolWord = coolWords[randint(0, coolWordLength )]
#print coolWord


#open file and split 
file = open("creds2.txt")
credStuff = file.read()
#print credStuff
creds = credStuff.split('\n')
#print creds[0]
#print creds[1]
#print creds[3]
api = twitter.Api(creds[0],creds[1],creds[2],creds[3])
file.close()

shutil.copyfile("/Users/georgiaday/Library/Application Support/Google/Chrome/Default/History", "history")

history = "history"
console = sqlite3.connect(history)
cursor = console.cursor()
# find the urls in the history
cursor.execute("SELECT * FROM urls")
    
rows = cursor.fetchall()


myArray = []
#look through array of urls and split everything then -1 to find the last thing in that array
for row in rows: 
    myArray =  row[1]
    
newArray = myArray.split("\n")

latestURL = newArray[-1]
#print latestURL
open
#finds the title in the latest url found
soup = BeautifulSoup(urllib2.urlopen(latestURL), "html.parser")
myTitle = soup.title.string
print myTitle
#ensures the title isnt more than 120 characters (to allow for phrase as well)
if (len(myTitle) > 140):
    myTitle = myTitle[:120]
# tweets phrase and title of web page
myTweet = api.PostUpdate(coolWord + myTitle )
#print myTweet

console.close()




#VtqjJTKCdW6pYRaywbgCgK1Mv
#GLkNhc9jjp2cEV6sVn6LD3mql1rm7NGJi1Fdk4GlA6i3Cziiev
#791949579004502017-e48wBPSgm39z14KqsLO9dJHN2EQo6CB
#Fjqz66XhvflbsvEOIn6KZWnPy4oc0n60YKCWXjV5klQTb
# /Users/georgiaday/Library/Application Support/Google/Chrome/Default
# Georgias-MacBook:~ georgiaday$ cat /Users/georgiaday/Library/Application\ Support/Google/Chrome/Default/Current\ Session 


