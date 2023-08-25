"""STRINGS"""

"""
Q. Make a python program to:

1. Take two string sentences from the user input 
and store it in the variable "mString" and 
"mString2". [MAKE SURE THE STRING LENGTH SHOULD BE 
GREATER THAN 7]
"""

mString = input("Enter string 1:  ")
mString2 = input("Enter string 2:  ")

while (len(mString) <= 7 and len(mString2) <= 7):
        
  print('String 1 or String 2 lenght is less than 7 plz enter it again...')
  mString = input("Re-Enter string 1:  ")
  mString2 = input("Re-Enter string 2:  ")

  if (len(mString) >= 7 and len(mString2) >= 7):
    break
        
  

# mString = "Hello people, Love to hear you..."
# mString2 = "Bye People nice to meet you!!!"  




"""
2. Pefrom concatiantion operation with over 
mString and mString2.
"""

print(mString + mString2)


"""
3. Pefrom slicing of firt 5 elements from the 
mString2.
"""

print(mString2[:6])  # slicing [start : end]   -> In slicing end point goes till end-1



"""
4. Print string '*' 10 times using string 
operation [don't use print('*') with FOR LOOP].
"""
i = '*'
print( 10 * i ) # produces string '*' 10 times



"""
5. Strip the elements of the mString from 
leading and beginning.
"""

print(mString.strip())  # strip's the whitespaces if it exists in the (leading and ending)


"""
6. Split the elements of the mString 
(splitting should be word by word).
"""

print(mString.split())    # split will create the list of words in the mString if I don't specify any parameter in the split() function.

"""
7. Loop each character of the string and print it.
"""

for i in mString:
  print(i) 


"""
8. Replace the characters in the string.
"""

string1 = "heo"
s = string1.replace('e', 'Aaloo')

print(s)


"""
9. print the mString sentence characters seperatly in the list.
"""

m = [*mString]   # [*mString] -> putting star is another method that you must know it as a method which can be memorized. 
print(m)

"""
10. join the list of the string charaters(letter)
 using .join().
"""

m = ['m', 'o', 'r', 'e', ' ', 'o', 'n']
con = ''
print(con.join(m))


"""
11. Split the mString into list of seperate 
strings characters(NOTE not to seperate by words) 
and then again merge them into string of sentence 
into orginal form.
"""

m = [*mString] # splittig the mString in list of characters in the mString.
con = ''
print(con.join(m))  # joining the list.



"""
12. Print this pattern using String opertion not
 by previous multiple looping method.
        * 
      * * 
    * * * 
  * * * * 
* * * * * 

(HINT: use string multiplication method refer Q4 above follow same 
procedure)
"""

row = 5
for i in range(1, row+1):

  for j in range(0, row-i):

    print('', end=" ")

  print( i * "*", end = '  ')  # printing stars i time with spaces thus "* "

  print('\n') # after printing stars we need to move to the next line/row. 



