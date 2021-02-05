import pyodbc 
from common import datageneric

class CrudCustomer:   

  def GetCustomers(skip, processDate, currentDateCustomer):
        objDataGeneric= datageneric.Datas()      
        conn= pyodbc.connect(datageneric.Datas.STRING_CONECTION)
        cursor= conn.cursor()
        cursor.execute("SELECT ID_Cliente, RFC, NombreCliente, DiasCredito, ID_Nacionalidad, RegistroCambio, RegistroAlta " 
                        "FROM Corporativo.Clientes WHERE "+
                        objDataGeneric.GetIncrementalInitialLoad(processDate, currentDateCustomer)+
                        "ORDER BY ID_Cliente ASC " + 
                        objDataGeneric.GetPagination(skip))  
       
        return cursor    
