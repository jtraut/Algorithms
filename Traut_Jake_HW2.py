"""
Assignment Name: HW2 

Author: Jake Traut 

Description: This program runs a RSA scheme to encode and decode a message

Additional Notes: Original message set to 2015

Date: 9-15-15

"""
import random 
import time

global m 
m = 2015

def rand_prime():
    while True:
        p = random.randrange(101, 10000, 2)
        q = random.randrange(101, 10000, 2)
        if (all(p % n != 0 for n in range(3, int((p ** 0.5) + 1), 2)) & all(q % n != 0 for n in range(3, int((q ** 0.5) + 1), 2)) & (p.bit_length() == q.bit_length())):      
			print "p = ", p, " q = ", q
			return p, q

#extended euclid algorithm		
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
        
#Encryption
def encrypt(key):
	e, n = key 
	c = (m ** e) % n 
	print "Encrpyted message c = ", c
	return c
	
#Decryption	
def decrypt(key, c):
	d, n = key
	m = (c ** d) % n
	print "Decrypted message m = ", m
	return m
	
		    
def rsa_keys():
	start = time.clock()
	
	(p, q) = rand_prime()
	n = p * q  #modulus n 
	t = (p-1)*(q-1) #totient phi(n) 
	#print "t = ", t 
	print "n = ", n
	
	#public key generator 
	i = 0
	while i == 0:
		e = random.randrange(3, t, 2) #public key e
		if (all(e % n != 0 for n in range(3, int((e ** 0.5) + 1), 2)) & (t % e != 0)):
			#print "e = ", e
			i = 1
	pub_key = (e, n)
	
	#private key generator
	gcd, x, y = egcd(e, t)
	if (gcd == 1): 
		d = x % t
	else:
		d = None #no mod inverse
		
	pri_key = (d, n)
	
	end = time.clock()
	key_runtime = end - start 
	
	print #nicer output 
	
	print "RSA Key generator runtime = ", key_runtime
	
	print 
	
	start = time.clock()
	c = encrypt(pub_key)
	end = time.clock()
	en_runtime = end - start 
	
	print "Encryption runtime = ", en_runtime
	
	print
	
	start = time.clock()
	m = decrypt(pri_key, c)
	end = time.clock()
	de_runtime = end - start
	print "Decryption runtime = ", de_runtime
	
rsa_keys()

	


 

