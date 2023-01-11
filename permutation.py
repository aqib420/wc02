def permute(m, s, a):
    ''' 
    Returns YES if you can append several elements to the array
    a, that their sum equals S and the resultant array is a permutation. Returns NO 
    otherwise.

    Parameters:
    - m : Lenght of array a
    - s : Sum of missing numbers of permutation
    - a : Known numbers of permutation
    
    Constraints:
    - 1 <= m <= 100
    - 1 <= s <= 10000
    - 1 <= a_i <= 100
    '''
    s += sum(a)
    sm = 0
    for i in range(1, s + 1):
        sm += i
        if sm >= s:
            break
    if sm != s:
        return "NO"
    else:
        return "YES"

T = int(input())
f = []
for i in range(T):
    m,s = [int(i) for i in input().split()]   
    lst = [int(i) for i in input().split()]
    ans = permute(m,s,lst)
    print(ans)   
    f.append(ans)
