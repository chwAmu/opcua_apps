import sqlite3


class dbOperation():
    options = []
    cmds = ''

    def __init__(self, tableName, path='database.db', ):
        # self.tcmd='create table if not exists '
        self.tableName = tableName
        self.dbname = path
        self.conn = self.dbInit()
        self.c = self.dbOper()

    # table layout
    # Tagname---DataType--Node---Comment
    def createTable(self):
        pass

    def createRows(self):
        pass

    # def createRows(self,tagName,DatType,Node,Comment):
    # 	dupliteCounter=0
    # 	dupliteFlag=False
    # 	t=tagName
    # 	while (dupliteFlag==False):
    # 		try:
    # 			self.c.execute(self.rcmd+"('"+t+"','"+DatType+"','"+Node+"','"+Comment+"')")
    # 		#while the current id is existed
    # 		#tag_1-->tag_2-->tag_x
    # 		except sqlite3.IntegrityError:
    # 			t=tagName+'_'+str(dupliteCounter)
    # 			dupliteCounter+=1
    # 		else:
    # 			dupliteFlag=True
    # 	print(dupliteFlag)

    def getTableName(self):
        return self.tableName

    def dbInit(self):
        conn = sqlite3.connect(self.dbname)
        conn.text_factory = str
        return conn

    def dbOper(self):
        return self.conn.cursor()

    def dbCommit(self):
        self.conn.commit()

    def dbClose(self):
        self.conn.close()

    def printAll(self):
        dbrows = self.c.execute("select * from " + self.tableName)
        # dbrows=self.dbSelectWithFilter('p%')
        # print(dbrows.rowcount)
        # show the keys
        for k in dbrows:
            print(k)

    # def dbSelectWithFilter(self,filter):
    # 	self.dbexe("select * from "+self.tableName+' where '+dbOperation.options+ 'like '+"'"+filter+"'")

    def dbSelectAll(self):
        self.dbexe("select * from " + self.tableName)

    def dbRowDelect(self, ele):
        self.dbexe("delete from " + self.tableName + ' where Tagname=' + "'" + ele + "'")

    def dbDelectAll(self):
        self.dbexe("delete from " + self.tableName)

    def dbUpdate(self):
        pass

    def dbexe(self, cmd):
        self.c.execute(cmd)


class stationdb(dbOperation):
    options = ['name', 'ipaddress']

    tablecmds = '''CREATE TABLE IF NOT EXISTS station
             (id INTEGER PRIMARY KEY,
             name Text NOT NULL,
             ipaddress Text NOT NULL)'''

    insertcmds = 'INSERT INTO station(name, ipaddress) VALUES (?,?)'

    deletecmds = 'DELETE FROM station WHERE name ='

    def __init__(self, tableName, path):
        super().__init__(tableName, path)
        self.createTable()

    # override
    def createTable(self):
        self.c.execute(stationdb.tablecmds)

    # override
    def createRows(self, stname, ip):
        try:
            self.c.execute(stationdb.insertcmds, (stname, ip))
        except sqlite3.IntegrityError as e:
            print(e)

    # override
    def dbSelectWithFilter(self, filter):
        print('SELECT * FROM ' + self.tableName + ' where ' + stationdb.options[0] + '=' + filter)
        y = self.c.execute('SELECT * FROM ' + self.tableName + ' where ' + stationdb.options[0] + '=' + "'" + filter + "'")
        print(y)
        for k in y:
            print(k)


    def getStaitonlist(self):
        # y = self.c.execute('SELECT name FROM ' + self.tableName).fetchall()
        y=[]
        y.append(self.c.execute('SELECT name FROM ' + self.tableName).fetchall())
        y.append(list(self.c.execute('SELECT ipaddress FROM ' + self.tableName).fetchall()))
        temp2=[]
        for j in range(len(y)):
            temp1 = []
            for i in y[j]:
                x=''.join(i)
                temp1.append(x)
            temp2.append(temp1)
        return temp2

    def dbRowDelect(self, element):
        self.c.execute(stationdb.deletecmds+" '"+element+"'")

if __name__ == '__main__':
    db1 = stationdb(tableName='station', path='db1.db')
    db1.createTable()
    db1.createRows('station2', '192.168.0.5')
    db1.dbSelectWithFilter('station2')
    db1.dbCommit()
    db1.getStaitonlist()
    db1.dbClose()
