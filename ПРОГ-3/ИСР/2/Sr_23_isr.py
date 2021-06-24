def fibon_1(lst):  
    sub_List = lst[2::2]
    result = sum(sub_List)
    print(result)

def fibon_2(lst):
    sub_List = lst[5::2]
    result = sum(sub_List)
    print(result)

def fibon_3(lst):
    med = round(len(lst)/2)
    sub_List = lst[:med:2]
    result = sum(sub_List)
    print(result)

def fibon_4(lst):
    med = round(len(lst)/2)
    if med % 2 == 0:
        sub_List = lst[med+1::2]
    else:
        sub_List = lst[med::2]
    result = sum(sub_List)
    print(result)

def fibon_5(lst):
    med = round(len(lst)/2)
    if med % 2 == 0:
        sub_List = lst[med::2]
    else:
        sub_List = lst[med+1::2]
    result = max(sub_List)
    print(result)


def fibon_6(lst):
    med = round(len(lst)/2)
    sub_List = lst[1:med:2]
    result = min(sub_List)
    print(result)

def fibon_7(lst):
    med = round(len(lst)/2)
    if med % 2 == 0:
        sub_List = lst[len(lst)-1:med:-2]
    else:
        sub_List = lst[len(lst)-1:med+1:-2]

    print(sub_List)

def fibon_8(lst):
    med = round(len(lst)/2)
    if med % 2 == 0:
        sub_List = lst[med+1:0:-2]
    else:
        sub_List = lst[med:0:-2]

    print(sub_List)

def fibon_9(lst):
    
    med = round(len(lst)/2)

    sub_List = lst[med:lst[len(lst)-1]]

    result = str(sub_List[len(sub_List)-1])
    result1 = result[::-1]

    print(result1)

def fibon_10(lst):
    
    med = round(len(lst)/2)

    sub_List = lst[:med:]
    result = sub_List[len(sub_List)-1]
    print(result)

def fibon_11(lst):

    med = round(len(lst)/2)

    sub_List = lst[med-3:med+3]

    even_List = sub_List[::2]

    result = even_List[len(even_List)-1]**2
    print(result)

def fibon_12(lst):
    med = round(len(lst)/2)
    sub_List = lst[:med:2]
    result1 = sum(sub_List)
    
    result = result1 + sum(lst)
    print(result)

def fibon_13(lst):
    med = round(len(lst)/2)
    sub_List = lst[1:med:2]
    result1 = sum(sub_List)
    result = result1 + sum(lst)
    print(result)

def fibon_14(lst):
    med = round(len(lst)/2)
    if med % 2 == 0:
        sub_List = lst[med::2]
    else:
        sub_List = lst[med+1::2]
    result = sum(sub_List) + sum(lst)
    print(result)

def fibon_15(lst):
    med = round(len(lst)/2)
    if med % 2 == 0:
        sub_List = lst[med+1::2]
    else:
        sub_List = lst[med::2]
    result1 = sum(sub_List)

    result = sum(lst) + result1
    print(result)

def fibon_16(lst):
    sub_List = lst[2::2]
    result1 = sum(sub_List)
    
    result = min(lst) + result1
    print(result)


def fibon_17(lst):
    sub_List = lst[5::2]
    result1 = sum(sub_List)

    result = max(lst) + result1
    print(result)


def fibon_18(lst):
    med = round(len(lst)/2)
    sub_List = lst[:med:2]
    result1 = sum(sub_List)

    med = round(len(lst)/2)
    if med % 2 == 0:
        sub_List = lst[med+1::2]
    else:
        sub_List = lst[med::2]
    result2= sum(sub_List)

    result = result1 + result2
    print(result)

def fibon_19(lst):
    med = round(len(lst)/2)
    sub_List = lst[:med:2]
    result1 = sum(sub_List)

    med = round(len(lst)/2)
    if med % 2 == 0:
        sub_List = lst[med+1::2]
    else:
        sub_List = lst[med::2]
    result2= sum(sub_List)

    result = result1 + result2
    print(result)

def main():
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 
    987, 1597, 2584, 4181, 6765, 10946]

    fibon_1(lst)
    fibon_2(lst)
    fibon_3(lst)
    fibon_4(lst)
    fibon_5(lst)
    fibon_6(lst)
    fibon_7(lst)
    fibon_8(lst)
    fibon_9(lst)
    fibon_10(lst)
    fibon_11(lst)
    fibon_12(lst)
    fibon_13(lst)
    fibon_14(lst)
    fibon_15(lst)
    fibon_16(lst)
    fibon_17(lst)
    fibon_18(lst)
    fibon_19(lst)

main()