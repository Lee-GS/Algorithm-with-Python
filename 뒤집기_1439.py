s = input()

one_count = 0
zero_count = 0

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        continue
    else:
        if s[i] == "1":
            one_count+=1
        else:
            zero_count+=1
       
if one_count > zero_count:
    print(one_count)
elif one_count < zero_count:
    print(zero_count)
else:
    print(one_count)    
 
        
     