rows=int(input())
cols=int(input())
for i in range(rows):
    if i < 2:
        print("+")
    elif i < 4:
        print("+        +")
    else:
        print("+" * cols)
    
