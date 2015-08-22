# -*- coding: utf-8 -*-
#7-5（部分功能没实现，有点摸不着头脑）

import time


db = {}
time1 = {}


def newuser():
    prompt = 'login desired: '
    while True :
        name = raw_input(prompt)
        if db.has_key(name) :
            prompt = 'name taken,try another:'
            continue
        else:
            break

    pwd = raw_input('passwd: ')
    db[name] = pwd
    time1[1] = time.time()
    choose()


def olduser():
    name = raw_input('login :').lower()
    pwd = raw_input('password:')
    passwd = db.get(name)
    if passwd == pwd:
        print 'welcome back', name
    else :
        print 'login incorrect'
    time1[len(time1)+1] = time.time()
    if time1[len(time1)] - time1[len(time1)-1] < 4 * 365 * 24 * 60 * 60：
        print ('last time you entered was at %f') % time1[len(time1)-1]
    choose()


def showmenu():
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit
Enter choice:"""

    done = False
    while not done:

        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError,KeyboardInterrupt):
                choice = 'q'
            print '\n you picked :[%s]' % choice
            if choice not in 'neq':
                print 'invalid option, try again'
            else:
                chosen = True

                if choice == 'q':
                    done = True
                if choice == 'n':
                    newuser()
                if choice == 'e':
                    olduser()


def manage():
    operation = raw_input('what do you want:')
    if operation == 'delete':
        key_delete = raw_input('which do you want to delete:')
        db.pop(key_delete)
    if operation == 'view':
        for name in db :
            print ('username: %s  password: %s') % (name,db[name])
    choose()


def choose():
    choice = raw_input ('please choose one model(user or manager):')
    if choice == 'user':
        showmenu()
    else:
        manage()


if __name__ == '__main__':
    choose()
