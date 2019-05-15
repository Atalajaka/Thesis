## Alejandro Mor Michael, Universidad Politécnica de Valencia (UPV)

#!/usr/bin/env python
#! -*- encoding: utf8 -*-

import pickle
from sys import argv

if __name__ == '__main__':
    V = argv[1]
    with open(V, 'rb') as fh:
        v = pickle.load(fh)
    i = 1
    for p in v:
        print('\nItem %d = %s' % (i, p))
        i += 1
