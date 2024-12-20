roman=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'X'),(5,'V'),(4,'IV'),(1,'I')]
n=int(input("Enter the number to convert:"))
ans=''
for val,letter in roman:
  while n>=val:
      ans+=letter
      n-=val
print("The roman value for the given integer is:",ans)
 
