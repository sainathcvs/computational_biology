str_input = open('rosalind_ba9i.txt').read().strip()
#get rotations
tmp = str_input*2
bwt_rot = [tmp[i:i+len(str_input)] for i in range(len(str_input))]
#sort the rotations
bwt_sorted = sorted(bwt_rot)
final_str = ""
for x in sorted(bwt_rot):
	final_str+=x[-1]
print final_str