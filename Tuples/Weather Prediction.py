Weather= (1,0,1,0,1,0,1)

sunny=0
rainy=0

for i in range(0,7):
    if Weather[i]==0:
        rainy+=1
    else:
        sunny+=1

if (sunny > rainy):
    print("It is a good weather.")  
else:
    print("It is a bad Weather.")              