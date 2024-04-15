import pyodbc

class ChatDatabase:

    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-P9I2VIEM\SQLEXPRESS;DATABASE=chats;')
        self.cursor = self.conn.cursor()


    def get_chats(self):
        query = "SELECT * FROM chatInfo"
        self.cursor.execute(query)

        #creating  a result list to append all the data
        result = []
        for i in self.cursor.fetchall():
            persons_dict = {}   #creating a dictionary
            persons_dict["CONTACT NUMBER"] = i[0]
            persons_dict["USER NAME"] = i[1]
            persons_dict["CHAT HISTORY"] = i[2]
            result.append(persons_dict)

        print(result)


    def get_chat(self):
        pass

    def add_chat(self, contact_number,username,chat):
        query = f"INSERT INTO chatInfo(contact_number,username,chat) values('{contact_number}','{username}','{chat}')"
        self.cursor.execute(query)
        self.conn.commit()
        print(query)

    def delete(self,contact_number):
        pass

db = ChatDatabase()
# db.add_chat(contact_number='12309102',username="nkadsoj",chat='293101`cxsdf')
# db.get_chats()
print("db connected")