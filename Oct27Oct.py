# import Oct27


# print(Oct27.a)
# print(Oct27.k)


# lst = [1,2,3,4]
# # lst.sort(reverse=True)
# lst.reverse()
# print(lst)

from concurrent.futures import ThreadPoolExecutor

def taks1():
    for i in range(1,10):
        print(i)

def taks2():
    for i in range(25,30):
        print(i)
def taks3():
    for i in range(10,25):
        print(i)

with ThreadPoolExecutor(max_workers=3) as pool:
    t1 = pool.submit(taks1)
    t2 = pool.submit(taks2)
    t3 = pool.submit(taks3)

