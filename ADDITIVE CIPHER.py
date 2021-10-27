#!/usr/bin/env python
# coding: utf-8

# # ADDITIVE CIPHER TECHNIQUE----> ENCRYPT

# In[2]:



def encrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result
 
#check the above function
text =  (input ( " enter the text: "))
s = int(input(" enter the shift:"))
print ("Text  : " + text)
print( "Shift : " + str(s))

print (" Ceaser Cipher: " + encrypt(text,s))


# # ADDITIVE CIPHER TECHNIQUE------>DECRYPT
#      

# In[3]:




def decrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
 
    return result
 
#check the above function
text =  (input ( " enter the  plane text: "))
s = int(input(" enter the shift between 0 to 25:"))
print ("Text  : " + text)
print( "Shift : " + str(s))
print ("Cipher: " + decrypt(text,s))


# In[ ]:




