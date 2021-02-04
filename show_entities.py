class ShowEntities:

    def ShowData(cursor):
        print('clc')
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
page=1
cursorCxcAbonos=crud_cxcabonos.CrudCxcAbonos.GetCxcAbonos(page)