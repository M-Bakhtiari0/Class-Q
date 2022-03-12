import re, hashlib

class Account:

    def __init__(self, username, password, phonenumber, email):
        self.username = input('enter username: ')
        self.password = check_password(password)
        self.phone = check_phonenumber(phonenumber)
        self.email = input('enter email: ')

    @staticmethod
    def _check_username(username):
        if not re.search("^\w+_\w+$",username):
            raise Exception('invalid username')
        
        return username


    @staticmethod
    def _check_email(email):
        if not re.search("([A-Za-z0-9]+[.-_])+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,5})+",email):
            raise Exception('invalid email')
        
        return email


    @classmethod
    def check_password(cls, password):
        if not all([re.search("[a-z]|[A-Z]+[0-9]\d{1}$", password) and len(password) >= 8]):
            raise Exception('invalid password')
        encoded = password.encode('utf-8')
        
        return hashlib.sha256(encoded)

    @classmethod
    def check_phonenumber(cls, phonenumber):
        if not (re.search("^((\+989)|(09))+[0-3,9]\d{8}$", phonenumber)):
            raise Exception('invalid phone number')
        
        return phonenumber

    #salam ostad vaghteton bekheir 
    # moteasefane man felan faghat ta inja vaght kardam pish beram chon ghesmat regex ro 
    # moshkel dashtam va az bache ha ham komak gereftam 