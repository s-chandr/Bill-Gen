# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
import psycopg2

#these all the details should be there in a seperate files
hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = 'root'
port_id = 5432
connection = None
cursor = None
try:
    connection = psycopg2.connect(
        host = hostname, dbname = database, user = username, password = pwd, port = port_id
    )
    cursor = connection.cursor()
    drop = '''DROP TABLE IF EXISTS transactions'''
    cursor.execute(drop)
    ddl_script = '''    
                        CREATE TABLE IF NOT EXISTS transactions(
                        id      int PRIMARY KEY,
                        name    varchar(25) not null,
                        total_amount  int,
                        items   int,
                        date    timestamp 
                         )'''
    cursor.execute(ddl_script)
    insert_script = 'INSERT INTO transactions (id, name, total_amount, items, date) VALUES (%s,%s,%s,%s,%s)'
    inser_value = [(1,'John',200,3,'2021-01-07'),(2,'Johnnty',300,2,'2021-02-07'),(3,'Mohn',200,3,'2021-03-07'),(4,'Zoen',900,5,'2021-04-07')]
    for item in inser_value:
        cursor.execute(insert_script,item)
    connection.commit()
    cursor.execute('SELECT * FROM transactions ')
    for record in cursor.fetchall():
        print(f'{record[1]} has made a purchase of Rs.{record[2]}')


except Exception as e:
    print(e)

finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()

print("End")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
