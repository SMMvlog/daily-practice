from threading import Thread

result = []
print("iidd--",id(result))
print(globals()["result"])

def get_even_num(n):
    for i in range(n):
        if i%2==0:
            result.append(i)
    print("iidd--",id(result))
    return result

t1 = Thread(target=get_even_num,args=(50,))

t1.start()

print(t1)
print(result)

get_fourth_highest_num = 0
print("fdfsdsd",get_fourth_highest_num)
def fourth_highest_num(lst):
    first_highest_num = 0
    second_highest_num = 0
    third_highest_num = 0
    for i in lst:
        if i > first_highest_num:
            second_highest_num = first_highest_num
            third_highest_num = second_highest_num
            get_fourth_highest_num =  third_highest_num
            first_highest_num = i
        elif i > second_highest_num:
            third_highest_num = second_highest_num
            get_fourth_highest_num = third_highest_num
            second_highest_num = i
        elif i > third_highest_num:
            get_fourth_highest_num = third_highest_num
            third_highest_num = i
        elif i > get_fourth_highest_num:
            get_fourth_highest_num = i
    return get_fourth_highest_num

t2 = Thread(target=fourth_highest_num,args=([5,6,7,8,9,10,3,11,18,5,7],))

t2.start()

print(t2)
print("forhtyyyyy-----",get_fourth_highest_num)

from multiprocessing import Process

def abc():
    print("Hello Mehboob")
if __name__ == "__main__":
    p = Process(target=abc)
    p.start()
    p.join()
    print(p)