from elgamal import *

#=====================================#
#            # QUESTION 4 #           #
#=====================================#

####### THE SENDING CLASSMATE...classsmate sending the encrypted message #######


#1) Generate a private Key
print "\nQuestion 1"
em= ElgamalModule()
print "p = "+ str(em.getLargePrime()) # set the a random largeprime number and returns the large prime
print "private key = "+ str(em.getPrivateKey()) # gets the private key where 1 <private_key < large_prime-1, if large prime does not yet exist it would be created and used acordingly

#2) Generate the corresponding public Key
print "\nQuestion 2"
print "g = "+ str(em.getPrimitiveRoot()) # gets the primitive root of the large prime number that has already been set, if no large prime number exsists yet, then the large prime would be created and the smallest primitive root of the large prime would be found
print "e = "+ str(em.computeE())
print "public key = "+ str(em.getPublicKey())

#3) Encrypt the private key using the DES algorithm. Use a secret password. Why is this necessary?
print "\nQuestion 3"
des = DES.new('01234567', DES.MODE_ECB) # secrete key
text = str(em.getPrivateKey())
multiplier=1
while True:
    if len(text)<8*multiplier:
        text=text+" " * ((8*multiplier) - len(text))
        break
    multiplier=multiplier+1

cipher_text = des.encrypt(text)
print "cipher text from DES = "+ cipher_text +"\n"

#4) Save the encrypted private key to a file called privatekey.dat 
print "\nQuestion 4"
file = open("privatekey.dat","w")
print cipher_text
file.write(cipher_text)# encrypted with des
file.close()

#5) Save the public key to a file called publickey.dat 
print "\nQuestion 5"
file = open("publickey.dat","w")
print str(em.getPublicKey())+""
file.write(str(em.getPublicKey()))
file.close()

#6) Use the public key from step 2 to encrypt using the Elgamal approach, a 144 twitter message to President Trump. 
print "\nQuestion 6"
print "Message Gets encrypted using the Elgamal approach\n"
tweet='''
1. "Can you imagine what the outcry would be if @SnoopDogg, failing career and all, had aimed and fired the gun at President Obama? Jail time!"
OK...
2. "Any negative polls are fake news, just like the CNN, ABC, NBC polls in the election. Sorry, people want border security and extreme vetting."
Sounds a little Orwellian...
3. "Watched protests yesterday but was under the impression that we just had an election! Why didn't these people vote? Celebs hurt cause badly."
Umm they did Donald. That's why you lost the popular vote...
4. "We are going to have an unbelievable, perhaps record-setting turnout for the inauguration, and there will be plenty of movie and entertainment stars. All the dress shops are sold out in Washington. It's hard to find a great dress for this inauguration."
The best way to kick off the New Year Donald...
'''

cipher_text="" ## Encrypting the twiter message character by character
i=0
for c in tweet:
    a_char=em.encode(c)
    val = em.elgamalEncrypt(a_char)
    cipher_text+=str(val["c1"])+" "+str(val["c2"])+ " "

cipher_text=cipher_text.rstrip(" ") # the encypted letter
# print "Cipher : ",cipher_text

print "\nQuestion 7"
#7)Email the encrypted letter to a COMP 6801 classmate
print "Encrypted message is stored in encrypted_letter.dat"
file = open("encrypted_letter.dat","w")
file.write(cipher_text)
file.close()

print "\nQuestion 8"
#8)In a separate email attached the encrypted private key file generated from step 4 to the same classmate as step 7
print "In a separate email  the encrypted private key file generated from step 4 was attached\n"

print "\nQuestion 9"
#9)In a separate email attach the DES key used to encrypt the private in step 3
print "In a separate email the DES key used to encrypt the private key in step 3 was attached\n\n"
file = open("des_key.txt","w")
file.write("01234567")# the DES key
file.close()

print "Run classmate_sender.py to show what the receiver of the encrypted message do with it"