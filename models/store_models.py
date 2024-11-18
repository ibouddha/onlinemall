#import
from flask import Flask, request
from models.connect import create_connection as conn

class store:
    def __init__(self, id, name, description, location):
        self.id = id
        self.name = name
        self.description = description
        self.location = location
        
    

def getIdByName(name):
    conn = conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM stores WHERE name=%s", (name,))
    store_id = cursor.fetchone()
    cursor.close()
    conn.close()
    return store_id[0]

