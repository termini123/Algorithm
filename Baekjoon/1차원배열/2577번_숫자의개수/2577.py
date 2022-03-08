'''
코드1번
cnt = int(input())
numbers = list(map(int, input().split()))
max = numbers[0]
min = numbers[0]

for i in numbers[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i

print(min,max)

'''
#코드2번(간략화)
cnt = int(input())
numbers = list(map(int, input().split()))
print(min(numbers),max(numbers))