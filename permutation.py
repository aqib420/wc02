# import ipdb; 
# ipdb.set_trace()
def permute(m, s, a):
    ''' 
    Returns YES if you can append several elements to the array
    a, that their sum equals S and the resultant array is a permutation. Returns NO 
    otherwise.

    Parameters:
    - m : Length of array a
    - s : Sum of missing numbers of permutation
    - a : Known numbers of permutation
    
    Constraints:
    - 1 <= m <= 100
    - 1 <= s <= 10000
    - 1 <= a_i <= 100
    '''
    pass
    # m = int(input())
    # s= int(input())
    # a= int(input())
    

    lst=[]
    for i in range(1,100):
        lst.append(i)
    for j in a:
        if j in lst:
            lst.remove(j)
        
    
    for i in range(len(lst)):
        if s>0:
            s=s-lst[i]
            a.append(lst[i])
        
    # for i in range(len(lst)):
    #     while s>0:
    #         s=s-lst[i]
    #         a.append(lst[i])
    if s!=0:
        return("NO")
    else:
        return ("YES")





# print(permute(m,s,a))
