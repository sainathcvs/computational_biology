str1="PRETTY"
str2="PRTTEIN"
final_str=''
editDistance=0
length_min = min(len(str1),len(str2))
if length_min==len(str1):
	min_str = str1
	max_str = str2
else:
	min_str = str2
	max_str = str1
	
for i in range(0,length_min):
    tmp_str=min_str[i]
    if tmp_str==max_str[i] :
        max_str=max_str[i: ]
        final_str+=tmp_str
    elif tmp_str != max_str[i] and max_str.count(tmp_str)>1:
        max_str=max_str[max_str.index(tmp_str): ]
        final_str += tmp_str
        editDistance += 1
    elif tmp_str!=max_str[i] and max_str.count(tmp_str)==0:
        max_str=max_str[i: ]
        final_str += tmp_str
        editDistance += 1
print editDistance