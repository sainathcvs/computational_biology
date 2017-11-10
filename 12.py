def countsymbol(symbol,within,last_col):
	last_col_str = last_col[:within]
	return last_col_str.count(symbol)

def first_occurence_symbol(symbol,first_col):
	return first_col.index(symbol)

def better_bwmatching(last_col,pattern,first_col):
	top = 0
	bottom = len(last_col)-1
	while len(pattern)>0:
		symbol = pattern[-1]
		pattern = pattern[0:-1]
		is_present = False
		for i in range(top,bottom+1):
			if last_col[i]== symbol:
				is_present = True
				break
		if is_present:
		    top = first_occurence_symbol(symbol,first_col)+countsymbol(symbol,top,last_col)
		    bottom = first_occurence_symbol(symbol,first_col)+countsymbol(symbol,bottom+1,last_col)-1
		else:
			return 0
	return bottom-top+1

str_input = open('rosalind_ba9m.txt').read().strip()
last_col = str_input.split("\n")[0]
patterns = str_input.split("\n")[1]
patterns_arr = patterns.split(" ")
first_col = sorted(last_col)
res = []
for pattern in patterns_arr:
	res.append(better_bwmatching(last_col,pattern,first_col))
for j in range(0,len(res)):
	if j==0:
		res_str = str(res[j])
	else:
		res_str+=" "+str(res[j])
print res_str
