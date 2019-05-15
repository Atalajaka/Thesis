#!/usr/bin/env python
#! -*- encoding: utf8 -*-

## Alejandro Mor Michael, Universidad Politécnica de Valencia (UPV)

from datetime import datetime
from zlib import crc32
from itertools import product
from string import digits
import pickle
from sys import argv, exit

def col(t):
    # Función de búsqueda de colisiones en la tabla
    # Crear un set, el cual no admite duplicados, cuyos elementos son los hashes obtenidos
    # El número de colisiones será igual a la diferencia entre el número de contraseñas
    # y el número de elementos del set

    u = set(t.values())
    print('\nContraseñas = %d' % (len(t)))
    print('\nÚnicos = %d' % (len(u)))
    print('\nColisiones en la tabla = %d\n' % (len(t) - len(u)))

if __name__ == '__main__':
    start = datetime.now()
    
    if (len(argv) > 2):
        # Tomando una tabla y un set de hashes aleatorios, comprobar cuántos
        # de estos hashes la tabla selecionada es capaz de romper
        P = argv[1]
        with open(P, 'rb') as fh:
            ps = pickle.load(fh)

        rT = argv[2]
        with open(rT, 'rb') as fh:
            rt = pickle.load(fh)

        pf = int(argv[3])
        hashes = list(rt.values())
        col = 0
        cr = []
        for p in ps:
            aux = []
            print('\n\nContraseña a romper = %s' % p)
            for k, v in rt.items():
                if ((v == p) and (v not in cr)):
                    aux.append(v)
            print(aux)
            if (aux):
                col += 1
                print('\nCONTRASEÑAS ROTAS HASTA AHORA = %d' % col)
                cr += aux
            else:
                h = p
                for i in range(pf):
                    r = bytes(str(h % 1000000), 'ascii')
                    h = crc32(r)
                    if ((h in hashes) and (h not in cr)):
                        print('\nContraseña rota al %d intento' % (i+1))
                        col += 1
                        aux = [v for v in hashes if v == h]
                        cr += aux
                        print('\nCONTRASEÑAS ROTAS HASTA AHORA = %d' % col)
                        break

        print('\n\n\nNúmero de contraseñas encontradas = %d' % col)
        print('\nPorcentaje de éxito = %.1f%s\n' % (((col/len(ps)) * 100), chr(37)))
        print('Tiempo transcurrido = %s\n' % (datetime.now() - start))
        exit()

    # La contraseña incial es '000000'
    # Las contraseñas se actualizarán secuencialmente de la siguiente manera:
    # '000000' => '000001' => ... => '999999'
    rt = {}
    i = 0
    for p in product(digits, repeat = 6):
        i += 1
        p = ''.join(p)
        h = crc32(bytes(p, 'ascii'))
        
        # Recodificación: a partir del hash actual, obtener una password en texto
        # Reconstrucción a una nueva contraseña = valor actual del hash % 10**6
        for j in range(1000): # profundidad de la tabla
            r = str(h % 1000000)
            h = crc32(bytes(r, 'ascii'))
        
        print('\n\n%d' % i)
        print('\nContraseña actual = %s' % p)
        print('\nHash final = %s\n' % h)
        rt[p] = h
        if (i == 1500): # número de filas de la tabla
            break

    # Guardado de la tabla en disco
    with open('TABLAS_M1/RAINBOW_TABLE_NUM_M1_1500x1.000', 'wb') as fh:
        pickle.dump(rt, fh)
    col(rt)
    # El formato impreso es el siguiente:
    # Tiempo transcurrido = Horas:minutos:segundos.microsegundos
    print('\nTiempo transcurido = %s\n' % (datetime.now() - start))
    exit()
