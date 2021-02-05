import pyodbc 
from common import datageneric

class CrudCxcAbonos:
   
    def GetCxcAbonos(skip,processDate, currentDateCustomer):
        objDataGeneric= datageneric.Datas()  
        conn= pyodbc.connect(datageneric.Datas.STRING_CONECTION)
        cursor= conn.cursor()
        cursor.execute('SELECT ID_RU_CXCAbono,ID_CXCCargo,Consecutivo,ID_CACXC,ProcedenciaDocumento,ConceptoCXC,FechaAbono,ID_Moneda,ValorCambio,ID_ZonaIVA ' 
                        ',ID_TasaIVA,PorcentajeIVA,Importe,IVA,RetencionISR,RetencionIVA,TTotal,Observaciones,ID_UsuarioAlta,RegistroAlta,ID_UsuarioCambio '
                        ',RegistroCambio,UI_CXCAbono,RetencionIEPS,IEPS,ID_CXCCargoFactura,ID_RU_CXCAbonoFactura,ID_CFD,EsCancelacion,Bloqueado,ISH,PorcentajeISH '
                        'FROM Facturacion.CXCAbonos WHERE '+
                        objDataGeneric.GetIncrementalInitialLoad(processDate, currentDateCustomer)+
                        'ORDER BY ID_RU_CXCAbono ASC ' +             
                        datageneric.Datas.GetPagination(skip))  
       
        return cursor  