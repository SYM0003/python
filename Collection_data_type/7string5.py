# ABOUT: THIS PROGRAM IS DEMONASTRATING THE USE OF  repleace() function

s=input("please enter a stirng\n")
print(s)
s1=s.replace('dificult','easy')
# s.replace("dificult","easy")
print(s1)


#suppose i wan't to remove each blank space from the 
# give string than i can use this function
# some may ask why noy strip()-->> cause it doesn't remove the 
# blank space that are present in the middile of the string


s="sdkfh sdlfkj hfsdfjk sdfk sdlfjss dfj"
print("string before removing the space")
print(s)
s1=s.replace(" ", "")
print("string after removing the space")
print(s1)
