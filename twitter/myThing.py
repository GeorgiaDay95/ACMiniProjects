import twitter, sqlite3, shutil, urllib2
from bs4 import BeautifulSoup
from random import randint


coolWords = ["WOW, ", "I Love ", "Go look at ", "I've just loaded ", "This is great: "]
coolWordLength = len(coolWords)-1
coolWord = coolWords[randint(0, coolWordLength )]
#print coolWord



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

cursor.execute("SELECT * FROM urls")
    
rows = cursor.fetchall()


myArray = []

for row in rows: 
    myArray =  row[1]
    
newArray = myArray.split("\n")

latestURL = newArray[-1]
#print latestURL

soup = BeautifulSoup(urllib2.urlopen(latestURL), "html.parser")
myTitle = soup.title.string
print myTitle
if (len(myTitle) > 140):
    myTitle = myTitle[:120]

myTweet = api.PostUpdate(coolWord + myTitle )
#print myTweet

console.close()




#VtqjJTKCdW6pYRaywbgCgK1Mv
#GLkNhc9jjp2cEV6sVn6LD3mql1rm7NGJi1Fdk4GlA6i3Cziiev
#791949579004502017-e48wBPSgm39z14KqsLO9dJHN2EQo6CB
#Fjqz66XhvflbsvEOIn6KZWnPy4oc0n60YKCWXjV5klQTb
# /Users/georgiaday/Library/Application Support/Google/Chrome/Default
# Georgias-MacBook:~ georgiaday$ cat /Users/georgiaday/Library/Application\ Support/Google/Chrome/Default/Current\ Session 


