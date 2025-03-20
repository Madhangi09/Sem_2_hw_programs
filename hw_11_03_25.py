def pattern(n):
    result=["1"]
    for _ in range(n):
        print(" ".join(result))  # Print the current sequence
        new_result=[]
        i=0
        while i<len(result):
            count=1
            while i+1<len(result) and result[i]==result[i+1]:
                count+=1
                i+=1
            new_result.append(str(count))
            new_result.append(result[i])
            i+=1
        result=new_result  
n=5
pattern(n)










