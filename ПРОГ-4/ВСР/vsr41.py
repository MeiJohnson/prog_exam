
def sort_paste(arr): 
    """ 
    Создание программы с реализацией вручную одного из алгоритмов 
    сортировки (вставки, плавной сортировки).
    """
    n = len(arr)
    for i in range(2,n):
        x = arr[i]
        j = i-1
        while(j>0 and arr[j] > x):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1] = x         

    return arr


def main():
    size = int(input("Введите размер массива "))
    m = []
    print("Введите массив ")
    for el in range(size):
        m.append(int(input()))
    m_sort = sort_paste(m)
    print(m_sort)
    pass
main()