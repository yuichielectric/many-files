#!/usr/local/bin/python3

import os
import random
import string

for i in range(1, 11):
    for j in range(1, 11):
        path = '%d/%d' % (i, j)
        os.makedirs(path)
        for k in range(1, 101):
            file_path = path + ('/%d' % k)
            with open(file_path, 'w') as f:
                f.write(''.join(random.choices(string.ascii_letters + string.digits, k=(30 * 1024))))
