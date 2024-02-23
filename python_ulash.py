# import psycopg2
#
# # Define your connection parameters
# people11 = {
#     'database': 'kamron',
#     'user': 'postgres',
#     'password': 26042604,
#     'host': 'localhost',
#     'port': 5432,
# }
#
# # Add additional connection parameter 'client_encoding' to the dsn string
# dsn = "dbname={database} user={user} password={password} host={host} port={port} client_encoding=latin1".format(**people11)
#
# # Establish the connection
# conn = psycopg2.connect(dsn)



import psycopg2
d = input('table kiriting')

oylik = {'dbname': 'kamron',
         'user': 'postgres',
         'host': 'localhost',
         'port': 5432,
         'password': 26042604
         }
coon = psycopg2.connect(**oylik)
curr = coon.cursor()


def new_table(a):
    curr.execute(f"create table {a} (id int)")
    print(f'{d} nomli TABLE YARATILDI')


new_table(d)

coon.commit()
coon.close()

















