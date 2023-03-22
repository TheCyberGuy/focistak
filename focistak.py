import datetime

class Focista():
    def __init__(self, name, team, born,salary):
        self.name = name
        self.team =team
        self.born = born
        self.salary = salary

focistak = []


def feladat_1():
    with open('focistak.txt', 'r', encoding='utf-8') as f:
        next(f)
        for line in f:
            data = line.split(';')
            focistak.append(Focista(team=data[1], name=data[0], born=int(data[2]), salary=data[3])) 

def feladat_2():
    print(f'{focistak[0].name} fizetes: {focistak[0].salary}')
    print(f'{focistak[-1].name} fizetes: {focistak[-1].salary}')

def feladat_3():
    year =  datetime.datetime.now().year
    eletkorok = {}
    for index, obj in enumerate(focistak):
        eletkorok[f'{obj.name}'] = year - obj.born
    eletkorok = dict(sorted(eletkorok.items(), key=lambda item: item[1]))
    # print(eletkorok)
    korok = []
    for index, keys in enumerate(eletkorok):
        if index == 0:
            print(f'\n{keys}: {eletkorok[keys]} a legfiatalabb\n')
            korok.append(eletkorok[keys])
        if index == len(eletkorok) -1:
            korok.append(eletkorok[keys])
    #! 4. feladat
    print(f'a kor kulonbseg: {korok[1] - korok[0]} a kor kulonbseg')       

def feladat_5():
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
    pass

feladat_1()
feladat_2()
feladat_3()
feladat_5()