
# FILE INTEGRITY CHECKER 

import os
import hashlib

# FUNCTION TO EVALUATE HASH
def hash_file(file_path, algorithm='sha512'):
    hash_func = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hash_func.update(chunk)
    return hash_func.hexdigest()
# FUNCTION TO PEFORM HASH COMPARSION 
def check_file_integrity(original_hash, file_path):
    current_hash = hash_file(file_path)
    if original_hash == current_hash:
        print(f"[+] --- FILE IS INTACT --- ")
    else:
        print(f"[-] !!! FILE MODIFIED !!!")

if __name__ == "__main__":
    file_path = input("Enter the file path to check: ")
    original_hash = hash_file(file_path)
    print(f"Original file hash: {original_hash}")
    
    input("PRESS ENTER TO CHECK THE INTIGRITY OF THE FILE AFTER MODIFICATION")
    check_file_integrity(original_hash, file_path)