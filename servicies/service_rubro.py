from servicies.service_conect import Conect
from models.rubro import Rubro
from tabulate import tabulate


class ServiceRubro(Conect):
    def __init__(self):
        self.conn = self.conectar()
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute ("CREATE TABLE rubros (codigo INT AUTO_INCREMENT,rubros TEXT,PRIMARY KEY (codigo))")
        except:
            pass
        
        self.conn.commit()
       
    
    def save(self,rubro:Rubro):
        self.cursor.execute("INSERT INTO rubros VALUES(%s,%s)",(None,rubro.name))
        self.conn.commit()
        self.conn.close()
        return True
    
    def get_all(self):
        self.cursor.execute("SELECT rubros FROM rubros")
        rta = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()
        return rta
    
    def clear_rubro(self,rubro:str):
        self.cursor.execute("DELETE FROM rubros WHERE rubros LIKE(%s)",(rubro))
        self.conn.commit()
        self.conn.close()
        return True 
    
   
    
    
        
        
    
        
    
        

