#Remember to give a full path of wordlist path
#created by Hasir Hamdan

import hashlib
print("*********************PASSWORD CRACKER**********************")

pass_found = 0
input_hash = input("Enter hashed password:")
pass_wordlist = input("\nEnter the wordlist path(full_path)\n")

try:
    passw = open(pass_wordlist , 'r')
except:
    print("Error, please give a correct path of wordlist")
    quit()

for word in passw:
    enc_word = word.encode('utf-8')
    hash_word = hashlib.md5(enc_word.strip())
    digest = hash_word.hexdigest()
    if digest == input_hash:
        print("your password found the password is", word)
        pass_found = 1
        break

if not pass_found:
       print("your password is not found in the",pass_wordlist,"file")


