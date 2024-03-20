from typing import Any
import sqlite3 as sql

class DbTable:
    def __init__(self,file,name,column:dict,check_same_thread:bool=True) -> None:
        self.file = file
        self.name = name
        
        
        self.conn = sql.connect(self.file,check_same_thread=check_same_thread)
        self.cursor = self.conn.cursor()

        self.dataStructure = {}
        self.dataStructure["id"] = int
        for key,value in column.items():
            self.dataStructure[key] = value
        
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{name}';")
        if not self.cursor.fetchone() is None:
            self.cursor.execute(f"PRAGMA table_info('{name}')")
            for col in self.cursor.fetchall():
                self.dataStructure[col[1]] = col[2]
        
        
        toCommit = f'''CREATE TABLE IF NOT EXISTS {self.name} (id INTEGER PRIMARY KEY'''
        for key in column.keys():
            if column[key] == int : column[key] = 'INTEGER'
            if column[key] == str : column[key] = 'TEXT'
            if column[key] == float : column[key] = 'REAL'

            toCommit += f''',{key} {column[key]}'''
            
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

        data = list(values.values())
        alreadyExist = True
        for key in values:
            alreadyExist = alreadyExist and self.exist(key,values[key])
            if not alreadyExist:
                break
        data = tuple(data)

        
        if duplicate:
            self.cursor.execute(toCommit,data)
            self.conn.commit()
        elif not alreadyExist:
            self.cursor.execute(toCommit,data)
            self.conn.commit()

    
    def deleteData(self,column:str, value:Any):
        # Delete all rows where value of the column match the inputed value
        toDelete = f'DELETE FROM {self.name} WHERE {column} = ?;'

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
    
    
    def requestData(self,column,value,requestedcolumn:str = '*'):
        select_query = f'''SELECT {requestedcolumn} FROM {self.name} WHERE {column} = ?;'''
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
    
    def exist(self,column:str,value:Any) -> bool:
        select_query = f'''SELECT * FROM {self.name} WHERE {column} = ?;'''
        self.cursor.execute(select_query,(value,))
        data = self.cursor.fetchall()
        return True if data else False
    
    def createColumn(self,columnName:str,columnType:Any):
        toCommit = f'''ALTER TABLE {self.name} ADD COLUMN {columnName} {columnType}'''
        self.dataStructure[columnName] = columnType
        self.cursor.execute(toCommit)
        self.conn.commit()
    
    def deleteColumn(self,columnName:str):
        toCommit = f'''ALTER TABLE {self.name} DROP COLUMN {columnName}'''
        self.dataStructure.pop(columnName)
        self.cursor.execute(toCommit)
        self.conn.commit()
    
    def updateStructure(self,newStructure:dict):
        toDelete = []
        for key,value in self.dataStructure.items():
            if key not in newStructure:
                toDelete.append((key,value))
        
        toCreate = []
        for key,value in newStructure.items():
            if key not in self.dataStructure:
                toCreate.append((key,value))
                
        for key, value in toDelete:
            self.deletecolumn(key)
            
        for key,value in toCreate:
            self.createcolumn(key,value)

        
    
    def closeConnection(self):
        self.conn.close()