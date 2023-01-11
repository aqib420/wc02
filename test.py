import permutation
import pytest
import random as rd
rd.seed(0)
tests = list()
tests1 = list()
# with open("test.txt","w") as f:

#     for t in range(1000):
#         n = rd.randint(1, 50)
#         s = 0
#         lst = []
#         ans = []
#         for i in range(1, n+1):
#             ans.append(i)
#             if rd.random() > 0.7:
#                 s += i
#             else:
#                 lst.append(i)
#         rd.shuffle(lst)
#         if lst != [] and s>0:
#             tests.append((
#                 str(len(lst))+' '+str(s),
#                 ' '.join(map(str, lst)),
#                 ' '.join(map(str, ans))
#             ))
#             f.write(str(len(lst))+' '+str(s)+'\t')
#             f.write(' '.join(map(str, lst))+'\t')
#             f.write(' '.join(map(str, ans))+'\n')
with open("test.txt","r") as f:
    data = f.read().strip().split("\n")
    for d in data:
        tests1.append(d.strip().split("\t"))
        # n,s = map(int,new[0].split(" "))
        # print(n,s)
        # print(new[1])

@pytest.mark.parametrize("ns,a,final", tests1)
def test_permute(ns,a,final):
    input_values = [ns, a]
    output = []

    def mock_input():
        return input_values.pop(0)
    permutation.input = mock_input
    permutation.print = lambda s: output.append(s)

    out = permutation.permute()
    print(out)

    assert sorted(out) == list(map(int,final.split(" ")))

 