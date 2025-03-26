def canPlaceFlowers(flowerbed,n):
    flowerbed=[0]+flowerbed+[0]  # Add padding to handle edge cases
    count=0
    for i in range(1,len(flowerbed)-1):
        if flowerbed[i-1]==flowerbed[i]==flowerbed[i+1]==0:
            flowerbed[i]=1  # Plant a flower
            count+=1
            if count>=n:
                return True
    return count>=n
print(canPlaceFlowers([1,0,0,0,1],1))  
print(canPlaceFlowers([1,0,0,0,1],2))  
