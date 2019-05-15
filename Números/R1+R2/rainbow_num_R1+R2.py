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

def r2(h):
    # Recodificación: a partir del hash actual, obtener una password en texto
    # Reconstrucción a una nueva contraseña, a partir del hash en hexadecimal:
    # Primero, eliminar los dos primeros caracteres del hash (0x)
    # Si el hash es de longitud mayor que 6, eliminar números desde el principio
    # Una vez obtenido un hash de longitud <= 6, los números se mantienen,
    # y las letras se cambian por el valor correspondiente a la media de
    # la suma de los números, uno a uno, del hash original
    
    r = list(hex(h))
    h = str(h)
    rr = -1

    del(r[0])
    del(r[0])
    while (len(r) > 6): del(r[0])
    
    for i in range(len(r)):
        if (r[i].isalpha()):
            r[i] = h[rr]
            rr -= 1
    
    r = ''.join(r)
    return r

if __name__ == '__main__':
    start = datetime.now()
    
    if (len(argv) > 2):
        # Tomando una tabla y un set de hashes aleatorios, comprobar cuántos
        # de estos hashes la tabla selecionada es capaz de romper
        P = argv[1]
        with open(P, 'rb') as fh:
            # lista de hashes a romper
            ps = pickle.load(fh)

        rT = argv[2]
        with open(rT, 'rb') as fh:
            # tabla del arcoiris
            rt = pickle.load(fh)
        
        # profundidad de la tabla
        pf = int(argv[3])
        # lista con los últimos hashes de la tabla
        hashes = list(rt.values())
        # número de colisiones encontradas en la tabla
        col = 0
        # lista con las contraseñas rotas
        cr = []
        for p in ps:
            aux = []
            print('\n\nContraseña a romper = %s' % p)
            """
            for k, v in rt.items():
                if ((v == p) and (v not in cr)):
                    aux.append(v)
            """
            if ((p in hashes) and (p not in cr)):
                aux = [v for v in hashes if v == p]

            print(aux)
            if (aux):
                col += 1
                print('\nCONTRASEÑAS ROTAS HASTA AHORA = %d' % col)
                cr += aux
            else:
                h = p
                for i in range(pf):
                    if (i % 2 == 0):
                        r = str(h % 1000000)

                    else:
                        r = r2(h)

                    h = crc32(bytes(r, 'ascii'))
                    if ((h in hashes) and (h not in cr)):
                        print('\nContraseña rota al %d intento en el bucle 1' % (i+1))
                        col += 1
                        aux = [v for v in hashes if v == h]
                        cr += aux
                        print('\nCONTRASEÑAS ROTAS HASTA AHORA = %d' % col)
                        break
                if (not aux):
                    h = p
                    for i in range(pf):
                        if (i % 2 == 0):
                            r = r2(h)

                        else:
                            r = str(h % 1000000)

                        h = crc32(bytes(r, 'ascii'))
                        if ((h in hashes) and (h not in cr)):
                            print('\nContraseña rota al %d intento en el bucle 2' % (i+1))
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
    # De momento, las contraseñas se actualizarán secuencialmente de la siguiente manera:
    # '000000' => '000001' => ... => '999999'
    rt = {}
    i = 0
    for p in product(digits, repeat = 6):
        i += 1
        p = ''.join(p)
        h = crc32(bytes(p, 'ascii'))
        
        for j in range(50): # profundidad de la tabla
            # En los pasos pares, la reconstrucción empleada será módulo 10^6
            if (j % 2 == 0):
                r = str(h % 1000000)
            # En los pasos impares, se reconstruirá empleando el método con el hash en hexadecimal
            else:
                r = r2(h)
            
            h = crc32(bytes(r, 'ascii'))
        
        print('\n\n%d' % i)
        print('\nContraseña actual = %s' % p)
        print('\nHash final = %s\n' % h)
        rt[p] = h
        if (i == 750): # número de filas de la tabla
            break

    # Guardado de la tabla en disco
    with open('TABLAS_R1+R2/RAINBOW_TABLE_NUM_R1+R2_750x50', 'wb') as fh:
        pickle.dump(rt, fh)
    col(rt)
    # El formato impreso es el siguiente:
    # Tiempo transcurrido = Horas:minutos:segundos.microsegundos
    print('\nTiempo transcurido = %s\n' % (datetime.now() - start))
    exit()
