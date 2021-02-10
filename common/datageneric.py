
import os
class Datas: 

    __limit=500

    # STRING_CONECTION=('Driver={ODBC Driver 17 for SQL Server};'
    #                      'Server=192.168.1.6;'
    #                      'Database=PQA;'
    #                      'UID=sa;'
    #                      'PWD=123;')


    STRING_CONECTION=f"Driver={'ODBC Driver 17 for SQL Server'};Server=192.168.1.6;Database=PQA;UID={os.environ['user']};PWD={os.environ['password']};"

    LIMIT=500 

    @classmethod
    def GetIncrementalInitialLoad(cls,processDate, currentDateCustomer):
      
        if  processDate=='':
            return "({0} IS NULL AND RegistroAlta <='{1}') OR ({0} IS NOT NULL AND RegistroAlta BETWEEN {0} AND '{1}') OR ({0} IS NOT NULL AND RegistroCambio BETWEEN {0} AND '{1}' AND RegistroAlta>{0}) ".format('NULL', currentDateCustomer)
        else:            
            return "('{0}' IS NULL AND RegistroAlta <='{1}') OR ('{0}' IS NOT NULL AND RegistroAlta BETWEEN '{0}' AND '{1}') OR ('{0}' IS NOT NULL AND RegistroCambio BETWEEN '{0}' AND '{1}' AND RegistroAlta>{0}) ".format(processDate, currentDateCustomer)

    @classmethod
    def GetPagination(cls, skip):
        return 'OFFSET {0} ROWS FETCH NEXT {1} ROWS ONLY'.format(str((skip-1)* cls.__limit), str(cls.__limit)) 
        