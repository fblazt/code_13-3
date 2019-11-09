import re

def username(username):
    if  re.match(r"[a-z]{5}", username) :
        print("Username (\"" + username + "\")")
        print(bool(True))
    else :
        print("Username (\"" + username + "\")")
        print(bool(False))

def password(password):
    if re.match(r"(?<![0-9])[0-9]{2}(?![0-9])([@&])(?<![A-Z])[A-Z]{4}(?![A-Z])", password) :
        print("Password (\"" + password + "\")")
        print(bool(True))
    else :
        print("Password (\"" + password + "\")")
        print(bool(False))

username("firman")
password("223@HKGJ")
