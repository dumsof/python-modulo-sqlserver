import os
class ShowEntities:

    def __init__(self) -> None:
        pass


    def ShowData(self,cursor):
        #os.system("cls")
        print('\n------------------------------------------------------------------------------------------------------------------')
        cnRow=0 
        row = cursor.fetchone() 
        while row:   
            cnRow = cnRow +1
            print('Reg. {} -> {}'.format(cnRow,row))
            row = cursor.fetchone()
        cursor.close()
        print('------------------------------------------------------------------------------------------------------------------\n')


from scraper import crud_customers,crud_cxcabonos
objShow=ShowEntities()
page:int
page=1
processDate='' 
currentDateCustomer='2018-12-31 18:10:00'
cursorCustomers= crud_customers.CrudCustomer.GetCustomers(page,processDate,currentDateCustomer)
objShow.ShowData(cursorCustomers)
#---------------------------------------------------------------------------------------------
#page=1
#cursorCxcAbonos=crud_cxcabonos.CrudCxcAbonos.GetCxcAbonos(page)
#objShow=ShowEntities()
#objShow.ShowData(cursorCxcAbonos)