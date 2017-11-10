str_input = open('rosalind_fibd.txt').read().strip()
n=int(str_input.split(" ")[0])#nth month
m=int(str_input.split(" ")[1])#lives for m months
rabbit_counts = [1,1]
for i in range(n-2):
    tmp_count = 0
    if i+2<m:
        tmp_count = sum(rabbit_counts[i:i+2])
    else:
        tmp_count = sum(rabbit_counts[i-(m-2):i+1])
    rabbit_counts.append(tmp_count)
print rabbit_counts[-1]