# # # # # # def dedup(items):
# # # # # #     seen = set()
# # # # # #     for item in items:
# # # # # #         if item not in seen:
# # # # # #             yield item
# # # # # #             seen.add(item)
# # # # # #
# # # # # # items=[1,5,6,4,5,6,4,4,5,6,8,9,1,7,3]
# # # # # # for i in dedup(items):
# # # # # #     print(i)
# # # # # #
# # # # # # fac = lambda x: __import__('functools').reduce(int.__mul__,range(1, x + 1),1)
# # # # # # gcd = lambda x, y: y % x and gcd(y % x, x) or x
# # # # # #
# # # # # # items = [12, 5, 7, 10, 8, 19]
# # # # # # items = map(lambda x: x ** 2, filter(lambda x: x % 2, items))
# # # # # # for i in items:
# # # # # #     print(i)
# # # # # # items = [12, 5, 7, 10, 8, 19]
# # # # # # items = [x ** 2 for x in items if x % 2]
# # # # # # print(items)    # [25, 49, 361]
# # # # # # class Fib(object):
# # # # # #
# # # # # #     def __init__(self, num):
# # # # # #         self.num = num
# # # # # #         self.a, self.b = 0, 1
# # # # # #         self.idx = 0
# # # # # #
# # # # # #     def __iter__(self):
# # # # # #         return self
# # # # # #
# # # # # #     def __next__(self):
# # # # # #         if self.idx < self.num:
# # # # # #             self.a, self.b = self.b, self.a + self.b
# # # # # #             self.idx += 1
# # # # # #             return self.a
# # # # # #         raise StopIteration()
# # # # # # a=Fib(10)
# # # # # # for i in a:
# # # # # #     print(i)
# # # # # # def fib(n):
# # # # # #     a,b=0,1
# # # # # #     for i in range(n):
# # # # # #         a,b=b,a+b
# # # # # #         yield a
# # # # # #
# # # # # # print(fib(9))
# # # # # # def multiply():
# # # # # #     return [lambda x: i * x for i in range(4)]
# # # # # #
# # # # # # print([m(1) for m in multiply()])
# # # # # # def multiply():
# # # # # #     for i in range(4):
# # # # # #         yield lambda x: x * i
# # # # # #
# # # # # #
# # # # # # # for i in multiply():
# # # # # # #     print(i)
# # # # # #
# # # # # #
# # # # # # [100 for 100 in multiply()]
# # # # # # import re
# # # # # #
# # # # # # username = 'jerry_friend'
# # # # # # m = re.match(r'\w{8,20}', username)
# # # # # # print(m)
# # # # # # def my_max(*args, key=None, default=None):
# # # # # #
# # # # # #     if len(args) == 1 and len(args[0]) == 0:
# # # # # #         if default:
# # # # # #             return default
# # # # # #         else:
# # # # # #             raise ValueError('max() arg is an empty sequence')
# # # # # #     items = args[0] if len(args) == 1 else args
# # # # # #     max_elem, max_value = items[0], items[0]
# # # # # #     if key:
# # # # # #         max_value = key(max_value)
# # # # # #     for item in items:
# # # # # #         value = item
# # # # # #         if key:
# # # # # #             value = key(item)
# # # # # #
# # # # # #         if  value > max_value:
# # # # # #             max_elem, max_value = item, value
# # # # # #     return max_elem
# # # # #
# # # # # # def count_letters(items):
# # # # # #     result = {}
# # # # # #     for item in items:
# # # # # #         if isinstance(item, (int, float)):
# # # # # #             result[item] = result.get(item, 0) + 1
# # # # # #     return result
# # # # # # print(count_letters(var))
# # # # # from collections import Counter
# # # # #
# # # # # # def count_letters(items):
# # # # # #     counter = Counter(items)
# # # # # #     return {key: value for key, value in counter.items()\
# # # # # #             if isinstance(key, (int, float))}
# # # # # #
# # # # # # var=[5,9,7,6,8,7,4,5,9,7,2,5]
# # # # # # print(count_letters(var))
# # # # # # import os
# # # # # #
# # # # # # g = os.walk(r'C:\Users\MCXJB666\Desktop\python\selenium')
# # # # # # for path, dir_list, file_list in g:
# # # # # #     for dir_name in dir_list:
# # # # # #         print(os.path.join(path, dir_name))
# # # # # #     for file_name in file_list:
# # # # # #         print(os.path.join(path, file_name))
# # # # # # from functools import lru_cache
# # # # # #
# # # # # #
# # # # # # @lru_cache()
# # # # # # def change_money(total):
# # # # # #     if total == 0:
# # # # # #         return 1
# # # # # #     if total < 0:
# # # # # #         return 0
# # # # # #     return change_money(total - 2) + change_money(total - 3) + \
# # # # # #         change_money(total - 5)
# # # # # #
# # # # # #
# # # # # # print(change_money(10))
# # # # # # def show_spiral_matrix(n):
# # # # # #     matrix = [[0] * n for _ in range(n)]
# # # # # #     row, col = 0, 0
# # # # # #     num, direction = 1, 0
# # # # # #     while num <= n ** 2:
# # # # # #         if matrix[row][col] == 0:
# # # # # #             matrix[row][col] = num
# # # # # #             num += 1
# # # # # #         if direction == 0:
# # # # # #             if col < n - 1 and matrix[row][col + 1] == 0:
# # # # # #                 col += 1
# # # # # #             else:
# # # # # #                 direction += 1
# # # # # #         elif direction == 1:
# # # # # #             if row < n - 1 and matrix[row + 1][col] == 0:
# # # # # #                 row += 1
# # # # # #             else:
# # # # # #                 direction += 1
# # # # # #         elif direction == 2:
# # # # # #             if col > 0 and matrix[row][col - 1] == 0:
# # # # # #                 col -= 1
# # # # # #             else:
# # # # # #                 direction += 1
# # # # # #         else:
# # # # # #             if row > 0 and matrix[row - 1][col] == 0:
# # # # # #                 row -= 1
# # # # # #             else:
# # # # # #                 direction += 1
# # # # # #         direction %= 4
# # # # # #     for x in matrix:
# # # # # #         for y in x:
# # # # # #             print(y, end='\t')
# # # # # #         print()
# # # # # items = [1, 2, 3, 4]
# # # # # print([i for i in items if i > 2])
# # # # # print([i for i in items if i % 2])
# # # # # print([(x, y) for x, y in zip('abcd', (1, 2, 3, 4, 5))])
# # # # # print({x: f'item{x ** 2}' for x in (2, 4, 6)})
# # # # # print(len({x for x in 'hello world' if x not in 'abcdefg'}))
# # # # # print({x for x in 'hello world' if x not in 'abcdefg'})
# # # # from functools import wraps
# # # # from time import time
# # # #
# # # #
# # # # def record_time(func):
# # # #     @wraps(func)
# # # #     def wrapper(*args, **kwargs):
# # # #         start = time()
# # # #         result = func(*args, **kwargs)
# # # #         print(f"{func.__name__}执行时间´: {time() - start}s")
# # # #         return result
# # # #
# # # #     return wrapper
# # # # @record_time
# # # # def fib(n):
# # # #     a,b = 0,1
# # # #     for i in range(n):
# # # #         a, b = b, a + b
# # # #         yield a
# # # #
# # # # fib(6)
# # # #
# # #
# # #
# # #
# # #
# # # # #     # 多个逻辑块 使用yield 生成一个列表
# # # # #     for i in range(10):
# # # # #         yield i
# # # # #     for j in range(5):
# # # # #         yield j * j
# # # # #     for k in [100, 200, 300]:
# # # # #         yield k
# # # #
# # # #
# # # #
# # # #
# # # class A:
# # #     def who(self):
# # #         print('A', end='')
# # #
# # # class B(A):
# # #     def who(self):
# # #         super(B, self).who()
# # #         print('B', end='')
# # #
# # # class C(A):
# # #     def who(self):
# # #         super(C, self).who()
# # #         print('C', end='')
# # #
# # # class D(B, C):
# # #     def who(self):
# # #         super(D, self).who()
# # #         print('D', end='')
# # #
# # # # item = D()
# # # # item.who()
# # # #
# # # print(D.mro())
# # #
# #
# # import operator
# #
# #
# # class Stack:
# #
# #
# #     def __init__(self):
# #         self.elems = []
# #
# #     def push(self, elem):
# #
# #         self.elems.append(elem)
# #
# #     def pop(self):
# #
# #         return self.elems.pop()
# #
# #     @property
# #     def is_empty(self):
# #
# #         return len(self.elems) == 0
# #
# #
# # def eval_suffix(expr):
# #
# #     operators = {
# #         '+': operator.add,
# #         '-': operator.sub,
# #         '*': operator.mul,
# #         '/': operator.truediv
# #     }
# #
# #     stack = Stack()
# #     for item in expr.split():
# #         if item.isdigit():
# #             stack.push(float(item))
# #         else:
# #             num2 = stack.pop()
# #             num1 = stack.pop()
# #             stack.push(operators[item](num1, num2))
# #     return stack.pop()
# #
# #
# # a='8*5+3*(1.2+8.9)'
# # eval_suffix(a)
# #
# #
# # message = 'hello, world!'
# # print(message.replace('o', 'O').replace('l', 'L').replace('he', 'HE'))
# # import re
# #
# # message = 'hello, world!'
# # pattern = re.compile('[aeiou]')
# # print(pattern.sub('#', message))
# # import random
# # a=[]
# # for i in range(100):
# #     a.append(random.gauss(1, 2))
# # print(a)
# # def extend_list(val, items=[]):
# #     items.append(val)
# #     return items
# #
# # list1 = extend_list(10)
# # list2 = extend_list(123, [])
# # list3 = extend_list('a')
# # print(list1)
# # print(list2)
# # print(list3)
# # with open(r'C:\Users\MCXJB666\Desktop\python\python点击\1.png', 'rb') as file:
# #     for data in iter(lambda: file.read(20), b''):
# #         print(data)
# # prices = {
# #     'AAPL': 191.88,
# #     'GOOG': 1186.96,
# #     'IBM': 149.24,
# #     'ORCL': 48.44,
# #     'ACN': 166.89,
# #     'FB': 208.09,
# #     'SYMC': 21.29
# # }
# # print(sorted(prices,key=lambda x:prices[x],reverse=True))
# # def more_than_half(items):
# #     temp, times = None, 0
# #     for item in items:
# #         if times == 0:
# #             temp = item
# #             times += 1
# #         else:
# #             if item == temp:
# #                 times += 1
# #             else:
# #                 times -= 1
# #     return temp
# # a=[1,2,3,4,4,3,5,5,5,]
# # print(more_than_half(a))
# import random
# from collections import Counter
# def find_same(lists):
#     d={}
#     if isinstance(lists,list):
#         dict=Counter(lists)
#     for key,value in dict.items():
#         if value >1:
#             d.update({key:value})
#     return d
#
#
# lists = []
# for x in range(10000):
#     lists.append(random.randint(1000, 9999))
# print(find_same(lists))
a='i love you very much'
b=''.join(a)
print(b)

