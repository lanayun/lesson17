lis = [1,2,3,4,5,-1,-2,0]
sum = 0
for i in lis:
    if not i==0:
        if not i <0:
            sum+=i
        else:
            pass
    else:
        break
print(sum)