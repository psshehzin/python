# def decor(func):
#     def inner():
#         print("inside new feature")
#         return(func())
#     return inner

# @decor
# def testdecor():
#     print(" i wont be opened unless inner returns func(a)")
#     return 4
# a=10
# b=testdecor()
# print(b)

# class Test():
#     def __init__(self,a1,b):
#         self.a1=a1
#         self.b=b
# class Test2():
#     def get_tasks(self):
#         return[
#             Test(1,2),
#             Test(1,3)
#         ]
# a=Test2()
# b=a.get_tasks()
# for i in b:
#     print(i.b)
import unittest
class Task():
    def __init__(self,name,dependsOn=[]):
        self.name=name
        self.dependsOn=dependsOn
class Tasklist():
    def get_tasks(self):
        return[
            Task("application A",["mongo"]),
            Task("Storage"),
            Task("mongo",["storage"]),
            Task("mem_cache"),
            Task("application B",["mem_cache"]),
        ]
class Solution(unittest.TestCase):
    def get_tasks_with_dependencies(self):        
        a=Tasklist()
        tasks=a.get_tasks()
        ans=[]
        for i in tasks:
            if len(i.dependsOn)==0:
                continue
            else:
                ans.append(i.name)
        return ans
b=Solution()
c=b.get_tasks_with_dependencies()
print(c)