import mmap


FIELDS: list = ['ID_Cliente', 'RFC', 'NombreCliente', 'DiasCredito', 'RegistroAlta', 'RegistroCambio',
                'ID_Nacionalidad', 'GETDATE() AS FechaActual','PedritoEscamoso AS [NombrePedro]','0 as [PedritoEscamoso]','100 as Sapo','100 as [sa]','100 as [desc]']

print('hola')    

result=map(lambda x: x if x.upper().find(' AS ')==-1 else x[x.upper().index('AS')+2:len(x)].strip(), FIELDS)
print(list(result))

#print(FIELDS)

#a = [1,2,3,2,3,4,3,5,6,6,5,4,5,4,3,4,3,2,1]
#result=map(lambda x: x if x != 4 else 'sss', a)

#print(list(result))

#for columm in FIELDS:
#    if (columm.__contains__('AS')):       
#        print(columm.index('AS'))
#        index : int = columm.index('AS') +2
#        print(columm[index : len(columm)].strip())

   