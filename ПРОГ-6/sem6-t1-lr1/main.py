# Программирование (Python)
# 6 семестр, тема 1

# Лабораторная работа 1

"""
Используя обучающий набор данных о пассажирах Титаника, находящийся в проекте (оригинал: https://www.kaggle.com/c/titanic/data), найдите ответы на следующие вопросы: 

1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.

2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.

3. Посчитайте долю погибших на параходе (число и процент)?

4. Какие доли составляли пассажиры первого, второго, третьего класса?

5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).

6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
1) возрастом и параметром survival;
2) полом человека и параметром survival;
3) классом, в котором пассажир ехал, и параметром survival.

7. Посчитайте средний возраст пассажиров и медиану.
8. Посчитайте среднюю цену за билет и медиану.

9. Какое самое популярное мужское имя на корабле?
10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?

"""

import pandas  # импортирование библиотеки для считывания данных
import numpy

# считаем данных из файла, в качестве столбца индексов используем PassengerId
data = pandas.read_csv('train.csv', index_col="PassengerId")
humanValue = len(data)

def sort_dict(dict1):
    sorted_dict = {}
    sorted_keys = sorted(dict1, key=dict1.get)  # [1, 3, 2]

    for w in sorted_keys:
        sorted_dict[w] = dict1[w]

    return sorted_dict

# TODO #1
def get_sex_distrib(data):
    """
    1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.
    """

    n_male, n_female = 0, 0

    res = data['Sex'].value_counts()
    n_male, n_female = res['male'], res['female']

    return n_male, n_female

ans1 = get_sex_distrib(data)
print("1. Какое количество мужчин и женщин ехало на параходе? Ответ: Мужчин - ", ans1[0], "Женщин - ", ans1[1])

# TODO #2
def get_port_distrib(data):
    """  
    2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
    """
    
    port_S, port_C, port_Q = 0, 0, 0

    res = data['Embarked'].value_counts()
    port_S, port_C, port_Q = res['S'], res['C'], res['Q']

    return port_S, port_C, port_Q

print("Порт S", get_port_distrib(data)[0], "Порт C", get_port_distrib(data)[1], "Порт Q", get_port_distrib(data)[2])

# TODO #3
def get_surv_percent(data):
    """
    3. Посчитайте долю погибших на параходе (число и процент)?
    """

    n_died, perc_died = 0, 0
    res = data['Survived'].value_counts()
    n_died = res[0]
    perc_died = (n_died / (res[0] + res[1])) * 100

    return n_died, perc_died

print("Число погибших", get_surv_percent(data)[0], "Процент погибших", get_surv_percent(data)[1])

# TODO #4
def get_class_distrib(data):
    """
    4. Какие доли составляли пассажиры первого, второго, третьего класса?    
    """
    n_pas_f_cl, n_pas_s_cl, n_pas_t_cl = 0, 0, 0

    res = data['Pclass'].value_counts()
    n_pas_f_cl = res[1] / humanValue
    n_pas_t_cl = res[3] / humanValue
    n_pas_s_cl = res[2] / humanValue

    return n_pas_f_cl, n_pas_s_cl, n_pas_t_cl

print("Доля первого класса", get_class_distrib(data)[0],"Доля второго класса",  get_class_distrib(data)[1], "Доля третьего класса",  get_class_distrib(data)[2])

# TODO #5
def find_corr_sibsp_parch(data):
    """
    5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
    """

    corr_val = -1
    corr_val = numpy.corrcoef(data['SibSp'], data['Parch'])[1,0]

    return corr_val

print("Коэффициент корреляции Пирсона между количеством супругов и количеством детей", find_corr_sibsp_parch(data))

# TODO #6-1
def find_corr_age_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    - возрастом и параметром survival;
    """

    corr_val = -1
    corr_val = data['Age'].corr(data['Survived'])

    return corr_val

print("Коэффициент корреляции между возрастом и выживаемостью", find_corr_age_survival(data))
print("Из результата следует, что корреляции между данными практически нет")

# TODO #6-2
def find_corr_sex_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - полом человека и параметром survival;
    """

    corr_val = -1

    sex = data['Sex']
    survival = data['Survived']
    #print(type(sex))
    #print(sex)
    sex_arr = []
    for i in sex:
        if (i == 'male'):
            sex_arr.append(0)
        else:
            sex_arr.append(1)
    
    sex_series_digit = pandas.Series(sex_arr)
    corr_val = sex_series_digit.corr(survival)

    return corr_val

print("Коэффициент корреляции между возрастом и выживаемостью", find_corr_sex_survival(data))
print("Из результата следует, что корреляции между данными практически нет")

# TODO #6-3
def find_corr_class_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:

    - классом, в котором пассажир ехал, и параметром survival.
    """

    corr_val = -1
    corr_val = data['Pclass'].corr(data['Survived'])

    
    return corr_val

print("Коэффициент корреляции между возрастом и выживаемостью", find_corr_class_survival(data))
print("Из результата следует, что корреляции между данными имеет слабую обратную корреляцию")

# TODO #7
def find_pass_mean_median(data):
    """
    7. Посчитайте средний возраст пассажиров и медиану.
    """

    mean_age, median = None, None
    age = data['Age']
    mean_age = age.mean()
    median = age.median()

    return mean_age, median

print("Средний возраст пассажиров", find_pass_mean_median(data)[0], "Медианный возраст", find_pass_mean_median(data)[1])

# TODO #8
def find_ticket_mean_median(data):
    """
    8. Посчитайте среднюю цену за билет и медиану.
    """

    mean_price, median = None, None
    fare = data['Fare']
    mean_price = fare.mean()
    median = fare.median()

    return mean_price, median

print("Средняя цена на билет", find_ticket_mean_median(data)[0], "Медианная цена на билет", find_ticket_mean_median(data)[1])

# TODO #9
def find_popular_name(data):
    """
    9. Какое самое популярное мужское имя на корабле?
    """
    name = ""
    names_lst = data['Name'].tolist()
    sex_lst = data['Sex'].tolist()
    
    names_dict = dict()

    for i in range(humanValue):
        if (sex_lst[i] == 'male'):
            if (names_lst[i].find('Mr.') != -1): # Ищем имена с приставкой Mr.
                temp_name = names_lst[i].split('Mr. ')[1] # Выбираем часть с именем
                if (len(temp_name.split(' ')) > 1): # если в разделенной строке больше одного элемента
                    temp_names = temp_name.split(' ')
                    k = 0
                    while (k < len(temp_name.split(' '))):
                        if (not(names_dict.get(temp_names[k]))):
                            names_dict.update({temp_names[k]:0}) # добавляем каждое имя в словарь с нулевым значением
                        k+=1    
                else:
                    if (not(names_dict.get(temp_name))): # иначе только одно
                        names_dict.update({temp_name:0})
            if (names_lst[i].find('Master.') != -1): # Ищем имена с приставкой Master.
                temp_name = names_lst[i].split('Master. ')[1]
                if (len(temp_name.split(' ')) > 1): # если в разделенной строке больше одного элемента
                    temp_names = temp_name.split(' ')
                    k = 0
                    while (k < len(temp_name.split(' '))):
                        if (not(names_dict.get(temp_names[k]))):
                            names_dict.update({temp_names[k]:0})
                        k+=1 
                else:
                    if (not(names_dict.get(temp_name))):
                        names_dict.update({temp_name:0})
        
    
    for i in range(humanValue): # считаем количество повторений имен
        if (sex_lst[i] == 'male'):
            if (names_lst[i].find('Mr.') != -1):
                temp_name = names_lst[i].split('Mr. ')[1]
                if (len(temp_name.split(' ')) > 1):
                    temp_names = temp_name.split(' ')
                    names_dict[temp_names[0]] +=1
                    names_dict[temp_names[1]] +=1
                else:
                    names_dict[temp_name] +=1
            if (names_lst[i].find('Master.') != -1):
                temp_name = names_lst[i].split('Master. ')[1]
                if (len(temp_name.split(' ')) > 1):
                    temp_names = temp_name.split(' ')
                    names_dict[temp_names[0]] +=1
                    names_dict[temp_names[1]] +=1
                else:
                    names_dict[temp_name] +=1
            

    names_sorted = sort_dict(names_dict)
    name = names_sorted.popitem()[0]

    return name

print("Самое популярное мужское имя:", find_popular_name(data))

# TODO #10
def find_popular_adult_names(data):
    """
    10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
    """
    popular_male_name, popular_female_name = "", ""
    male_names_dict = dict()
    female_names_dict = dict()
    return popular_male_name, popular_female_name


# ------------------------------

# Реализуем вычисление количества пассажиров на параходе и опишем предварительные действия с данными (считывание)

# После загрузки данных с помощью метода read_csv и индексации его по первому столбцу данных (PassangerId) становится доступно выборка данных по индексу. 
# С помощью запроса ниже мы можем получить имя сотого пассажира
print((data.iloc[100]['Name']))


def get_number_of_pass(data_file):
    """
        Подсчет количества пассажиров. 
        data_file - str
        В качестве аргумента удобнее всего использовать строковую переменную, куда будет передаваться название файла (т. к. далее, возможно, потребуется подсчитать параметры для другого набора данных test.csv)
    """
    male_int, female_int = 0, 0
    # считывание и обработка данных
    data = pandas.read_csv(data_file, index_col="PassengerId")

    # считать данных из столбца возможно с помощью метода value_counts()
    res = data['Sex'].value_counts()
    # res будет содержать ассоциативный массив, ключами в котором являются значения столбца sex, а целочисленные значениями - количества пассажиров обоих полов
    male_int, female_int = res['male'], res['female']
    return male_int, female_int


def test_get_number_of_pass():
    assert get_number_of_pass('train.csv') == (577,314), " Количество мужчин и женщин на Титанике"

# аналогично протестировать остальные функции

example = "(djjdj"
rasultat = example.split('(')
print(rasultat)