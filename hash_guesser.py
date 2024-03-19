import hashlib

hash_input = str(input('Enter hash:'))
wordlist = "wordlist2.txt"

with open(wordlist, 'r') as file:
    for line in file.readlines():
        hash_obj = hashlib.md5(line.strip().encode())
        hashed_pass = hash_obj.hexdigest()
        
        if hashed_pass == hash_input:
            print('Found cleartext string: ' + line.strip())
            exit(0)
