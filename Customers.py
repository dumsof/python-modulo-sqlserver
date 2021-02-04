from scraper import crud_customers
page:int
page=2
cursor= crud_customers.CrudCustomer.GetCustomers(page)
cnRow=0 
row = cursor.fetchone() 
while row:   
    cnRow = cnRow +1
    print('Reg. {} -> {}'.format(cnRow,row))
    row = cursor.fetchone()
cursor.close()
   
