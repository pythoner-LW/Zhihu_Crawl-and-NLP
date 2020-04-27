import pymysql


# mysql数据库操作
class mysql:
    def connection(self):
        db = pymysql.connect("localhost", "root", "123456", "zhihu_data")
        # print("succeed")
        return db

    def insert_question(self, db, follow_num, broswer_num, answer_num, q_content, describe,topic):
        flag = True
        cursor = db.cursor()
        sql = "INSERT INTO SINGLE_QUESTION_PLUS(follow_num, broswer_num, answer_num, q_content, describes,topic) VALUES (%s, %s, %s, '%s', '%s', '%s')" % (
         follow_num, broswer_num, answer_num, q_content, describe, topic)

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except Exception as e:
            # 如果发生错误则回滚
            db.rollback()
            print(e)
            flag = False
        return flag

    #查询关注数大于2000的问题
    def select_question_more(self,db):#返回的是元组数据类型
        cursor = db.cursor()
        result = ()
        sql = "	SELECT q_content FROM single_question_plus WHERE follow_num > 2000 "
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            db.rollback()
            print(e)
        return result

    #查询问题内容和问题类别
    def select_que_type(self,db,topic):
        result = ()
        cursor = db.cursor()
        sql = "	SELECT q_content,topic FROM SINGLE_QUESTION_PLUS where topic= '%s'" % topic
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            db.rollback()
            print(e)
        return result #返回元组数据类型

    #得到问题的关注数
    def select_follow_num(self,db):
        result = ()

        cursor = db.cursor()
        sql = "	SELECT follow_num FROM SINGLE_QUESTION_PLUS "
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            db.rollback()
            print(e)
        return result  # 返回元组数据类型

    # 得到问题的回答数
    def select_answer_num(self, db):
        result = ()

        cursor = db.cursor()
        sql = "	SELECT answer_num FROM SINGLE_QUESTION_PLUS "
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            db.rollback()
            print(e)
        return result  # 返回元组数据类型

    # 得到问题的浏览数
    def select_broswer_num(self, db):
        result = ()
        cursor = db.cursor()
        sql = "	SELECT broswer_num FROM SINGLE_QUESTION_PLUS "
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            db.rollback()
            print(e)
        return result  # 返回元组数据类型


    def closedb(self, db):
        db.close()

    # def sele(self):
    #      cursor = db.cursor()
    #      sql = "SELECT * FROM QUESTION"
    #      cursor.execute(sql)
    #      results = cursor.fetchall()
    #      print(results)
    #      db.close()
    #
    #  def select(self):
    #      # 使用cursor()方法获取操作游标
    #      cursor = db.cursor()
    #
    #      # SQL 查询语句
    #      sql = "SELECT * FROM %s "
    #      try:
    #          # 执行SQL语句
    #          cursor.execute(sql)
    #          # 获取所有记录列表
    #          results = cursor.fetchall()
    #          for row in results:
    #              fname = row[0]
    #              lname = row[1]
    #              age = row[2]
    #              sex = row[3]
    #              income = row[4]
    #              # 打印结果
    #              print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
    #                    (fname, lname, age, sex, income))
    #      except:
    #          print("Error: unable to fetch data")
    #
    #      # 关闭数据库连接
    #      db.close()
