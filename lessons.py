# 以下のURLの問題の回答コード
# 
# 問題１

# a = int(input())
# b, c = map(int,input().split())
# s = input()

# print('{} {}'.format(a+b+c,s))

# #問題２


# a, b = map(int,input().split())
# print("Even" if a*b % 2 == 0 else "Odd" )


# 問題３
# s=input()4

# print(s.count("1"))

# 問題４

N = int(input())
A = list(map(int,input().split()))
count = 0
while all(a % 2 == 0 for a in A):
  A = [a/2 for a in A]
  count += 1
print(count)
