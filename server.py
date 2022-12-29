import socket
import threading
import random
import pickle


host = '127.0.0.1'
port = 5116

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(2)

user_1, addr_1 = server.accept()
user_2, addr_2 = server.accept()

# def connected():
#     nicks = []
#     clients = []
#     client, adress = server.accept()
#     nick = client.recv(1024).decode('utf-8')
#     nicks.append(nick)
#     clients.append(client)
#     print(nicks, clients)


def choose_letters_for_game():
    letters_list = ['Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ', 'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л',
                    'Д', 'Ж', 'Э', 'Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю', 'Ё']
    letters = []
    positions = []
    game_lst = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                '', '', '', '', '', '', '', '', '', '']

    while len(letters) != 36:
        letter = random.choice(letters_list)
        if letter not in letters:
            letters.append(letter)
            letters.append(letter)

    while len(positions) != 36:
        pos = random.randint(0, 35)
        if pos not in positions:
            positions.append(pos)

    for el in positions:

        game_lst[el] = letters[0]
        letters.pop(0)
    return game_lst

# lst = choose_letters_for_game()
# n = int(user_1.recv(1024).decode('utf-8'))
# e = lst[n]
# user_1.send(e).encode('utf-8')
#
# print(lst)


