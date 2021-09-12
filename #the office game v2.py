#the office game v2
#JJ Bergren Ramirez
#20210831


#setting up basic interactions w characters and returning player choice
def interact():
    print('You can Flirt, Thats What She Said, or Prank Dwight')
    choice = input('Enter F, TWSS, or P.')
    return choice.lower()

#win/lose mechanics
def winner():
    print('Wow! Great job! You win!')

def loser():
    print('Better luck next time. Now youre stuck talking to this person all day.')

#start game
def startGame():
    print('You are a new hire at a local paper company, Dunder Mifflin. Its time to meet and greet all your new coworkers.')
    return Pam()


#characters
def Pam():
    print("Hi, I'm Pam! Welcome to Dunder Mifflin. What would you like to do?")
    action = interact()

    
    if 'f' in action:
        print("Oh, wow you are a great fit for Michael. He has his jeans on today!")
        return Michael()
    elif 'p' in action:
        print("Oh, you know who needs some prank ideas? Dwight. He needs to get Jim back for yesterday.")
        return Dwight()
    elif 't' in action:
        print("Dude you just got here and you're already making jokes like that?")
        return Toby()
    else: 
        print('thats not available today, sorry. try something else.')
        return Pam()

def Michael():
    print('You enter Michaels office')
    print('Welcome welcome welcome! We havent had someone new since our temp Ryan!')
    action = interact()

    
    if 'f' in action:
        print("I am Beyonce, always.")
        return Ryan()
    elif 'p' in action:
        print("I don’t come up with this stuff, I just forward it along. You wouldn’t arrest the guy who was just passing drugs from one guy to another.")
        print("Anyway, go hang out with Jim. He's the one who likes the PRANKS!!")
        return Jim()
    elif 't' in action:
        print("Make friends first, make sales second, make love third. In no particular order.")
        return winner()
    else: 
        print('thats not available today, sorry. try something else.')
        return Michael()

def Jim():
    print('You approach Jims desk.')
    print('Hey dude. Whats up?')
    action = interact()

    
    if 'f' in action:
        print("Jim flirts back with you a little bit. Maybe you've made this hottie forget about Pam, finally!")
        return winner()
    elif 'p' in action:
        print("""Oh awesome! Some of the goof balls are outside doing parkour, the internet sensation of 2004. 
        It was in one of the Bond films. It’s pretty impressive. The point is to get from point A to point B as creatively as possible, 
        so technically they are doing parkour as long as point A is delusion and point B is the hospital.""")
        return Dwight()
    elif 't' in action:
        print("Oh man, you must be looking for our boss. He thinks those jokes are funny too.")
        return Michael()
    else: 
        print('thats not available today, sorry. try something else.')
        return Jim()


def Dwight():
    print('You approach Dwights desk. He strikes a defensive pose, reaching under his desk.')
    print('Hello. You need to complete the safety training.')
    print('As safety officer it is my duty to test you.')
    action = interact()

    
    if 'f' in action:
        print("When someone smiles at me, all I see is a chimpanzee begging for its life. Go bother Jim.")
        return Jim()
    elif 'p' in action:
        print("Please. As if I could be fooled by such a green employee's trickcery. Go talk to Accounting.")
        return Angela()
    elif 't' in action:
        print("Oh! My best friend Michael loves those jokes!")
        return Michael()
    else: 
        print('thats not available today, sorry. try something else.')
        return Dwight()


def Angela():
    print('you approach accounting, but unfortunately Angela is the only one there.')
    print('What do you want.')

    action = interact()

    
    if 'f' in action:
        print("I am really not interested in a new relationship right now. I have my hands full with the Senator.")
        return loser()
    elif 'p' in action:
        print("Dwight is a perfectly reasonable employee. I don't understand why everyone tries to get on his nerves so much!")
        return loser()
    elif 't' in action:
        print("That is highly inappropriate! You know, you could do with a church service.")
        return loser()
    else: 
        print('thats not available today, sorry. try something else.')
        return Angela()


def Ryan():
    print('You move on to the kitchen. Ryan is avoiding work by pretending to drink coffee,')
    print('he said last week that the only thing he drinks is mushroom tea shipped in from Taiwan.')
    print('Hows it going? He asks.')
    action = interact()

    
    if 'f' in action:
        print("I'm sure Kelly would love to entertain right now. Why don't you flirt with her so she leaves me alone?")
        return Kelly()
    elif 'p' in action:
        print("I'm really not interested in pulling pranks right now, Jim 2.0. But do you wanna hear about WWOOF?")
        return loser()
    elif 't' in action:
        print("There is no such thing as an appropriate joke, that’s why it’s a joke.")
        return Toby()
    else: 
        print('thats not available today, sorry. try something else.')
        return Ryan()

def Toby():
    print('You have been sent to Toby...')
    action = interact()

    
    if 'f' in action:
        print("If I had a gun with two bullets and I was in a room with Hitler, Bin Laden, and Toby, I would shoot Toby twice.")
        print("So why the hell are you flirting with him?")
        return loser()
    elif 'p' in action:
        print("Dude, you're literally talking to the HR rep. Why are you trying to pull pranks?")
        return loser()
    elif 't' in action:
        print("Toby went to seminary. I don't think he understood your joke.")
        return loser()
    else: 
        print('thats not available today, sorry. try something else.')
        return Toby()

def Kelly():
    print('Kelly approaches, looking like shes got a full tank of air.')
    interact()

    action = interact()

    
    if 'f' in action:
        print("I mean, I’m not a slut but who knows.")
        return loser()
    elif 'p' in action:
        print("""Ugh, you sound like Jim and Dwight. I'm not like them. I did a training program.
        You guys I’m like really smart now. You don’t even know. You could ask me, Kelly what’s the biggest company in the world? 
        And I’d be like, ‘blah blah blah, blah blah blah blah blah blah.’ Giving you the exact right answer.""")
        return loser()
    elif 't' in action:
        print("I have a lot of questions. Number one, how dare you?")
        return loser()
    else: 
        print('thats not available today, sorry. try something else.')
        return Kelly()

startGame()