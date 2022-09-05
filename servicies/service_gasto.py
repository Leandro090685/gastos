from email.policy import default
from models.gasto import Gasto
from servicies.service_conect import Conect
from tabulate import tabulate




class ServiceGasto(Conect):
    def __init__(self) -> None:
        self.conn = self.conectar()
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute ("CREATE TABLE gastos (id INT AUTO_INCREMENT, Fecha TEXT, Rubro TEXT, Descripcion TEXT, Monto FLOAT,PRIMARY KEY (id))")
            
        except:
            pass
        
        
        self.conn.commit()
        
        
    def save_gasto(self,gasto:Gasto):
        self.cursor.execute("INSERT INTO gastos VALUES(%s,%s,%s,%s,%s)",(None,gasto.fecha,gasto.rubro,gasto.descripcion,gasto.importe))
        self.conn.commit()
        self.conn.close()

    def get_all_table(self):
        self.cursor.execute("SELECT id, Fecha, Rubro, Descripcion, Monto FROM gastos")
        rta = self.cursor.fetchall()
        tabla = (tabulate(rta, headers=["id","fecha","rubro","descripcion","monto"],tablefmt="pretty"))
        self.conn.commit()
        self.conn.close()
        return tabla
    
    def total(self):
        self.cursor.execute("SELECT Monto From gastos")
        rta = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()
        return rta    
    
    def get_one(self,rubro):
        self.cursor.execute("SELECT * FROM gastos WHERE Rubro LIKE (%s)",(rubro))
        rta = self.cursor.fetchall()
        tabla = (tabulate(rta, headers=["id","fecha","rubro","descripcion","monto"],tablefmt="pretty"))
        self.conn.commit()
        self.conn.close()
        return tabla
    
    def total_rubro(self,rubro):
        self.cursor.execute("SELECT Monto FROM gastos WHERE Rubro LIKE (%s)",(rubro))
        rta = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()
        return rta
    
    def clear_gasto(self,id):
        self.cursor.execute("DELETE FROM gastos WHERE id LIKE (%s)",(id))
        rta = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()
        return rta
                            
        
        
    
    
    
        

        
        
     