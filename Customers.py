from scraper import crud_customers

cursor= crud_customers.CrudCustomer.GetCustomers(2)
cnRow=0 
row = cursor.fetchone() 
while row:   
    cnRow = cnRow +1
    print('Reg. {} -> {}'.format(cnRow,row))
    row = cursor.fetchone()
cursor.close()
   
