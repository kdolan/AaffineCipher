def egcd(a, b):
    i = 1
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        i+=1
    #print(b,x,y)
    return b, x, y
def modinv(a, m):
    #print("DOING: " +str(a))
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


#for i in range(1,13):
#    print(str(i)+": "+str(modinv(i,13)))


#print(modinv(3,26))
"""
Author: Kevin J Dolan (Github: kdolan)
Date: 2/15/2013
Purpose: Affine cipher all purpose caculator
"""
from math import exp
#Global abc list
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class Map:
    """Map handles the encryption and decryption of strings. Map is initialized with an a, b, and a modulus m."""
    __slots__ = "encryptDict","decryptDict","a","b","m"
    
    def __init__(self, a, b, m):
        """
        Parameters: a, b, m. A is the multiplicative modifier and b is the additive modifier.
        Initializes the map class and creates the encryption and decryption dictionaries.
        """
        self.encryptDict = {}
        self.decryptDict = {}
        self.a = a
        self.b = b
        self.m = m
        counter = 1 
        for letter in abc:
            encryptedValue = (a*counter+b)%m
            self.encryptDict[letter]=encryptedValue
            self.decryptDict[encryptedValue] = letter
            counter+=1

    def __str__(self):
        """Returns a string with a map for all letters and their coresponding encrypted values."""
        string = ''
        counter = 0
        for letter in abc:
            string+=letter+" -> "+str(self.encryptDict[letter])+'\n'
            counter += 1
        return string
        
    def decryptList(self, list):
        """Takes a list of encrypted ints and returns the decrypted string."""
        dycryptedString = ''
        for encryptedNumber in list:
            dycryptedString+=str(self.decryptDict[encryptedNumber])
        return dycryptedString
    
    def encryptString(self, string):
        """Takes a string and returns a list of encrypted ints."""
        string = string.upper()
        encryptedList = []
        for char in string:
            encryptedList.append(self.encryptDict[char])
        return encryptedList

def checkPrime(number, m):
    """Checks to see if a number is prime using Fermat's little theorem."""
    num = int(number)
    b = m**(num-1)
    if (b % num) == 1:
        print("Most likely prime. Probability: "+str(((.5)**m)*100))
    else:
        print("NOT prime")
        

map = Map(3,7,37) 
print(map.encryptString('HELP'))     
map = Map(10,23,37)
print(map)
print(map.decryptList([1,29,36,33,15,28,31,36,18,2,28,1,31,25]))

"""
Output:
[31, 22, 6, 18]
A -> 33
B -> 6
C -> 16
D -> 26
E -> 36
F -> 9
G -> 19
H -> 29
I -> 2
J -> 12
K -> 22
L -> 32
M -> 5
N -> 15
O -> 25
P -> 35
Q -> 8
R -> 18
S -> 28
T -> 1
U -> 11
V -> 21
W -> 31
X -> 4
Y -> 14
Z -> 24

THEANSWERISTWO

"""
