str_input = open('rosalind_ctea.txt').readlines()
str1=str_input[1]
str2=str_input[3]
dp=[]
dp = [[0 for j in range(0,len(str2)+1)] for i in range(0,len(str1)+1)]
cnt = [[0 for j in range(0,len(str2)+1)] for i in range(0,len(str1)+1)]

for i in range(0,len(str1)+1):
	for j in range(0,len(str2)+1):
		if i==0:
			dp[0][j] = j
			cnt[0][j] = 1
		elif j==0:
			dp[i][0] = i
			cnt[i][0] = 1
		else:
			dp[i][j] = min(dp[i - 1][j - 1]+(str1[i-1]!=str2[j-1]),dp[i][j - 1]+1, dp[i - 1][j]+1)
			if dp[i][j] == (str1[i-1]!=str2[j-1])+dp[i-1][j-1]:
				cnt[i][j] += cnt[i-1][j-1]
			if dp[i][j] == 1+dp[i-1][j]:
				cnt[i][j] += cnt[i-1][j]
			if dp[i][j] == 1+dp[i][j-1]:
				cnt[i][j] += cnt[i][j-1]

print cnt[len(str1)][len(str2)]%134217727