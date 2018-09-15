from Crypto.PublicKey import RSA
key_encoded=open('./id_rsa.pub','r').read()

def inverse(x, m):
    a, b, u = 0, m, 1
    while x > 0:
        q = b // x # integer division
        x, a, b, u = b % x, u, x, a - q * u
    if b == 1:
        return a % m
    

def main():

    pubkey = RSA.importKey(key_encoded)
    
    q = 1094782941871623486260250734009229761
    e = pubkey.e
    ct = open('./data','r').read()
    p = pubkey.n / q 

    # compute n
    n = pubkey.n

    # Compute phi(n)
    phi = (p - 1) * (q - 1)

    # Compute modular inverse of e
    # gcd, a, b = egcd(e, phi)
    d = inverse(e, phi)

    print( "n:  " + str(d) );

    # Decrypt ciphertext
    private_key = RSA.construct((n, e, d))
    dsmg = private_key.decrypt(ct)
    print( "pt: " + str(dsmg) )

if __name__ == "__main__":
    main()

