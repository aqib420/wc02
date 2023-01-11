input = '''5
2 48
3 1
4 27
3 6 2 5
7 10
3 1 5 4 7 6 2
2 2
1 3
5 67
3 1 5 7 6'''

with open('input1.txt', 'w') as f:
    f.write(input)

import os
import hashlib
def test_permute():
    os.system('python3 permutation.py <input1.txt >output.txt')
    with open('output.txt', 'r') as f:
        lines = f.readlines()
        output = ' '.join(map(str, [i.strip() for i in lines]))
    hash = hashlib.sha256(output.encode('utf-8')).hexdigest()
    assert hash == "15145b26951c9f20116bfbabcccf5754bd4770e3a47dcc46b5c644f37631b6bf"

test_permute()