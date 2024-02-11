import pickle
import os

users_file = 'users.bin'
def load_Users():
    if os.path.exists(users_file):
        with open(users_file, 'rb') as file:
            try:
                users = pickle.load(file)
            except EOFError:
                users = {}
    else:
        users = {}
    return users

def save_users(users):
    with open(users_file, 'wb') as file:
        pickle.dump(users, file)