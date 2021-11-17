import random
import myoe

rs = myoe.save.read_save
ws = myoe.save.write_save

while True:
# SAVE CHECK
    while not rs():
        myoe.save.create_save(myoe.util.name_input())
# TUTORIAL CHECK
    while rs(1) == 'False':
        for i in range(len(myoe.gui.hint)):
            myoe.gui.main_menu(i, myoe.gui.hint)
            myoe.util.enter()
        ws(1, 'True')
# DEATH CHECK
    sts = [(rs(3), 0), (rs(4), 1), (rs(5), 2), (rs(6), 3)]
    for i, n in sts:
        if not(0 < int(i) < 10):
            if int(i) <= 0:
                nn = 0
            else:
                nn = 1
            myoe.gui.death_menu(n, nn)
            myoe.save.del_save()
            myoe.util.enter()
            break
# CORE
    ran = random.randint(0, len(myoe.gui.opts) - 2)
    while rs():
        st1 = myoe.gui.opts[ran][5]
        st2 = myoe.gui.opts[ran][6]
        opt = myoe.util.opt_input(ran)
        if opt == 1:
            ws(st1[0], int(rs(st1[0])) + st1[1])
            ws(st2[0], int(rs(st2[0])) + st2[1])
            ws(2, int(rs(2)) + random.randint(15, 150))
            break
        elif opt == 2:
            ws(st1[0], int(rs(st1[0])) + st1[2])
            ws(st2[0], int(rs(st2[0])) + st2[2])
            ws(2, int(rs(2)) + random.randint(50, 250))
            break
        elif opt == 9:
            myoe.gui.start_menu()
            ws(0, myoe.util.name_input())
            break
        elif opt == 0:
            opt = myoe.util.opt_input(len(myoe.gui.opts) - 1)
            while True:
                if opt == 1:
                    myoe.save.del_save()
                    break
                elif opt == 2:
                    break
                else:
                    opt = myoe.util.opt_input(len(myoe.gui.opts) - 1)
        else:
            opt = myoe.util.opt_input(ran)
