import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json','r',encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user['username'], password = user['password'], email = user['email'])
                    self.users.append(newUser)
            print(self.users)

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print('User is created!')

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('Successfully Logged In')
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Çıkış yapıldı.')

    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print('giriş yapılmadı.')

    def savetoFile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__)) #allow us to alter user class to a dictionary

        with open('users.json','w') as file:
            json.dump(list, file) #we can only dump dicts so we need to use __dict__  to our User class


repository = UserRepository()

while True:
    print('Menu'.center(50,'*'))
    option = input('1- Register\n2- Login\n3- Logout\n4- identity\n5- Exit\nWhat would you like to do: ')
    if option == '5':
        break
    else:
        if option == '1':
            username = input('username: ')
            password = input('password: ')
            email = input('email: ')

            user = User(username=username, password = password, email = email)
            repository.register(user)
        elif option == '2':
            if repository.isLoggedIn:
                print('You have already logged in')
            else:
                username = input('username: ')
                password = input('password: ')
                repository.login(username, password)
        elif option == '3':
            repository.logout()
        elif option == '4':
            repository.identity()
        else:
            print('Invalid Option')
