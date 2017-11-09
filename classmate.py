from elgamal import *

#=====================================#
#            # QUESTION 4 #           #
#=====================================#

#1) Generate a private Key

em= ElgamalModule()
print "p = "+ str(em.getLargePrime()) # set the a random largeprime number and returns the large prime
print "private key = "+ str(em.getPrivateKey()) # gets the private key where 1 <private_key < large_prime-1, if large prime does not yet exist it would be created and used acordingly

#2) Generate the corresponding public Key

print "g = "+ str(em.getPrimitiveRoot()) # gets the primitive root of the large prime number that has already been set, if no large prime number exsists yet, then the large prime would be created and the smallest primitive root of the large prime would be found
print "e = "+ str(em.computeE())
print "public key = "+ str(em.getPublicKey())

#3) Encrypt the private key using the DES algorithm. Use a secret password. Why is this necessary?

des = DES.new('01234567', DES.MODE_ECB) # secrete key
text = str(em.getPrivateKey())
multiplier=1
while True:
    if len(text)<8*multiplier:
        text=text+" " * ((8*multiplier) - len(text))
        break
    multiplier=multiplier+1

cipher_text = des.encrypt(text)
print "cipher text from DES = "+ cipher_text

#4) Save the encrypted private key to a file called privatekey.dat 

file = open("privatekey.dat","w")
file.write(cipher_text)
file.close()

#5) Save the public key to a file called publickey.dat 

file = open("publickey.dat","w")
file.write(str(em.getPublicKey()))
file.close()

#6) Use the public key from step 2 to encrypt using the Elgamal approach, a 144 twitter message to President Trump. 

file = open("twitermsg.txt","r")
print file.read()

file.close()



file = open("publickey.dat","r")
pk=file.readline()
file.close()
pk=ast.literal_eval(pk) # https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
print pk["large_prime"]



print "cipher text from DES = "+ cipher_text
print "deciphered text from DES = "+ des.decrypt(cipher_text)