import rainbow_num_Hex_tester

if __name__ == '__main__':
    #filas = [250, 500, 750, 1000, 1500, 2000, 2500, 5000, 10000]
    #columnas = [50, 100, 200, 400, 500, 1000]

    for columna in [50, 100]:
        print('%d x %d' % (20000, columna))
        rainbow_num_Hex_tester.busq(20000, columna)

    for columna in [40, 100]:
        print('%d x %d' % (25000, columna))
        rainbow_num_Hex_tester.busq(25000, columna)

    for columna in [20, 50, 100]:
        print('%d x %d' % (50000, columna))
        rainbow_num_Hex_tester.busq(50000, columna)

    for columna in [10, 50, 100]:
        print('%d x %d' % (100000, columna))
        rainbow_num_Hex_tester.busq(100000, columna)

    for columna in [5]:
        print('%d x %d' % (200000, columna))
        rainbow_num_Hex_tester.busq(200000, columna)

    for columna in [4, 50, 100]:
        print('%d x %d' % (250000, columna))
        rainbow_num_Hex_tester.busq(250000, columna)

    for columna in [2, 50, 100]:
        print('%d x %d' % (500000, columna))
        rainbow_num_Hex_tester.busq(500000, columna)

    for columna in [1, 50, 100]:
        print('%d x %d' % (1000000, columna))
        rainbow_num_Hex_tester.busq(1000000, columna)
