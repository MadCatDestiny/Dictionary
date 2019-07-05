from Block import Block
import MySQLdb as mysql
from ftplib import FTP
import os
import re

def authorization(email,password):
    conn = mysql.connect(host='localhost', user='root', password='pakistan4898', database='dictionary')
    curs = conn.cursor()
    string = 'SELECT id_user From users Where email = \'{0}\' and password = \'{1}\';'.format(email,password)
    #print(string)
    curs.execute(string)
    try:
         id  = list(curs.fetchone())
    except TypeError:
        print('WRONG LG OR PASS')
        return [0,'WRONG LG OR PASS']
    else:
        print ('WELCOME')
        return [id,'WELCOME']


class Dictionary():
    """
    Describes the class of the custom dictionary
    Provides interaction with database and server
    Contains and manages user blocks
    """
    def __init__(self,id,email,password):
        self.id = id
        self.email = email
        self.password = password
        self.blocks_paths = []
        self.blocks = []

    def load_blocks (self):
        #Get paths from SQL server
        conn = mysql.connect(host='localhost', user='root', password='pakistan4898', database='dictionary')
        curs = conn.cursor()
        string = """SELECT path FROM blocks 
                    JOIN users_blocks ub 
                    ON blocks.id_block = ub.id_block 
                    WHERE id_user in (SELECT id_user From users  Where email = \'{}\');""".format(self.email)
        length = curs.execute(string)
        ls = list(curs.fetchall())
        print(ls)
        for i in range(0,length):
            self.blocks_paths.append(ls[i][0])
            print(self.blocks_paths[i])

        #Load blocks
        rg = re.compile(r'\\\w+\.txt$')
        for i in self.blocks_paths:
            name = rg.search(i).group()
            name = name.split('.')[0]
            name = name[1:]
            print(name)
            b = Block(name)
            self.blocks.append(b)
        print(self.blocks)

        # Download file frome FTP server
        ftp = FTP()
        ip = '192.168.0.105'
        login = 'hb1998'
        psw = 'l0gpass'
        ftp.connect(ip, 21, 10)
        lg = ftp.login(login, psw)
        out = os.getcwd()
        # out = r'C:\Users\hb199\PycharmProjects\ftp_client\F.txt'
        print(out)

        for i in range(0,len(self.blocks_paths)):
            path = out + '\\' + self.blocks[i].name + '.txt'
            print('path: ' + path)
            f = open(path, 'wb')
            ftp.retrbinary('RETR ' + self.blocks_paths[i], f.write)
            f.close()
#------------------------------------For TEST------------------------------------#
id = [0,'']
while id[0] == 0:
    # email = input('Email:')
    # password = input('Password')
    id = authorization('hb1998@ya.ru', 'pakistan4898')

d = Dictionary(id,'hb1998@ya.ru','pakistan4898')
d.load_blocks()

