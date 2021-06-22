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
# close_db(conn)

# create_table('stocks',['id int', 'date text', 'qty real'])
def create_tb(c, fieldset):
    # убедиться что таблицы нет
    # если она есть, пропустить создание
    # при этом он адолжна быть объектом класса <class 'sqlite3.Connection'>
    if not isinstance(conn, sqlite3.Connection):
            raise sqlite3.OperationalError
    else:
        try:
        # Create table
            c.execute(f"CREATE TABLE 'stocks' {fieldset}")
        except sqlite3.ProgrammingError:
            print('tb already exists.')
  
# еще 4 функции: добавление данных в таблицу, обновление, удаление, выборка 
create_tb(conn,['id int', 'date text', 'qty real'])
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
    
def test_f_PE(c, f_name, tb_name, *args):
    try:
        f_name(c,tb_name)
    except sqlite3.ProgrammingError:
        print('Table not found.')


def test_f_OE(c, f_name, tb_name, *args):
    try:
        f_name(c,tb_name, args)
    except sqlite3.OperationalError:
        print('Uncorrect values.')


# Insert a row of data
# # c.execute("INSERT INTO stocks VALUES ('2006-01-05','SELL','RHAT',100,35.14)")

# # Save (commit) the changes
# conn.commit()

# #for rec in c.execute("SELECT * FROM stocks"):
# #    print(rec)

# c.execute("DELETE FROM stocks WHERE trans= 'BUY'")

# for rec in c.execute("SELECT * FROM stocks"):
#     print(rec)
    
# qty = 300 
# trans = 'SELL'
# symbol = 'RHAT'
   
# c.execute(f"UPDATE stocks SET trans = '{trans}', qty = {qty} WHERE symbol = '{symbol}'")

# for rec in c.execute("SELECT * FROM stocks"):
#     print(rec)



# # SELECT * FROM stocks

# # UPDATE stocks SET trans = 'BUY', qty = 200 WHERE symbol = 'RHAT'