import re
dna_string_input_raw = open('/home/cvs/PycharmProjects/sampleg/rosalind_grp.txt').readlines()
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
    # print(str(len(str_array)))
    print(strings_arr[label_strip])
    return str_array


dna_string_input = format_input_file()
# print(str_array)
key_arr = []
protein_string_arr = []
string_dict = {}
for ct in range(0, len(dna_string_input)-1, 2):
    key_arr.append(str_array[ct].split("\r")[0])
    # print(key_arr)
    tmp = ct
    j = tmp+1
    protein_string_arr.append(str_array[j])
    key_tmp = str_array[ct].split("\r")[0]
    # print(key_tmp+"---"+str_array[j])
    string_dict[key_tmp] = str_array[j]

print(string_dict)


file1 = open('output_7.txt', 'w')
total_protein_num = string_dict.__len__()
final_str = ""
while len(protein_string_arr)>0:
    for label_str, protein_str in string_dict.items():
        for i in range(total_protein_num, 0, -1):
            print(str_array[:i])
            if protein_str.endswith(str_array[0][:i]):
                final_str = protein_str+str_array[:i]
                print(str_array[0][:i])


for ctr1 in range(0, total_protein_num):
    #print(total_protein_num)
    for m in range(0, total_protein_num):
        # verify with the char in the next string
        tmp_str = protein_string_arr[m]
        #print(tmp_str)
        for i in range(0, len(tmp_str)):
            char_to_compare_o = tmp_str[i]
            #print(char_to_compare_o)
            for j in range(0, total_protein_num):
                if j != m:
                    for k in range(0, len(tmp_str)):
                        char_to_compare_d = tmp_str[k]
                        #print(char_to_compare_d)

file1.close()