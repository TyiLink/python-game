import os


def create_save(x):
    default_save = f'{x};False;0;5;5;5;5'
    try:
        f = open('save.json', 'x')
    except:
        try:
            f = open('save.json', 'w')
        except:
            return
        else:
            f.write(default_save)
            f.close()
    else:
        f.write(default_save)
        f.close()


def del_save():
    os.remove('save.json')


def read_save(x = -1):
    try:
        f = open('save.json', 'r')
    except:
        return False
    else:
        if x == -1:
            with open('save.json', 'r') as f:
                if not f.read(1):     
                    return False
                else:
                    return True
        else:
            for args in f:
                info = args.split(';')
                return info[x]
        f.close()


def write_save(x, y):
    try:
        f = open('save.json', 'r')
    except:
        return
    else:
        for args in f:
            old_save = args.split(';')
        old_save[x] = y
        new_save = ''
        for i in old_save:
            new_save += f'{i};'
        f.close()
        try:
            f = open('save.json', 'w')
        except:
            return
        else:
            f.write(new_save[:-1])
            f.close()
