from models.connect import create_connection
        
conn = create_connection()

def user_logout(userId):
    cursor = conn.cursor()
    cursor.execute("UPDATE users set status = %s where userId = %s",('offline',userId))
    conn.commit()

