def getlf(stri,index):
	last_lf = stri[index]
	last_lf_all = [i for i,val in enumerate(stri) if val == last_lf]
	last_lf_index = last_lf_all.index(index)
	sort_str = sorted(stri)
	first_lf_all = [i for i,val in enumerate(sort_str) if val == last_lf]
	res = first_lf_all[last_lf_index]
	return res

def bwmatching(last_col,pattern):
	top = 0
	bottom = len(last_col)-1
	while len(pattern)>0:
		symbol = pattern[-1]
		pattern = pattern[0:-1]
		occurences = []
		for i in range(top,bottom+1):
			if last_col[i]== symbol:
				occurences.append(i)
		if len(occurences)>0:
		    topIndex = occurences[0]
		    bottomIndex = occurences[-1]
		    top = getlf(last_col,topIndex)
		    bottom = getlf(last_col,bottomIndex)
		else:
			return 0
	return bottom-top+1

str_input = open('rosalind_ba9l.txt').read().strip()
last_col = str_input.split("\n")[0]
patterns = str_input.split("\n")[1]
patterns_arr = patterns.split(" ")
res = []
for pattern in patterns_arr:
	res.append(bwmatching(last_col,pattern))
for j in range(0,len(res)):
	if j==0:
		res_str = str(res[j])
	else:
		res_str+=" "+str(res[j])
print res_str
