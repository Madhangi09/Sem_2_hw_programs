#number to roman
roman=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'X'),(5,'V'),(4,'IV'),(1,'I')]
n=int(input("Enter the number to convert:"))
ans=''
for val,letter in roman:
  while n>=val:
      ans+=letter
      n-=val
print("The roman value for the given integer is:",ans)
 
#roman to number
def roman_to_int(num):#CXX
    roman_value=[(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
    result=0
    for v,i in roman_value:#(100,C)
        while num.startswith(i):#
            result+=v#100
            num=num.removeprefix(i)#
    print(result)
roman_to_int("CXX")
