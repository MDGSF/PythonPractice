#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
安装：
conda install -c bioconda mysqlclient
"""

import MySQLdb


def getVersion(db):
    cursor = db.cursor()

    cursor.execute("select VERSION()")

    data = cursor.fetchone()

    print(f"Databse version: {data}")


def createTable(db):
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    sql = """
CREATE TABLE EMPLOYEE (
FIRST_NAME CHAR(20) NOT NULL,
LAST_NAME CHAR(20),
AGE INT,
SEX CHAR(1),
INCOME FLOAT )
    """
    cursor.execute(sql)


def insertdata(db):
    cursor = db.cursor()

    sql = """
INSERT INTO EMPLOYEE(
FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
VALUES ('Mac', 'Mohan', 20, 'M', 2000)
    """

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


def selectdata(db):
    cursor = db.cursor()

    sql = "SELECT * FROM EMPLOYEE  \
          WHERE INCOME > %s" % 1000

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            print(f'fname={fname}, lname={lname}, age={age}, sex={sex}, '
                  f'income={income}')
    except:
        print('Error: unable to fetch data')


def main():
    db = MySQLdb.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='123456',
        db='MysqlPractice')

    getVersion(db)
    createTable(db)
    insertdata(db)
    selectdata(db)

    db.close()


if __name__ == "__main__":
    main()
