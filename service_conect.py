import pymysql

class Conect:
    def __init__(self) -> None:
        pass
     
    def conectar(self):
        conn = pymysql.connect (host ="localhost", port = 3306, user = "root", passwd = "", db = "Gastos")
        
        conn.close
        
        return conn
    
    def conectar_csv(self,modo):
        f = open("registros.csv",{modo})
        f.close()

a = Conect()
a.conectar_csv(a)
        
        
       
    
