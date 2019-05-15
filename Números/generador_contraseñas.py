## Alejandro Mor Michael, Universidad Politécnica de Valencia (UPV)

#!/usr/bin/env/python
#! -*- encoding: utf8 -*-

from random import choices
from string import digits
from zlib import crc32
import pickle

if __name__ == '__main__':
    ps = []
    for i in range(1000):
        p = ''.join(choices(digits, k = 6))
        h = crc32(bytes(p, 'ascii'))
        ps.append(h)
        print('\n%d' % i)
        print('\nContraseña = %s' % p)
        print('Hash = %d\n' % h)

    with open('CONTRASEÑAS', 'wb') as fh:
        pickle.dump(ps, fh)
