def editDistance(str1,str2,dp):
	m = len(str1)
	n = len(str2)
	dp[0][0]=0
	for i in range(1,m+1):
		dp[i][0] = i#initializing the edit cost
	for j in range(1,n+1):
		dp[0][j] = j#initializing the edit cost
	for i in range(1,m+1):
		for j in range(1,n+1):
			if str1[i - 1] == str2[j - 1]:
				dp[i][j] = dp[i - 1][j - 1]
			else:
				dp[i][j] = min(dp[i - 1][j - 1]+1, min(dp[i][j - 1]+1, dp[i - 1][j]+1))
	return dp[m][n]

def augmentedString(str1,str2,dp):
	result = []
	i = len(str1)
	j = len(str2)
	sb1= []
	sb2= []
	while i!=0 and j!=0:
		if str1[i-1] == str2[j-1]:
			sb1.append(str1[i-1])
			sb2.append(str2[j-1])
			i-=1
			j-=1
		elif dp[i][j] == 1+dp[i-1][j-1]:
			sb1.append(str1[i-1])
			sb2.append(str2[j-1])
			i-=1
			j-=1
		elif dp[i][j] == 1+dp[i-1][j]: 
			sb1.append(str1[i-1])
			sb2.append("-")
			i-=1
		elif dp[i][j] == 1+dp[i][j-1]:
			sb1.append("-") 
			sb2.append(str2[j-1])
			j-=1
		else:
			return []
	return [''.join(sb1[::-1]),''.join(sb2[::-1])]

str_input = open('rosalind_edta.txt').readlines()
str1=str_input[1]
str2=str_input[3]
dp=[]
dp = [[0 for j in range(0,len(str2)+1)] for i in range(0,len(str1)+1)]
print editDistance(str1,str2,dp)
result = augmentedString(str1,str2,dp)
print result[0]
print result[1]

