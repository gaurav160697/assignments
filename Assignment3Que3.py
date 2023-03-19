s = "The quick Brow Fox"
u,l = 0,0
for i in s:
    if (i>='a'and i<='z'):
         
        
        u=u+1               
    if (i>='A'and i<='Z'):
         
        l=l+1
         
print('No. of lower case characters: ',l)
print('No. of upper case Characters: ',u)
