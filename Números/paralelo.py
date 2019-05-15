#!/usr/bin/env python
#! -*- encoding: utf8 -*-

## Alejandro Mor Michael, Universidad Politécnica de Valencia (UPV)

from datetime import datetime
from zlib import crc32
from itertools import product
from multiprocessing.pool import Pool
from string import digits, ascii_lowercase
import pickle
from sys import argv, exit

def col(t):
    # Función de búsqueda de colisiones en la tabla
    # Obtener primero los hashes de la tabla, los cuales son los valores de cada entrada del diccionario
    # A continuación, revertir el diccionario, poniendo como claves los hashes, 
    # y como valores las contraseñas que comparten el hash final
    # Después, se obtiene una lista cuyos elementos son tuplas de contraseñas con el mismo hash final
    # Colisiones = número total de elementos de dicha lista

    rev_t = {}
    for k, v in t.items():
        rev_t.setdefault(v, set()).add(k)

    l = [v for k, v in rev_t.items() if len(v) > 1]
    ##print(rev_t)
    c = 0
    for x in l:
        print('\nColisión:')
        for p in x:
            print('%s' % p)
            c += 1

    print('\nColisiones en la tabla = %d\n' % c)

def tabla_R1 (p):
    p = ''.join(p)
    h = crc32(bytes(p, 'ascii'))
    # Recodificación: a partir del hash actual, obtener una password en texto
    # Reconstrucción a una nueva contraseña = valor actual del hash % 10**6
    for j in range(1000): # profundidad de la tabla
        r = bytes(str(h % 1000000), 'ascii')
        h = crc32(r)
    return (p, h)

if __name__ == '__main__':
    start = datetime.now()
    
    if (len(argv) == 2):
        # Búsqueda de la contraseña, tan sólo trata de encontrarla en la tabla actual
        # Cargado de la tabla desde disco
        rT = argv[1]
        with open(rT, 'rb') as fh:
            rt = pickle.load(fh)
        ##print('\n')
        ##print(rt)
        ##print('\n')
        p = int(open('current_password.txt', 'r').read())
        # Bucle de búsqueda de la contraseña
        for k, v in rt.items():
            if (v == p):
                print('\nContraseña encontrada = %s' % k)
                print('\nTiempo transcurrido = %s segundos\n' % (datetime.now() - start))
                exit()

        print('\nLa contraseña no ha sido encontrada\n')
        print('\nTiempo transcurrido = %s\n' % (datetime.now() - start))
        exit()
    
    if (len(argv) > 2):
        # Tomando una tabla y un set de hashes aleatorios, comprobar cuántos
        # de estos hashes la tabla selecionada es capaz de romper
        P = argv[1]
        with open(P, 'rb') as fh:
            ps = pickle.load(fh)

        rT = argv[2]
        with open(rT, 'rb') as fh:
            rt = pickle.load(fh)
        
        col = 0
        cr = []
        for p in ps:
            aux = []
            print('\n\nContraseña a romper = %s' % p)
            for k, v in rt.items():
                if (v == p):
                    aux.append(k)
                    print('\nContraseña rota = %s' % k)
            if (aux):
                col += 1
                cr += aux
        print('\n\nNúmero de contraseñas encontradas = %d\n' % col)
        print('\nContraseñas rotas =')
        print(sorted(cr))
        print('\nLongitud = %d' % len(cr))
        print('\nÚnicos = %d' % len(set(cr)))
        print('\nPorcentaje de éxito = %.2f%s\n' % (((col/len(ps)) * 100), chr(37)))
        print('Tiempo transcurrido = %s\n' % (datetime.now() - start))
        exit()

    # La contraseña incial es '000000'
    # De momento, las contraseñas se actualizarán secuencialmente de la siguiente manera:
    # '000000' => '000001' => ... => '999999'
    rt = {}
    i = 0
    with Pool(2) as pool:
        for p, h in pool.imap_unordered(tabla_R1, product(digits, repeat = 6)):
            i += 1
            print('\n\n%d' % i)
            print('\nContraseña actual = %s' % p)
            print('\nHash final = %s\n' % h)
            rt[p] = h
            if (i == 1000): # número de filas de la tabla
                break

    print('\nTabla del arcoiris obtenida =\n')
    print(rt)
    print('\n')
    f = open('current_password.txt', 'w')
    f.write(str(h))
    f.close()
    # Guardado de la tabla en disco
    with open('TABLA_TEST_R1', 'wb') as fh:
        pickle.dump(rt, fh)
    col(rt)
    # El formato impreso es el siguiente:
    # Tiempo transcurrido = Horas:minutos:segundos.microsegundos
    print('\nTiempo transcurido = %s\n' % (datetime.now() - start))
    exit()
