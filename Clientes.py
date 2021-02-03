import pyodbc 

limit=500
skip=1

paginacion='OFFSET '+repr((skip-1)*limit) + ' ROWS FETCH NEXT ' + repr(limit)+' ROWS ONLY'

conn= pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=192.168.1.6;'
                        'Database=PQA01;'
                        'UID=sa;'
                        'PWD=123;')
cursor= conn.cursor()

cursor.execute('SELECT ID_Cliente, RFC, NombreCliente, DiasCredito, ID_Nacionalidad, RegistroCambio, RegistroAlta ' 
               'FROM Corporativo.Clientes '
               'ORDER BY ID_Cliente ASC ' +             
               paginacion)               

cnRow=0
 
row = cursor.fetchone() 
while row:   
    cnRow = cnRow +1
    print('Reg. {} -> {}'.format(cnRow,row))
    row = cursor.fetchone()
cursor.close()
   