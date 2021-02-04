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

page:int
#page=2
#cursorCustomers= crud_customers.CrudCustomer.GetCustomers(page)
#ShowEntities.ShowData(cursorCustomers)
page=74
cursorCxcAbonos=crud_cxcabonos.CrudCxcAbonos.GetCxcAbonos(page)
objShow=ShowEntities()
objShow.ShowData(cursorCxcAbonos)