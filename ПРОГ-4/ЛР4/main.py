import sqlite3
# from deco import once 
import functools

def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, func.__doc__, args, kwargs) 
        if not inner.called:      
            conn = func(*args, **kwargs)
            inner.called = True
            print('called is changed')
            return conn
    print('init')       
    inner.called = False 
    return inner 

@once
def connect_to_db(path_to_db):
    connection = None
    if (path_to_db):
        try:
            # connection = sqlite3.connect('file:' + path_to_db + '?mode=rw', uri=True)
            connection = sqlite3.connect(":memory:") # код для trinket, не для repl.it
        except:
            return None
        else:
            c = connection.cursor()
            return {"conn": connection, "cursor": c}

    return connection


def wrapper(conn,table):
    auth_stat = False
    # он должен в себе содержать: 
    # ввод с клавиатуры или получения из другого источника 
    # логина и пароля 
    log = str(input("Введите логин "))
    pas = str(input("Введите пароль "))
    # получение из БД пользователя с тем логином, который был введен
    user_query = "SELECT * FROM " + str(table) + " WHERE login=" + "'" + log + "'"
    cursor = conn.cursor()
    res = cursor.execute(user_query)
    user_info = res.fetchall()
    if not user_info:
        print("Нет такого пользователя")
        return auth_stat
    print(user_info)
    # сверка пароля введенного пользователем с паролем, хранящемся в БД
    # если успех и аутентификация прошла успешно, показываем 
    # private_zone_area
    # если нет, то показать надпись пользователю о том, пользователя с таким паролем - нет
    role = ''
    
    if (user_info[0][1] == pas):
        print(private_zone_area())    
    else:
        print("Пользователя с таким паролем не существует")
        return auth_stat
    
    if (user_info[0][0]) == 'root':
        print('Вы зашли как root')
        role = '0'
        
    elif (user_info[0][0]) == 'admin':
        print('Вы зашли как admin')
        role = '1'
    else:
        print('Вы зашли как обычный пользователь')
        role = '2'
    return role


def private_zone_area():
    return "private_zone_area"


def get_users_from_table(conn, table):
    sql_query = "SELECT * FROM " + str(table)
    cursor = conn.cursor()
    res = cursor.execute(sql_query)
    users_lst = res.fetchall()

    return users_lst


def main():
    conn_dict = connect_to_db('example.db')
    conn, cur = conn_dict["conn"], conn_dict["cursor"]

    
    try:
        sql_query = '''CREATE TABLE users
            (login text, pass text, role int)'''
        cur.execute(sql_query)
    except sqlite3.OperationalError as e:
        e_str = str(e)
        if ("already exists" in e_str):
            print(f' NOTICE: {e}. CONTINUE ')
    else:
        sql_query = '''INSERT INTO users VALUES (?, ?, ?)'''
        users_lst = [('root', '123', 0), ('admin', '789', 1), ('user', 'qwe', 2)]
    try:
        cur.executemany(sql_query, users_lst)
        conn.commit()
    except sqlite3.Error as e:
        print(f'Error with adding users to db. {e}')
    
    users = get_users_from_table(conn, 'users')            

    print(users)
    user_role = False
    while(user_role == False):
        user_role = wrapper(conn,'users')
        if user_role == False:
            print("Выйти?")
            if str(input("Да/Нет ")) == "Да":
                conn.close()
                cur, conn = None, None
                return 0
    conn.close()
    cur, conn = None, None

main()