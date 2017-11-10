str_input = open('rosalind_ba9k.txt').read().strip()
stri = str_input.split("\n")[0]
index = int(str_input.split("\n")[1])
last_lf = stri[index]
last_lf_all = [i for i,val in enumerate(stri) if val == last_lf]
last_lf_index = last_lf_all.index(index)
sort_str = sorted(stri)
first_lf_all = [i for i,val in enumerate(sort_str) if val == last_lf]#sort_str.index(last_lf)
res = first_lf_all[last_lf_index]
print res
