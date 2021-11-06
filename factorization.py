
import math

def factorization(n):
    num_list = []
    pow_list = []
    counter = 0
    pow = 1
    while n % 2 == 0:
        num_list.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            num_list.append(i)
            n = n / i
    if n > 2:
        num_list.append(n)
    leng = len(num_list)
    for x in num_list:
        tmp = x
        if(counter + 1 < leng):
            if(tmp == num_list[counter + 1]):
               pow += 1
            else:
                pow_list.append(pow)
                pow = 1
            counter += 1
        else:
            pow_list.append(1)
    tmp = 0
    count =0
    counter = 0
    print("[", end = '')
    for k in num_list:
        if(k != tmp):
            if(count < len(pow_list) -1 ):
                print(f"({int(k)}, {pow_list[count]}), ", end = '')
                count += 1
            else:
                print(f"({int(k)}, {pow_list[count]})", end = '')
    print("]")
if __name__ == '__main__':
    n = 123213
    factorization(n)
