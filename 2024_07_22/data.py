from dotenv import load_dotenv
import psycopg2
import os
load_dotenv()



def get_areas() -> list[tuple]:
    conn = psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])
    with conn:
        with conn.cursor() as cursor:
            sql ='''
            SELECT DISTINCT sarea
            FROM youbike;
            '''

            cursor.execute(sql)
            return cursor.fetchall()
    conn.close()

def get_snaOfArea(area:str) -> list[tuple]:
    conn = psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])
    with conn:
        with conn.cursor() as cursor:
            sql ='''
            SELECT sna as ���I,total as �`������,rent_bikes as �i��,return_bikes as �i��, mday as �ɶ�,act as ���A
            FROM youbike
            WHERE (updatetime,sna) IN (
	        SELECT MAX(updatetime),sna
	        FROM youbike
	        WHERE sarea = (%s)
	        GROUP BY sna
            )
            '''

            cursor.execute(sql,(area,))
            return cursor.fetchall()
    conn.close()