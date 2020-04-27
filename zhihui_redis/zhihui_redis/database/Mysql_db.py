import pymysql


# mysql数据库操作
class mysql:
    def connection(self):
        db = pymysql.connect("localhost", "root", "123456", "zhihu_data")
        # print("succeed")
        return db

    def insert_answer(self, db, voteup_num, comment_num, a_content, a_q_id):
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 插入语句
        sql = "INSERT INTO ANSWER(voteup_num, comment_num, a_content, q_id) VALUES (%s, %s, '%s', %s)" % (
         voteup_num, comment_num, a_content, a_q_id)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except Exception as e:
            # 如果发生错误则回滚
            db.rollback()
            print(e)

    def insert_question(self, db, id, follow_num, broswer_num, answer_num, q_content, describe):
        cursor = db.cursor()
        sql = "INSERT INTO QUESTION(q_id,follow_num, broswer_num, answer_num, q_content, describes) VALUES (%s, %s, %s, %s, '%s', '%s')" % (
        id, follow_num, broswer_num, answer_num, q_content, describe)

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except Exception as e:
            # 如果发生错误则回滚
            db.rollback()
            print(e)

    #查询关注数前百分之十的问题
    def select_ten_question(self,db):#返回的是元组数据类型
        cursor = db.cursor()
        sql = "SELECT g.q_content FROM (SELECT @rownum:=0) r join question g where  (@rownum:=@rownum+1)<=(select round(count(*)*0.1) from question) ORDER BY follow_num;"

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            db.rollback()
            print(e)
        return result


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
