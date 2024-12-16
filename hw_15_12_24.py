#1
def mergeStrings(word1,word2):
    result=[]
    i,j =0,0
    while i<len(word1) or j<len(word2):
        if i<len(word1):  
            result.append(word1[i])
            i+=1
        if j<len(word2): 
            result.append(word2[j])
            j+=1
    return''.join(result)
word1=input("Enter the first string (word1):")
word2=input("Enter the second string (word2):")
print("The merged string is:", mergeStrings(word1,word2))


#2
def canPlaceFlowers(flowerbed,n):
    count=0
    i=0
    length=len(flowerbed)
    while i<length:
        if flowerbed[i]==0:
            if (i==0 or flowerbed[i-1]==0) and (i==length-1 or flowerbed[i+1]==0):
                             flowerbed[i]=1
                count+=1
                if count>=n:
                    return True
                i+=1
        i+=1
    return count>=n
flowerbed_input=input("Enter the flowerbed array (0's and 1's) as a comma-separated list:")
flowerbed=list(map(int, flowerbed_input.split(',')))
int(input("Enter the number of flowers you want to plant (n):"))
result=canPlaceFlowers(flowerbed, n)
print(f"Can place {n} flowers? {result}")
