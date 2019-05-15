if __name__ == '__main__':
    filas = [250, 500, 750, 1000, 1500, 2000, 2500, 5000, 10000]
    columnas = [50, 100, 200, 400, 500, 1000]
    
    for fila in filas:
        for columna in columnas:
            c = int(input(str(fila)+'x'+str(columna)+': '))
            p = (c / fila) * 100
            print('%f%s\n' % (p, chr(37)))
