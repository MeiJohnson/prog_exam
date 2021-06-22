import sqlite3


# c = conn.cursor()

def connect(db_name):
    try:
        conn = sqlite3.connect('file:'+db_name+'?mode=ro', uri=True)
    except sqlite3.OperationalError:
        try:
            conn = sqlite3.connect('file:'+db_name+'?mode=ro', uri=True)
        except sqlite3.OperationalError as e:
            return e
    else:
        return conn        

db_name1 = 'example.db'
conn = connect(db_name1)

if isinstance(conn, sqlite3.OperationalError):
    conn = sqlite3.connect(db_name1)

print(type(conn))

def close_db(conn):
    try:
        conn.close()
    except AttributeError:
        pass
    finally:
        print('ЕХИТ')
close_db(conn)

# create_table('stocks',['id int', 'date text', 'qty real'])
def create_tb(c, domens_lst):
    # убедиться что таблицы нет
    # если она есть, пропустить создание
    # при этом он адолжна быть объектом класса <class 'sqlite3.Connection'>
    if not isinstance(conn, sqlite3.Connection):
            raise sqlite3.OperationalError
    else:
        try:
        # Create table           
            c.execute(f"CREATE TABLE stoks text {domens_lst[0]}, text {domens_lst[1]}, text {domens_lst[2]}, real {domens_lst[3]}, real {domens_lst[4]}")
        except sqlite3.ProgrammingError:
            print('tb already exists.')
  
# еще 4 функции: добавление данных в таблицу, обновление, удаление, выборка 

def insert_data(c, tb_name, *args):
    data = args[0]
    c.execute(f"INSERT INTO {tb_name} VALUES {data}")


def update_data(c, tb_name, *args):
    field_val = args[0] 
    condition = args[1]
    c.execute(f"UPDATE {tb_name} SET {field_val} WHERE {condition}")


def select_data(c, tb_name, field, condition):
    c.execute(f"SELECT {field} FROM {tb_name} WHERE {condition}")
    
        

def del_data(c, tb_name, condition):
    try:
        c.execute(f"DELETE FROM {tb_name}  WHERE {condition}")
    except sqlite3.ProgrammingError:
        print('Data not found.')
        
create_tb(conn, ['papa','mama', 'you', 12,13])