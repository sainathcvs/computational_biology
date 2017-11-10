import re
dna_string_input_raw = open('rosalind_mgap.txt').readlines()
str_array = []


def format_input_file():
    strings_arr = {}
    label_strip = None
    for ctr in range(len(dna_string_input_raw)):
        if re.match('>', dna_string_input_raw[ctr]):
            if ctr != 0:
                str_array.append(strings_arr[label_strip])
            label_strip = dna_string_input_raw[ctr].strip('\n >')
            if ctr != 0:
                str_array.append("" + label_strip)
            if ctr == 0:
                str_array.append("" + label_strip)
            strings_arr[label_strip] = ''
        else:
            strings_arr[label_strip] += dna_string_input_raw[ctr].strip()
    str_array.append(strings_arr[label_strip])
    return str_array


dna_string_input = format_input_file()
str1=dna_string_input[1]
str2=dna_string_input[3]

lc=[]
lc = [[0 for j in range(0,len(str2)+1)] for i in range(0,len(str1)+1)]

for i in range(0,len(str1)+1):
	for j in range(0,len(str2)+1):
		if i==0 or j==0:
			lc[i][j] = 0
		elif str1[i-1]==str2[j-1]:
			lc[i][j] = 1+lc[i-1][j-1]
		else:
			lc[i][j] = max(lc[i-1][j],lc[i][j-1])

gap_n = 2*lc[len(str1)][len(str2)]
print len(str1)+len(str2)-gap_n