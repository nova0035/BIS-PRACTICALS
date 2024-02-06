all_chars = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plaintext : str,key : int) -> str:

    plaintext = plaintext.lower()

    cypher_Text = ""

    for i in plaintext:
  
        cypher_Text += all_chars[(all_chars.index(i) + key) % 26]
    
    return cypher_Text

def decrypt(cypherText : str,key : int) -> str:

    cypherText = cypherText.lower()

    plain_Text = ""

    for i in cypherText:

        plain_Text += all_chars[(all_chars.index(i) - key) % 26]

    return plain_Text

print("Encrypted Text : " + encrypt("hello",34))
print("Decrypted Text : " + decrypt("pmttw",34))

"""
output 
Encrypted Text : pmttw
Decrypted Text : hello
"""
