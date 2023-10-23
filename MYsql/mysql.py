import pymysql

connect_db = pymysql.connect(

    user = "root",
    password = "0312",
    host = "127.0.0.1",
    db = "mobledb",
    charset= "utf8",

)

#객체생성
cursor = connect_db.cursor()
sql = "SELECT * FROM customer"
# insert into table이름(column이름) values(값);
cursor.execute(sql)
#결과값 받아옴
len = cursor.fetchall()
#튜플형식으로 리턴
print(len)
#db닫기
connect_db.close()
