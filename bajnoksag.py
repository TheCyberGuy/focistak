import math


class Csapat:
    def __init__(self, standing, name, win, draw, goal_in, goal_out, points):
        self.standing = standing
        self.name = name
        self.win = int(win)
        self.draw = int(draw)
        self.goal_in = int(goal_in)
        self.goal_out = int(goal_out)
        self.points = int(points)


csapatok = []


def feladat_1():
    with open('bajnoksag.csv', 'r', encoding='utf-8') as f:
        next(f)
        for line in f:
            data = line.split(';')
            # print(data)
            csapatok.append(
                Csapat(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
    print('beolvasas kesz')


def feladat_2():
    print('\n2. feladat')
    print(f'{len(csapatok)} csapat jatszott a bajnoksagban')


def feladat_3():
    print('\n3. feladat')
    csapat = input('adjon meg egy csapat nevet')
    # csapat = 'Athletic Bilbao'
    for i in csapatok:
        if i.name == csapat:
            print(f'a megadott csapat a {i.standing}. helyen all')


def feladat_4():
    print('\n4. feladat')
    golok = 0
    for i in csapatok:
        golok += i.goal_out
    print(f'osszesen {golok} golt rugtak')


def feladat_5():
    print('\n5. feladat')
    more_goal = []

    for i in csapatok:
        if i.goal_in > 60:
            more_goal.append(i.name)
    print(
        f'osszesen {len(more_goal)} csapat lott 60 golnal tobbet es ezek a kovetkezok:')
    print(', '.join(more_goal))


def feladat_6():
    print('\n6. feladat')
    goal_diff = {}
    for i in csapatok:
        goal_diff[i.name] = i.goal_in - i.goal_out
    biggest_diff = max(zip(goal_diff.values(), goal_diff.keys()))
    print(
        f'a legnagyobb gol diffenciaval rendelkezo csapat a {biggest_diff[1]} volt {biggest_diff[0]}-as kulonbseggel')


def feladat_7():
    avarage = {}

    for i in csapatok:
        matches = i.win + i.draw
        avarage[i.name] = [
            {math.ceil(i.goal_out/matches)}, {math.ceil(i.goal_in/matches)}]
    # print(avarage)
    with open('atlag.txt', 'w', encoding='utf-8') as f:
        f.write("Csapat nev; Atlag rugott; Atlag kapott\n")
        for i in avarage:
            f.write(f'{i};{avarage[i][0]};{avarage[i][1]}\n')


feladat_1()
feladat_2()
feladat_3()
feladat_4()
feladat_5()
feladat_6()
feladat_7()
