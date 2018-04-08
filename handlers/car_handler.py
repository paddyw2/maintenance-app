import mysql.connector

class car_handler:

  def connect_db(self):
    """
    You can test db connection using this code
    Make sure the mysql server is running and replace
    test_env with a database you created.
    """
    cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='471_project')
    return cnx

  def close_connection(self, cursor, cnx):
    cursor.close()
    cnx.close()

  def select_query(self,user_input):
    return ["these", "are", "the", "results"]

  def insert_query(self, values):
    return True

  def update_query(self, values):
    return True

  def delete_query(self, values):
    return True

  def insert_values(self, query):
    cnx = self.connect_db()
    cursor = cnx.cursor()
    cursor.execute(query)
    cnx.commit()
    self.close_connection(cursor, cnx)


  def select_query_values(self, query):
    cnx = self.connect_db()
    cursor = cnx.cursor()
    cursor.execute(query)
    return_values = []
    for row in cursor:
      return_values.append(row)
    self.close_connection(cursor, cnx)
    return return_values

