N = int(input())
A = list(map(int, input().split()))

# 진짜 약수가 모두 주어지기 떄문에
# 가장 작은 값과 가장 큰 값을 곱하면
# 진짜 수를 구할 수 있다.
max_num = max(A)
min_num = min(A)

print(max_num * min_num)