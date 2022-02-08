# 以下の問題の回答コード
# https://atcoder.jp/contests/abs/tasks
# 問題１

# a = int(input())
# b, c = map(int,input().split())
# s = input()

# print('{} {}'.format(a+b+c,s))

# #問題２


# a, b = map(int,input().split())
# print("Even" if a*b % 2 == 0 else "Odd" )


# 問題３
# s=input()

# print(s.count("1"))
#参考(https://note.nkmk.me/python-collections-counter/)

# 問題４


# N = int(input())
# A = list(map(int,input().split()))
# count = 0
# while all(a % 2 == 0 for a in A):
#   A = [a/2 for a in A]
#   count += 1
# print(count)

#参考：https://udemy.benesse.co.jp/development/python-work/python-for.html

#問題５

# a, b, c, x = map(int, [input() for i in range(4)])
# answer = 0
# for i in range(a+1):
#     for j in range(b+1):
#         for k in range(c+1):
#             if i * 500 + j * 100 + k * 50 == x:
#                 answer += 1
# print(answer)

# 参考：https://www.javadrive.jp/python/function/index6.html

# n, a, b = map(int, input().split())
# count = 0
# for i in range(n+1):
#   s = str(i)
#   sums = list(map(int, s))
#   if a <= sum(sums) <= b:
#     count += i
# print(count)

# 問題６
# n = int(input())
# l = list(map(int, input().split()))
# l.sort(reverse=True)
# x = 0
# for i in range(len(l)):
#     if i % 2 ==0:
#         x += l[i]
#     else:
#         x -= l[i]
# # output
# print(x)

# 問題７


# n = int(input())
# a = [int(input()) for i in range(n)]
# print(len(set(a)))

# 参考：https://uxmilk.jp/14834


