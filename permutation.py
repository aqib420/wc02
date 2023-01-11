def permute():
    ''' 
    Returns the permutation if you can append several elements to the array
    a, that their sum equals S and the result will be a permutation. Return NO 
    otherwise.

    Parameters:
    - None
    
    Constraints:
    - 1 <= m <=50
    - 1 <= S <=1000
    - 1 <= a_i <= 50
    '''

    n, s = map(int, input().split())
    a = [int(x) for x in input().split()]
    s += sum(a)
    sm = 0
    cnt = 0
    new = []
    for i in range(1, s + 1):
        if sm >= s:
            break
        sm += i
        
        new.append(i)
        cnt = i
    if sm != s or max(a) > cnt or cnt <= n:
        return "NO"
    else:
        return new
if __name__ == "__main__":
    permute()
        
