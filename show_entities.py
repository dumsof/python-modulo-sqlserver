import os
import csv
from scraper import crud_customers,crud_cxcabonos
class ShowEntities:

    def __init__(self) -> None:
        pass


    def ShowData(self,cursor):
         os.system("cls")       
         print('\n------------------------------------------------------------------------------------------------------------------')
         cnRow=0 
         row = cursor.fetchone() 
         if str(row)=='None':           
             print('\nNO EXISTE INFORMACIÓN')
             print('\n------------------------------------------------------------------------------------------------------------------')
             return
         while row:   
             cnRow = cnRow +1
             print('Reg. {} -> {}'.format(cnRow,row))
             row = cursor.fetchone()
         cursor.close()
         print('------------------------------------------------------------------------------------------------------------------\n')


    def startTask(self):
        try:
            swExistPage=True
            countPage=0
            processDate='' 
            currentDateCustomer='2018-12-31 18:10:00'
            while swExistPage:
                countPage+=1
                cursorCxcAbonos=crud_customers.CrudCustomer.GetCustomers(countPage,processDate,currentDateCustomer)
                #print('Cursor numero de fila: ',cursorCxcAbonos.fetchall)
                fp = open(f'Files\\{countPage}.FileCxcAbonos.csv', 'w')
                myFile = csv.writer(fp)
                myFile.writerows(cursorCxcAbonos)
                fp.close()
                print('Cursor numero de fila: ', cursorCxcAbonos )
                swExistPage=False
                print('Ejecución',countPage)
        except Exception as e:
            exception_message = f"Exception cxcabonos startTask: {e}"
            print(exception_message)
            ##log.error(exception_message)



# from scraper import crud_customers,crud_cxcabonos
#objShow=ShowEntities()
# page:int
# page=2
# processDate='' 
# currentDateCustomer='2018-12-31 18:10:00'
# cursorCustomers= crud_customers.CrudCustomer.GetCustomers(page,processDate,currentDateCustomer)
# objShow.ShowData(cursorCustomers)
#---------------------------------------------------------------------------------------------
#cursorCxcAbonos=crud_cxcabonos.CrudCxcAbonos.GetCxcAbonos(page,processDate,currentDateCustomer)
#objShow.ShowData(cursorCxcAbonos)


#poder iniciar la creación de archivos
objShow=ShowEntities()
#---------------------------------------------------------------------------------------------
objShow.startTask()
#---------------------------------------------------------------------------------------------