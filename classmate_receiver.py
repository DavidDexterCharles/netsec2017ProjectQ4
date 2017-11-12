from elgamal import *
####### THE RECEIVING CLASSMATE...classsmate receiving the encrypted message #######
em= ElgamalModule()
print "\nQuestion 10"
#10)Your classmate you since you are in the class should write a python program to use
    #the encrypted letter and decrypted private (used the DES key from step 9) to decrypt the
    #letter and print its contents to the screen
file = open("des_key.txt","r")
des_key=file.read()
file.close()

print "des_key read from des_key.txt file = ", str(des_key),"\n"
des_for_receiver = DES.new(str(des_key), DES.MODE_ECB) # secrete key

file = open("privatekey.dat","r")
decrypted_privatekey=int(des_for_receiver.decrypt(file.read()))
file.close()
print "Decrypted private key read from privatekey.dat file = ", str(decrypted_privatekey),"\n"

file = open("publickey.dat","r")
publickey_accessed=ast.literal_eval(file.read())
file.close()
publickey_accessed["e"]=int(publickey_accessed["e"])
publickey_accessed["large_prime"]=int(publickey_accessed["large_prime"])
publickey_accessed["primitive_element"]=int(publickey_accessed["primitive_element"])
print "Public key read from publickey.dat file = ",publickey_accessed, "\n"

file = open("encrypted_letter.dat","r")
cipher_text_received=file.read()
file.close()
print "The cipher text received is read in from encrypted_letter.dat \n"



clist=cipher_text_received.split(" ")
# print clist
# print clist
decoded_text=""
C={}
for i in range(1,len(clist)+1):
    # print i
   
    if i%2!=0: # allows me to select the c1 and c2 in question 
        C["c1"]=int(clist[i-1])
    else:
        C["c2"]=int(clist[i-1])
        # print C#,em.getCiphertext()
        # print "Plain Text: "+str(em.elgamalDecrypt(C,em.getPrivateKey(),em.getPublicKey()))
        decoded_text+=str(em.decode(em.elgamalDecrypt(C,decrypted_privatekey,publickey_accessed)))
        
  

print "The Decrypted Received Message:\n\n ", decoded_text