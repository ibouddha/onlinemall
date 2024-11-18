from models.connect import create_connection

class users:
    def __init__(self, name, surname, username, email, password, role, status, store_id):
        self.name = name
        self.surname = surname
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.status = status
        self.store_id = store_id
    

def checkConnection(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM users WHERE username=%s", (username,))
    user_data = cursor.fetchone()
    cursor.close()
    close_connection(conn)
    
    if user_data == 'online':
        return True
    else:
        return False
    

def save(user):
    conn = create_connection()
    cursor = conn.cursor()
    if(user.role != "admin" and user.store_id == 0):
        return "Error: Store ID is required for non-admin users"
    else:
        cursor.execute("INSERT INTO users (name, surname, username, email, password, role, status, store_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (user.name, user.surname, user.username, user.email, user.password, user.status, user.store_id))
        conn.commit()
        cursor.close()
        close_connection(conn)
        return "Success: User registered successfully!"
    
def getLoggedUser(email,password):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
        user_data = cursor.fetchone()
        
    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)
        return error
        
    if user_data:
        return user_data
    else:
        return None
        
    
def get_user_role(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM users WHERE username=%s", (username,))
    user_data = cursor.fetchone()
    cursor.close()
    print(user_data)
    if user_data:
        return user_data[0]
    else:
        return None
    
#save registered user
# def addUser(user):

def update_status(username):
    cursor = conn.cursor()
    cursor.execute("UPDATE users set status = %s where username = %s",('online',username))
    conn.commit()