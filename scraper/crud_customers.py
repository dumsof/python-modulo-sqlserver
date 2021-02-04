import pyodbc 
from common import datageneric

class CrudCustomer:
   
    def GetCustomers(skip):
        conn= pyodbc.connect(datageneric.Datas.STRING_CONECTION)
        cursor= conn.cursor()
        cursor.execute('SELECT ID_Cliente, RFC, NombreCliente, DiasCredito, ID_Nacionalidad, RegistroCambio, RegistroAlta ' 
                        'FROM Corporativo.Clientes '
                        'ORDER BY ID_Cliente ASC ' +             
               datageneric.Datas.GetPagination(skip))  
       
        return cursor       


