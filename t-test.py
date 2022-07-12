import math
a = [10, 20, 30, 40, 50] #input1
b = [1, 29, 46, 78, 99] #input2 
def me_an(ele =''):
    mean_sum = 0
    for i in ele:
        mean_sum = mean_sum+i
    return(mean_sum/len(a))

def std_dev(ele=''):
    mn = me_an(ele)
    sd_sum = 0
    for i in ele:
        sd_sum = (sd_sum +(abs(i - mn))**2)
    varience = sd_sum/len(a)
    return math.sqrt(varience)

def t_test(a,b):
    
    mean_diff = (me_an(a)-me_an(b))
    sqroot = math.sqrt(((me_an(a)**2)/len(a))+((me_an(a)**2)/len(a)))
    test = (mean_diff/sqroot)
    return abs(test)
print(t_test(a, b))
