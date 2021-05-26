s=input('enter the string : ')
count=0
for i in s:
  if i in 'aeiouAEIOU':
    count+=1
print('we have',count,'no of vowels in string',s)
