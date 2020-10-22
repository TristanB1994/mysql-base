from sql_base import SQL_Base

class Resource(SQL_Base):
    SQL_Base.__init__(self, "host", "user", "password", "database")

    def insert(self, username, email):
        query = "INSERT INTO users(username, email) VALUES (%s,%s)"
        return self.execute(query, [username, email])
          
    def get(self, username):
        query = "SELECT id, username, email FROM users WHERE username=%s"
        result = self.select_one(query, [username])
        return {'id': result[0],
                'username': result[1],
                'email': result[2]} 
      
    def get_all(self):
        query = "SELECT id, username, email FROM users"
        result = self.select_all(query)
        users = []
        for row in result:
            users.append({'id': row[0],
                          'username': row[1],
                          'email': row[2]})
        return users
 
    def update(self, username, email):
        query = "UPDATE users SET email=%s WHERE username=%s"
        return self.execute(query, [email, username])
          
    def delete(self, username):
        query = "DELETE FROM users WHERE username=%s"
        return self.execute(query, [username])
