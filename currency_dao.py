import psycopg2

# data to get access to db
dbname = "dbname"
user = "user"
password = "password"
host = "host"
port = "port"


# load data about currency to db
def add_currency_rate_to_database(line):

    try:

        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )



        id=int(line['Cur_ID'])
        date=line['Date']
        abb=str(line['Cur_Abbreviation'])
        scale=int(line['Cur_Scale'])
        name=str(line['Cur_Name'])
        rate=float(line['Cur_OfficialRate'])


        cursor = conn.cursor()
        sql_query = "INSERT INTO public.currency (\"Cur_id\", \"Date\", \"Cur_Abbreviation\", \"Cur_Scale\", \"Cur_Name\", \"Cur_OfficialRate\") VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql_query, (id, date, abb, scale, name, rate))

        conn.commit()
        cursor.close()

        conn.close()
    except psycopg2.IntegrityError as e:
        if 'duplicate key value violates unique constraint "currencies"' in str(e):
            return


    return