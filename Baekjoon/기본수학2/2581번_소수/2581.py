M = int(input())
N = int(input())

# process
decimal = []
for i in range(M, N+1):
	for j in range(2, i+1):
		if j == i:
			decimal.append(i)
		if i % j == 0:
			break

# output
if not decimal:
	print(-1)
else:
	print(sum(decimal))
	print(decimal[0])