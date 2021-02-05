

class Datas: 

    __limit=500

    STRING_CONECTION=('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=192.168.1.6;'
                        'Database=PQA;'
                        'UID=sa;'
                        'PWD=123;')
    LIMIT=500 

    @classmethod
    def GetIncrementalInitialLoad(self,processDate, currentDateCustomer):
      
        if  processDate=='':
            return "({0} IS NULL AND RegistroAlta <='{1}') OR ({0} IS NOT NULL AND RegistroAlta BETWEEN {0} AND '{1}') OR ({0} IS NOT NULL AND RegistroCambio BETWEEN {0} AND '{1}' AND RegistroAlta>{0}) ".format('NULL', currentDateCustomer)
        else:            
            return "('{0}' IS NULL AND RegistroAlta <='{1}') OR ('{0}' IS NOT NULL AND RegistroAlta BETWEEN '{0}' AND '{1}') OR ('{0}' IS NOT NULL AND RegistroCambio BETWEEN '{0}' AND '{1}' AND RegistroAlta>{0}) ".format(processDate, currentDateCustomer)

    @classmethod
    def GetPagination(self, skip):
        return 'OFFSET '+repr((skip-1)* self.__limit) + ' ROWS FETCH NEXT ' + repr(self.__limit)+' ROWS ONLY'          