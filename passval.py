import re
s = input(" Enter the password that contains \n At least 8 characters \n A mixture of both uppercase and lowercase letters \n A mixture of digits \n Inclusion of at least one special character from the following @, $, _) \n ")
l, u, p, d = 0, 0, 0, 0
if(len(s)>=8):
    for i in s:
        if(i.islower()):
            l+=1
        
        if(i.isupper()):
            u+=1

        if(i.isdigit()):
            d+=1
        
        if(i=='@' or i=='$' or i=='_' ):
            p+=1

if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
    print('VALID PASSWORD')
else:
    print('INVALID PASSWORD')