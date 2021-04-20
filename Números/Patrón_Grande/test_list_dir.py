from os import walk
from sys import argv, exit
import rainbow_num_Patrón_Grande_tester
import pickle

def get_tablas():
    files = []
    tablas = []

    for (dirpath, dirnames, filenames)in walk('TABLAS_Patrón_Grande/'):
        files.extend(filenames)
        break

    for f in files:
        fila = f[f.rfind('_')+1:f.find('x')]
        columna = f[f.find('x')+1:]
        print('Fila = %s, columna = %s\n' % (fila, columna))
        tablas.append((fila, columna))

    print(tablas)
    with open ('TABLAS_LISTA', 'wb') as fh:
        pickle.dump(tablas, fh)

def exec_tablas():
    T = 'TABLAS_LISTA'
    with open (T, 'rb') as fh:
        tablas = pickle.load(fh)

    for t in tablas:
        rainbow_num_Patrón_Grande_tester.busq(t[0], t[1])

if __name__ == "__main__":

    if len(argv) == 1:
        print('No argument selected\nUse arg GET to get all tables available\nUse arg TEST to test all tables previously gotten')
        exit()

    if argv[1] == "GET":
        get_tablas()

    elif argv[1] == "TEST":
        exec_tablas()
