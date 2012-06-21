phrase=raw_input("Enter sentence to encrypt: ")
shift=input('Enter shift value: ')
encoded_phrase = ''
for c in phrase:
    if (ord(c)>64 and ord(c)<91):
        asc=ord(c)
        alph_asc=asc-65
        shift_asc=(alph_asc+shift)%26
        enc_asc=shift_asc+65
        encoded_phrase = encoded_phrase + chr(enc_asc)
    elif (ord(c)>96 and ord(c)<123):
        asc=ord(c)
        alph_asc=asc-97
        shift_asc=(alph_asc+shift)%26
        enc_asc=shift_asc+97
        encoded_phrase = encoded_phrase + chr(enc_asc)
    else:
        encoded_phrase = encoded_phrase+c
    
print encoded_phrase
