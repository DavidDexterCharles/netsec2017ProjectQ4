import random
import ast

from Crypto.Cipher import DES


class ElgamalModule(object):
    
    def __init__(self):
        self.large_prime=0#58613#13
        self.primitive_element=0#2#0
        self.private_key=0#9
        self.e=0
        self.public_key={}
        self.elgamal_ciphertext={}
        self.elgamal_ciphertextC1=""
        self.elgamal_ciphertextC2=""

    def encode(self,text ):
        result = 0
        for c in text :
            result = 256* result + ord ( c )
        return result

    def decode (self,number ):
        number = int ( number )
        result = ""
        while number !=0:
            result = chr ( ( number % 256) ) + result
            number //= 256
        return result



    def millerRabin(self,p,iterations):
        if p ==2:
            return True
        elif p==1 or p%2==0:
            return False
        pminusone=p-1
        twodivideamt = 0
       
        while pminusone%2==0:
            pminusone = pminusone/2
            twodivideamt = twodivideamt +1

        for j in range(1,iterations):
            a= random.randint(2, p-1)
            T = self.powmod(a,pminusone,p)
            if T!=1 and T!=p-1: 
                iternum=1

                while(iternum <= twodivideamt-1) and (T!=p-1):
                    T = self.powmod(T,2,p)
                    iternum = iternum+1
                if T!=(p-1):
                    return False
        return True

    def powmod(self, x, y, z):
        num = 1
        while y:
            if y & 1:
                num = num * x % z
            y >>= 1
            x = x * x % z
        return num

    def getLargePrime(self): #https://stackoverflow.com/questions/21043075/generating-large-prime-numbers-in-python
        if self.large_prime==0:
            while True:
                p = random.randrange(1001, 10000, 2)
                if all(p % n != 0 for n in range(3, int((p ** 0.5) + 1), 2)):
                    if self.millerRabin(p,5):# use miller rabin to check if prime
                        self.large_prime=p
                        return p
        else:
            return self.large_prime

    def getPrimitiveRoot(self):
        if self.primitive_element==0:
            prim=[]
            n=self.getLargePrime()
            for i in range(1,n):
                prim.insert(1,i)
                check=0
                for j in range(2,n):
                    check+=1
                    x= self.powmod(i,j,n)
                    if x in prim: 
                        break
                    prim.insert(j,x)
                if j==n-1: 
                    self.primitive_element=i
                    return i

                prim[:] = []
        else:
            return self.primitive_element

    def getPrivateKey(self):
        if self.private_key==0:
            self.private_key= random.randint(2, self.getLargePrime()-2)
        return self.private_key

    def computeE(self):
        if self.e==0:
            self.e=self.powmod(self.getPrimitiveRoot(),self.getPrivateKey(),self.getLargePrime())
        return self.e

    def getPublicKey(self):
        if len(self.public_key)==0:
            self.public_key["large_prime"]=self.getLargePrime()
            self.public_key["primitive_element"]=self.getPrimitiveRoot()
            self.public_key["e"]=self.computeE()
        return self.public_key
    
    def getCiphertext(self):
        return self.elgamal_ciphertext


    def elgamalEncrypt(self,message):
        
        k=random.randint(2, 100)
        p=self.getLargePrime()
        g=self.getPublicKey()["primitive_element"]
        e=self.getPublicKey()["e"]
        c1= self.powmod(g,k,p)
        # print "message = ",message
        c2=((message%p)*self.powmod(e,k,p))%p
        # print "c2 value ", c2
        self.elgamal_ciphertext["c1"]=c1
        self.elgamal_ciphertext["c2"]=c2
        self.elgamal_ciphertextC1=c1
        self.elgamal_ciphertextC2=c2
        return self.elgamal_ciphertext

    def elgamalDecrypt(self,cipher,privatekey,publickey):
        c1=cipher["c1"]
        c2=cipher["c2"]
        p=publickey["large_prime"]
        d=privatekey
        k = self.powmod(c1,d,p)
        # print "value of k: ", k
        # print "decrypt c2 value ", c2
        plaintext=((cipher["c2"]%p)*(self.powmod(k,p-2,p)))%p
        return plaintext