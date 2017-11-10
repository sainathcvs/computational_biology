import re
dna_string_input_raw = open('/home/cvs/PycharmProjects/sampleg/rosalind_grph_1.txt').readlines()
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
    print(str(len(str_array)))
    return str_array


dna_string_input = format_input_file()
print len(str_array)
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
    # print(string_dict.__len__())

file1 = open('output_7.txt', 'w')

total_protein_num = (len(str_array)/2)
for m in range(0, total_protein_num):
    # print(string_dict[key_arr[m]])
    suffix = string_dict[key_arr[m]][-3:]
    #print(key_arr[i]) #prefix
    for j in range(0, total_protein_num):
        if j != m:
            prefix_tmp = string_dict[key_arr[j]][0:3]
            #print(suffix+"---"+string_dict[key_arr[j]][0:3]) #suffix
            if suffix == prefix_tmp:
                print(key_arr[m]+" "+key_arr[j])
                file1.write(key_arr[m]+" "+key_arr[j]+"\n")
file1.close()