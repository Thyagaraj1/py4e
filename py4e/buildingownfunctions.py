#we create a new function using the def keyword followed by optional parameteres in parenthesis
def print_lyrics():
    print("I'm luberjack, and I'm okay")
    print("I sleep all night and work all day")
#def just remebers the code but doesn't excecute the code unless invoked, we need to invoke it

#Not invoked
x=5
print('hello')
def print_lyrics():
    print("I'm a master")
    print("I work hard")
print('Yo')
x=x+2
print(x)

#hello
#Yo
#7


#Invoked
x=5
print('hello')
def print_lyrics():
    print("I'm a master")
    print("I work hard")
print('Me')
print_lyrics()

#Me
#I'm a master
#I work hard
