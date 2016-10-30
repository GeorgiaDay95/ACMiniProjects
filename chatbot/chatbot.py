import wikipedia

goodResponse = ["happy", "great", "relaxed", "content", "excited", "good",]
badResponse = ["sad", "down", "angry", "tearful",]
pet = ["cat", "dog", "rabbit", "bunny", "hampster", "gerbil", "chinchilla", "rat", "mouse", "fish", "guinipig",
      "horse", "snake", "lizard", "frog", "parrot", "bird", "hedgehog",]
fWords = []    
bye = ["Well I'm pretty tired now, so i'll see you later!", "Bye!!", "Im bored of you now, cya!", "hmm, ill ttyl"]
bye = len(bye)-1
bye = bye[randint(0, bye )]

# only used stop words in the first few questions as an exaple - would work fully throughout code
wordstuff = open("stopwords.txt")
words = wordstuff.read()
word = words.split("\n")

def splitResponse(response):
    print response
    myInput = response.split(" ")
    for Input in myInput:
        if (Input not in words):
            fWords.append(Input)
#    print fWords
    return fWords[-1]

# can type and type of yes or no as answer and will accept it
def yesNoAnswer(answer):
    answer = answer.lower()
    YNresponse = False
    if answer == "yes" or answer == "y" or answer == "yeah" or answer == "ye m8" or answer == "mhmm":
        YNresponse = True
        answer = "yes"
    if answer == "no" or answer == "n" or answer == "naa" or answer == "nope" or answer == "nuh uh":
        YNresponse = True
        answer = "no"
    return answer

name = splitResponse(raw_input("Hi, I'm ChatBot - What's your name? "))
print("Hello "+ name + "! Nice to meet you.")
feeling = splitResponse(raw_input("So, how are you feeling today " + name + "? "))
    # if statements to determine the answer whether happy or sad
if feeling not in str(badResponse) and feeling not in str(goodResponse):
    print("Sorry, I dont know what that means..")
    feeling = ""
    while (feeling == ""):
        feeling = raw_input("Lets try that again "+name + ", how are you feeling today? ")

if feeling in str(badResponse):
    print("Oh, thats not good " + name + ", maybe I can cheer you up.")
    favPet =  raw_input("Lets talk about things you like! What is your favourite pet? ")
    
elif feeling in str(goodResponse):
    print("yay!! Im glad youre feeling " + feeling + " today.")
    whyHappy = raw_input("why are you feeling " + feeling + " "+ name + " ?")
    print("Oh I see! Well I am " + feeling + " that you are " + feeling)
    favPet = raw_input("I really want to get to know you " + name + ". What is your favourite pet? ")
    
#if pet isnt in array will be added to the array is you tell chatbot it is a real animal
while (favPet not in str(pet)):
    question = raw_input("I havent heard of a " + favPet + " before. Is that really a pet? ")
    if (question == "no"):
        favPet  = raw_input("Okay " + name + " what really is your favourite pet? ")
    elif (question == "yes"):
        pet.append(favPet)
        
        
if favPet in str(pet):
    question = raw_input("Oh, so you love " + favPet + "'s? ").lower()
    while yesNoAnswer(question) != "yes" and yesNoAnswer(question) != "no":
        question = raw_input("A yes or no will do nicely thank you? ")
    if question == "yes":
        myPet = raw_input("I love " + favPet + "'s too! Do you own one? ")
        while yesNoAnswer(myPet) != "yes" and yesNoAnswer(myPet) != "no":
            myPet = raw_input("Sorry, I didnt quite catch that. Do you own a " + favPet + "? ")
        if myPet == "yes":
            print("Aw, you're so lucky to have a " + favPet + "! I wish I could have one.. But im just a chatBot..")
        elif myPet == "no":
            print("That is a shame, maybe you can get a " + favPet + " one day!")
    elif question == "no":
        print("Ohh. Well its weird you would say its your favourite pet then.. What can I say, you are only human")
        
        #can talk about anything from wikipedia search     
response = raw_input("I'll stop asking the questions! What do you want to talk about? ")
wikiSearch = wikipedia.search(response, results = 10)
#print (wikiSearch)
x = 1
for answers in range(len(wikiSearch)):
    yesNo = raw_input("Are you talking about " + wikiSearch[x] + "? " )
    if (yesNoAnswer(yesNo) == "yes"):
        info = wikipedia.summary(wikiSearch[x], sentences = 3)
        print (info)
        break
    x = x + 1
    # limmits results to three things so doesnt get tedious
    if (x >= 3):
        yesNo = raw_input("I'm running out of ideas here.. Did you mean " + wikiSearch[x] + "? ")
        if (yesNoAnswer(yesNo) == "yes"):
            info = wikipedia.summary(wikiSearch[x], sentences = 3)
            print (info)
            break
        if (yesNoAnswer(yesNo) == "no"):
            yesNo = raw_input("Well I don't know then! Do you want to change the subject? ")
            if (yesNoAnswer(yesNo) == "yes"):
                #able to change subject if you said no too many times
                response = raw_input("What do you want to change the subject to? ")
                wikiSearch = wikipedia.search(response, results = 10)
                x = 1
            if (yesNoAnswer(yesNo) == "no"):
                print "Okay, sorry I dont know everything."
                break
print bye

    