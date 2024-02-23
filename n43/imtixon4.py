import psycopg2
oylik = {'dbname': 'kamron',
         'user': 'postgres',
         'host': 'localhost',
         'port': 5432,
         'password': 26042604
         }
coon = psycopg2.connect(**oylik)
curr = coon.cursor()


for i in oylik:
    with open('info.csv', 'a') as kam:
        kam.write(f'{i}\n')



coon.commit()
coon.close()