import datetime


class Focista():
    def __init__(self, name, team, born, salary):
        self.name = name
        self.team = team
        self.born = born
        self.salary = salary


focistak = []


def feladat_1():
    # print('\n1. feladat')
    with open('focistak.txt', 'r', encoding='utf-8') as f:
        next(f)
        for line in f:
            data = line.split(';')
            focistak.append(
                Focista(team=data[1], name=data[0], born=int(data[2]), salary=data[3]))


def feladat_2():
    print('\n2. feladat')
    print(f'{focistak[0].name} fizetes: {focistak[0].salary}')
    print(f'{focistak[-1].name} fizetes: {focistak[-1].salary}')


def feladat_3():
    print('\n3. feladat')
    year = datetime.datetime.now().year
    eletkorok = {}
    for index, obj in enumerate(focistak):
        eletkorok[f'{obj.name}'] = year - obj.born
    eletkorok = dict(sorted(eletkorok.items(), key=lambda item: item[1]))
    # print(eletkorok)
    korok = []
    for index, keys in enumerate(eletkorok):
        if index == 0:
            print(f'{keys}: {eletkorok[keys]} a legfiatalabb\n')
            korok.append(eletkorok[keys])
        if index == len(eletkorok) - 1:
            korok.append(eletkorok[keys])
    #! 4. feladat
    print('\n4. feladat')
    print(f'a kor kulonbseg: {korok[1] - korok[0]} ev')


def feladat_5():
    print('\n5. feladat')
    talalat = []
    csapatnev = input('adjon meg egy csapat nevet: ')
    for i in focistak:
        if i.team == csapatnev:
            talalat.append(i.name)
    if len(talalat) > 0:
        print(f'a {csapatnev}ben/ban ok jatszanak:')
        for i in talalat:
            print(i, end=', ')
    else:
        print('nincs ilyen csapat vagy nem jatszik ilyen nevu jatekos')


def feladat_6():
    print('\n6. feladat')
    csapatok = {}

    for i in focistak:
        if i.team not in csapatok:
            csapatok[i.team] = 1
        else:
            csapatok[i.team] += 1
    for keys in csapatok:
        if csapatok[keys] > 1:
            print(f'{keys}: {csapatok[keys]} jatekos jatszik a listabol')


def feladat_7():
    print('\n7. feladat')
    oregek = {}
    for i in focistak:
        if i.born < 2000:
            oregek[i.name] = f'{i.born} {i.team}'
    print(oregek)

    with open('oregek.txt', 'w', encoding='utf-8') as f:
        for key in oregek:
            f.write(f'{key}: {", ".join(oregek[key].split(" "))}\n')


feladat_1()
feladat_2()
feladat_3()
feladat_5()
feladat_6()
feladat_7()
