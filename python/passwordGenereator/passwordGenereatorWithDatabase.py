import random
import sqlite3 
from datetime import datetime

'''  at least one lower char  
     at least one upper char 
     at least one number
     at least one special chat
     at least 12 chars  
'''  
class generate_password:
  def __init__(self):
    #the charlists
    self.upper_case = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    self.lower_case = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    self.digits = [chr(i) for i in range(ord('0'), ord('9') + 1)]
    self.special_chars = ['!', '#', '<', '>', '?', '}', '{', '(', ')', '[', ']', '&']
    self.use_upper=False
    self.use_lower=False
    self.use_digits=False
    self.use_special=False 
    
     
  def one_uppercase(self):  
        self.use_upper=True
        return random.choice(self.upper_case)
  
  def one_lowercase(self):   
        self.use_lower=True
        return random.choice(self.lower_case)
  
  def one_digits(self):   
        self.use_digits=True
        return random.choice(self.digits)
  
  def one_specialchar(self):   
        self.use_special=True
        return random.choice(self.special_chars)

  def  generate_password(self,length):
   chr_pool= self.upper_case+self.lower_case+self.digits+self.special_chars
   password=[random.choice(chr_pool) for _ in range(length)]
   
   if not self.use_upper:
            idx = random.randint(0, length - 1)
            password[idx] = self.one_uppercase()
   if not self.use_lower:
            idx = random.randint(0, length - 1)
            password[idx] = self.one_lowercase()
   if not self.use_digits:
            idx = random.randint(0, length - 1)
            password[idx] = self.one_digits()
   if not self.use_special:
            idx = random.randint(0, length - 1)
            password[idx] = self.one_specialchar()

   return ''.join(password)



#-------------------------database--------------------#
def create_database():
    conn=sqlite3.connect('passwords.db')
    cursor=conn.cursor()
    cursor.execute(''' 
                  CREATE TABLE if NOT EXISTS passwords(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  password TEXT NOT NULL,     
                  created_at TEXT NOT NULL，
                  website TEXT NOT NULL,    
                  )
                   ''')
    conn.commit()
    conn.close()

def save_password_to_db(password):
    conn=sqlite3.connect('passwords.db')
    cursor=conn.cursor()
    cursor.execute('INSERT INTO passwords(password,created_at) VALUES (?,?)',
                    (password,datetime.now().strftime('%Y-%m-%d %H:%M:%S')))  

    conn.commit()
    conn.close()


create_database()  # 第一次运行时创建表
gp = generate_password()
for _ in range(5):  # 生成 5 个密码并保存
    pwd = gp.generate_password(12)
    save_password_to_db(pwd)
    print("保存密码：", pwd)    








