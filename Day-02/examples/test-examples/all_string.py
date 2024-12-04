str1 = "ram" 
str2 = "vijay"
result = (str1 + str2) # string concatination

life = "always be happy"
length = len(life) #length of the charactors

my_name ="Aravind from Vizag"
lowercase = my_name.lower()
uppercase = my_name.upper()         # uppercase or lowercase


a = " Iam a maharaj"
b = " that is sivaji "
change = a.replace("maharaj", "king")   #replacing the character
modifying = b.split()       # spliting the character


info = "I am here"
substring = "I"
if substring in info:
    print(substring,"am available")     # substring

print("changed",modifying)
print("modified", change)
print("Lowercase", lowercase)
print("uppercase", uppercase)
print("lenght of the character ", length)
print(result)



