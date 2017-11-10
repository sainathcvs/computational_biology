freq_list = {}


def calc_symbol_frequencies(input_str):
    freq_a = 0
    freq_c = 0
    freq_g = 0
    freq_t = 0
    for i in range(0, len(input_str)):
        if input_str[i] == "A":
            freq_a += 1
        if input_str[i] == "C":
            freq_c += 1
        if input_str[i] == "G":
            freq_g += 1
        if input_str[i] == "T":
            freq_t += 1
    freq_list["A"] = str(freq_a)
    freq_list["C"] = str(freq_c)
    freq_list["G"] = str(freq_g)
    freq_list["T"] = str(freq_t)
    return freq_list


str_input = open('/home/cvs/PycharmProjects/sampleg/rosalind_dna.txt').read()
freq_all = calc_symbol_frequencies(str_input)
print(freq_list['A']+" "+freq_list['C']+" "+freq_list['G']+" "+freq_list['T'])
