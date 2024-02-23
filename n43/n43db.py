# import psycopg2
#
# oylik = {'dbname': 'kamron',
#          'user': 'postgres',
#          'host': 'localhost',
#          'port': 5432,
#          'password': 26042604
#          }
# coon = psycopg2.connect(**oylik)
# curr = coon.cursor()
#
#
# curr.execute("""""")
# # def der_op(table_name):
# #     curr.execute(f"drop table {table_name}")
# #     print('uchdi')
# #
# # der_op('olma')
#
# coon.commit()
# coon.close()


import psycopg2
a = input('table namenini kiriting')
oylik = {'dbname': 'kamron',
         'user': 'postgres',
         'host': 'localhost',
         'port': 5432,
         'password': 26042604
         }
coon = psycopg2.connect(**oylik)
curr = coon.cursor()


def new_table(a):
     curr.execute(f"drop table {a}")
     print('uchdi')

new_table(a)


coon.commit()
coon.close()