import random
from Crypto.Cipher import DES


class ElgamalModule(object):
    
    def __init__(self):
        self.large_prime=0
        self.primitive_element=0
        self.private_key=0
        self.e=0
        self.public_key={}

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
            self.e=pow(self.getPrimitiveRoot(),self.getPrivateKey(),self.getLargePrime())
        return self.e

    def getPublicKey(self):
        if len(self.public_key)==0:
            self.public_key["large_prime"]=self.getLargePrime()
            self.public_key["primitive_element"]=self.getPrimitiveRoot()
            self.public_key["e"]=self.computeE()
        return self.public_key

        # return

des = DES.new('01234567', DES.MODE_ECB)
text = 'abcdefgh'

cipher_text = des.encrypt(text)

print cipher_text

print  des.decrypt(cipher_text)

em= ElgamalModule()

print em.getLargePrime() # set the a random largeprime number and returns the large prime
em.getPublicKey()
print em.getPrimitiveRoot() # gets the primitive root of the large prime number that has already been set, if no large prime number exsists yet, then the large prime would be created and the smallest primitive root of the large prime would be found
print em.getPrivateKey()# gets the private key where 1 <private_key < large_prime-1, if large prime does not yet exist it would be created and used acordingly




