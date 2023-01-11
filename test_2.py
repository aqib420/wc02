input = '''20
3 30
6 3 4
1 1
2
16 14
3 20 12 19 18 14 17 11 13 10 4 9 16 15 7 8
9 83
7 5 1 18 16 3 13 14 11
7 189
1 6 18 9 5 19 17
6 183
14 16 12 6 5 10
8 85
6 7 3 11 2 12 1 4
11 109
7 18 12 16 10 11 3 13 9 1 15
12 344
2 4 15 6 10 9 1 5 20 11 14 19
10 57
12 14 15 9 1 4 5 3 16 17
2 6
2 1
7 113
14 6 2 13 4 15 1
2 9
1 5
7 37
6 8 10 1 3 4 2
6 27
5 7 6 8 9 1
7 129
12 11 17 5 7 2 15
6 91
4 8 5 10 3 6
11 90
20 8 14 4 13 11 19 12 15 3 1
8 38
3 1 8 10 4 5 9 13
2 7
3 2'''

with open('input2.txt', 'w') as f:
    f.write(input)

import os
import hashlib
def test_permute():
    os.system('python3 permutation.py <input2.txt >output.txt')
    with open('output.txt', 'r') as f:
        lines = f.readlines()
        output = ' '.join(map(str, [i.strip() for i in lines]))
    hash = hashlib.sha256(output.encode('utf-8')).hexdigest()
    assert hash == "9e0503c4df9870ff65c857d0c45fbf456ee5b85510200aca9b651f4171832d34"

test_permute()