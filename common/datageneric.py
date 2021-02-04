

class Datas: 
    __limit=500

    STRING_CONECTION=('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=192.168.1.6;'
                        'Database=PQA;'
                        'UID=sa;'
                        'PWD=123;')
    LIMIT=500 

    @classmethod
    def GetPagination(self, skip):
        return 'OFFSET '+repr((skip-1)* self.__limit) + ' ROWS FETCH NEXT ' + repr(self.__limit)+' ROWS ONLY'          