from User import User
import re
import os


class Authentication:
    __users = []

    def __int__(self):
        # self.fname = None
        # self.lname = None
        # self.email = None
        # self.password = None
        # self.phone = None
        pass

    @staticmethod
    def register():
        Authentication.fname = input("Enter first name: ")
        while len(Authentication.fname) < 1 or not Authentication.fname.isalpha():
            Authentication.fname = input("Enter first name: ")

        Authentication.lname = input("Enter last name: ")
        while len(Authentication.lname) < 1 or not Authentication.lname.isalpha():
            Authentication.lname = input("Enter last name: ")

        Authentication.email = input("Enter email: ")
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        while len(Authentication.email) < 1 or not re.match(email_pattern, Authentication.email):
            Authentication.email = input("Enter email: ")

        Authentication.password = input("Enter password: ")
        while len(Authentication.password) < 1:
            Authentication.password = input("Enter password: ")
        phone_pattern = r"^01[0125][0-9]{8}$"

        Authentication.phone = input("Enter phone: ")
        while len(Authentication.phone) < 1 or not re.match(phone_pattern, Authentication.phone):
            Authentication.phone = input("Enter phone: ")

        user = User(Authentication.fname, Authentication.lname, Authentication.email, Authentication.password,
                    Authentication.phone)
        try:
            Authentication.save(user)
            return f"Account successfully registered"
        except Exception as e:
            return e

    @staticmethod
    def save(user):
        Authentication.load()
        users = Authentication.__users
        for record in users:
            if record.email == user.email:
                raise Exception(f"Email {user.email} already exists!")
        filepath = "users.txt"
        with open(filepath, 'a') as file:
            file.write(f"{user.email};{user.password};{user.fname};{user.lname};{user.phone}\n")

    @staticmethod
    def load():
        filepath = "users.txt"
        if not os.path.exists(filepath):
            f = open(filepath, 'w')
            f.close()
        else:
            file = open(filepath, 'r')
            file_parse = file.read()
            file.close()
            for line in file_parse.split("\n"):
                if line:
                    split = line.split(';')
                    usr = User(email=split[0], password=split[1],
                               fname=split[2], lname=split[3], phone=split[4])
                    Authentication.__users.append(usr)

    @staticmethod
    def login(email, password):
        Authentication.load()
        users = Authentication.__users
        for usr in users:
            if usr.email == email and usr.password == password:
                return usr
        raise Exception("Wrong Email or Password! Please try again")
