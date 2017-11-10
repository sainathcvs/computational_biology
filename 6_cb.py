import math
# getting input and formatting as needed
dna_string_input = open('/home/cvs/PycharmProjects/sampleg/rosalind_prob.txt').read()
str_array = dna_string_input.split("\n")
dna_string = str_array[0]
ak_str = str_array[1]
ak_arr = ak_str.split(" ")


# calculate b[k] based on probabilities
def get_at_probability(val):
    tmp = (1-float(val))/2
    at_probability = math.log10(tmp)
    return at_probability


def get_gc_probability(val):
    gc_probability = math.log10((float(val))/2)
    return gc_probability


result = []
for j in range(0, len(ak_arr)):
    final_bk = 0
    for i in range(0, len(dna_string)):
        if dna_string[i] == 'A' or dna_string[i] == 'T':
            tmp_bk = get_at_probability(ak_arr[j])
            # print('at '+"%.3f" %(tmp_bk))
            final_bk = final_bk + tmp_bk
        if dna_string[i] == 'G' or dna_string[i] == 'C':
            tmp_bk = get_gc_probability(ak_arr[j])
            # print('gc ' + "%.3f" % (tmp_bk))
            final_bk = final_bk + tmp_bk
    if j == 0:
        result = str("%.3f" % final_bk)
    if j != 0:
        result = result+" "+str("%.3f" % final_bk)
print(result)
