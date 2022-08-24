list1 =[1,2,3,4,5,6,7,8,9,10,11,12]
"""
create a function that will loop throght a list
when it loop throght a list divisible by 4, print "fibo"
if it divisible by both 4 and 6,print "fibonanci"
else print that number
"""
def fiboNazi(list):
    
    for i in list1 :
        if (i%4 == 0 and i%6 == 0) :
            print("fiboNazi")
        elif (i%4 == 0) :
            print("fibo")
        else :
            print(i)

fiboNazi(list)