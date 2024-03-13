from typing import Any
import sqlite3 as sql

class DbTable:
    def __init__(self,file,name,colomn:dict,check_same_thread:bool=True) -> None:
        self.file = file
        self.name = name
        
        self.dataStructure = {"id": int}
        self.dataStructure.update(colomn)
        
        self.conn = sql.connect(self.file,check_same_thread=check_same_thread)
        self.cursor = self.conn.cursor()

        toCommit = f'''CREATE TABLE IF NOT EXISTS {self.name} (id INTEGER PRIMARY KEY'''
        for key in colomn.keys():
            if colomn[key] == int : colomn[key] = 'INTEGER'
            if colomn[key] == str : colomn[key] = 'TEXT'
            if colomn[key] == float : colomn[key] = 'REAL'

            toCommit += f''',{key} {colomn[key]}'''
            
        toCommit += ''')'''
        self.cursor.execute(toCommit)
        self.conn.commit()
        
    def insertData(self, values:dict, duplicate:bool=False) -> None:
        toCommit = f"INSERT INTO {self.name}("

        for key in values:
            toCommit += f'{key},'
        toCommit = toCommit.rstrip(',')
        toCommit += ') VALUES ('

        for key in values:
            toCommit += '?,'
        toCommit = toCommit.rstrip(',')
        toCommit += ')'

        data = []
        alreadyExist = True
        for key in values:
            data.append(values[key])
            alreadyExist = alreadyExist and self.exist(key,values[key])
        data = tuple(data)

        
        if duplicate:
            self.cursor.execute(toCommit,data)
            self.conn.commit()
        elif not alreadyExist:
            self.cursor.execute(toCommit,data)
            self.conn.commit()

    
    def deleteData(self,colomn: str,value: Any):
        # Delete all rows where value of the colomn match the inputed value
        toDelete = f'DELETE FROM {self.name} WHERE {colomn} = ?;'

        self.cursor.execute(toDelete , (value,))
        self.conn.commit()

        if self.cursor.rowcount > 0:
            return True
        else:
            return False
    
    def requestAllData(self):
        select_query = f'''SELECT * FROM {self.name};'''
        self.cursor.execute(select_query)
        rows = self.cursor.fetchall()
        toReturn = []
        for row in rows:
            dict_to_add = {}
            for elem,colName in zip(row,self.dataStructure.keys()): 
                dict_to_add[colName] = elem
            toReturn.append(dict_to_add)
        return toReturn
    
    
    def requestData(self,colomn,value,requestedColomn:str = '*'):
        select_query = f'''SELECT {requestedColomn} FROM {self.name} WHERE {colomn} = ?;'''
        self.cursor.execute(select_query,(value,))
        data = self.cursor.fetchall()
        if data:
            if len(data[0]) == 1:
                return data[0][0]
            else:
                toReturn = {}
                for elem,colName in zip(data[0],self.dataStructure.keys()):
                    toReturn[colName] = elem
                return toReturn
        else:
            return None
    
    def exist(self,colomn:str,value:Any) -> bool:
        select_query = f'''SELECT * FROM {self.name} WHERE {colomn} = ?;'''
        self.cursor.execute(select_query,(value,))
        data = self.cursor.fetchall()
        return True if data else False
    
    def closeConnection(self):
        self.conn.close()