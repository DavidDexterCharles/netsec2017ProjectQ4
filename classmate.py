from elgamal import *

#=====================================#
#            # QUESTION 4 #           #
#=====================================#

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
file.write(cipher_text)
file.close()

#5) Save the public key to a file called publickey.dat 
print "\nQuestion 5"
file = open("publickey.dat","w")
print str(em.getPublicKey())+""
file.write(str(em.getPublicKey()))
file.close()

#6) Use the public key from step 2 to encrypt using the Elgamal approach, a 144 twitter message to President Trump. 
print "\nQuestion 6"
# tweet="This is my tweet"
# print "The tweet to encode: "+"T"
tweet=" "
message=em.encode(tweet)
# print result
# print "encoded="+str(result)
# result = em.decode(result)
# print "decoded=", result
# print "part of tweet:", result
print "message = ",message
print "p = ",em.getLargePrime()
print "g = "+ str(em.getPrimitiveRoot())
print "d = "+ str(em.getPrivateKey())
print "e = "+ str(em.computeE())
print "public key = "+ str(em.getPublicKey())
print "Cipher : "+str(em.elgamalEncrypt(message))
print "Plain Text: "+str(em.elgamalDecrypt(em.getCiphertext(),em.getPrivateKey(),em.getPublicKey()))
print "Actual plain text: "+str(em.decode(em.elgamalDecrypt(em.getCiphertext(),em.getPrivateKey(),em.getPublicKey())))
# "multiplicative inverse and (a^p-2 mod p)"

# file = open("publickey.dat","r")
# pk=file.readline()
# file.close()
# pk=ast.literal_eval(pk) # https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
# print pk["large_prime"]



# print "cipher text from DES = "+ cipher_text
# print "deciphered text from DES = "+ des.decrypt(cipher_text)