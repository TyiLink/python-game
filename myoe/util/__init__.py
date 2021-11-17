import myoe


def enter():
    try:
        input('Pressione <ENTER> para continuar...')
    except:
        print()
        return


def name_input():
    name = ''
    while not(0 < len(name) < 25) or ';' in name:
        myoe.gui.start_menu()
        name = input('Seu nome: ')
    return name


def opt_input(i):
    while True:
        try:
            myoe.gui.main_menu(i)
            opt = int(input('Escolha uma opção: '))
        except:
            print()
            continue
        else:
            return opt


def show_st(args):
    x = int(myoe.save.read_save(args))
    if x < 0:
        y = ' ' * 10
        return y
    elif 0 <= x <= 10:
        y = '█' * x + ' ' * (10 - x)
        return y
    else:
        y = '█' * 10
        return y
