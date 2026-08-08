def palindrome(r):
    a= len(r)-1
    b= 0
    while (a<b):
        if (r[a]!= r[b]):
            return False
        a+=1
        b-=1
    return True
r=(1,2,4,2,1,)    
if (palindrome(r)):
    print("Tuple is Flip-Flop")
else:
    print('Tuple is not a Flip- Flop.')    
    