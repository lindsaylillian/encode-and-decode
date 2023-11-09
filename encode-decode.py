# encode-and-decode
alphabet= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z''a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z''a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z''a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z''a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("TYPE decode or encode\n")
text=input("what text is it ").lower()
shift=int(input("type the shift number"))


def encrypt(plain_text,shift_amount): 
    ciphertext = ""    
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position=position + shift_amount
        new_letter=alphabet[new_position]
        ciphertext += new_letter
    print(f"the encoded is {ciphertext}")


def decrypt(cipher_text,shift_amount):
    
    plain_text = ""    
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position=position - shift_amount
        new_letter=alphabet[new_position]
        plain_text += new_letter
    print(f"the decoded is {plain_text}")

if direction=="encode":
    encrypt(plain_text=text,shift_amount=shift)
elif direction=="decode":
    decrypt(cipher_text=text,shift_amount=shift)
