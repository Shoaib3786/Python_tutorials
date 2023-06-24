
1.
percentage=int(input("enter your marks"))

if (percentage > 95):
    print(" grade a")

elif(percentage >70) and (percentage <96):
       print("grade b")

elif(percentage >60) and (percentage <71):
     print("grade c") 

elif(percentage >50) and (percentage <60):
     print("grade d")

elif(percentage >40) and (percentage <50):
    print("grade e")

elif(percentage ==29) and (percentage ==30):
     print("grade f")

elif(percentage ==10) and (percentage ==11):
     print("grade g")      

# 2.
# Q:write python code if tomorrow it isn't too hot,i'll go to sea, but if it is,i'll have a walk in the forest.however,if it rains,i'll stay at home.
# a=input("enter weather:")

if (a!="too hot") and ("a!=rain"):
  print("i will go to the sea")

elif (a=="too hot"):
  print("i'll have a walk in the forest")

elif (a=="rain"):
  print("i'll stay at home")

# 3.         
# Q: accept any city name from the user and display the monuments of the city name:
#  -if city is Delhi then print monuments of Red fort
#  -if city is Agra then print monuments of Taj mahal
#  -if city is Jaipur then print monuments of Jal mahal

a=input("enter city name:")

if a==("delhi"):
    print("print monuments of Red fort")

elif a==("agra"):
    print("monuments of Taj mahal")   

elif a==("jaipur"):
    print("monuments of Jal mahal")

# 4.
# Q:write python program to check whether a person is senior citizen or not:
#   -if person's age >60 then he/she is a senior citizen
#   - else he/she is not
a = int(float(input("enter age of citizen:")))

# [or]
a = input("enter age of citizen:")
a = float(a)
a = int(a)

print(type(a))

if (a > 60):
    print("senior citizen")

else:
   print("not senior citizen")

