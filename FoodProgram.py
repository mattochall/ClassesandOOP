import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1': ['2/15/2023', 'The Lone Patty', 17, 569],
        'trans2': ['2/15/2023', 'The Octobreakfast', 18, 569],
        'trans3': ['2/15/2023', 'The Octoveg', 16, 570],
        'trans4': ['2/15/2023', 'The Octoburger', 20, 570],
        }


customerid = 570
name = 'Danni Sellyar'
address = '97 Mithcell Way Hewitt Texas 76712'
email = 'dsellyarft@gmpg.org'
phone = '254-555-9362'
memberstatus = False

'''
customerid = 569
name = 'Aubree Himsworth'
address = '1172 Moulton Hill Waco Texas 76710'
email = 'ahimsworthfs@list-manage.com'
phone = '254-555-2273'
memberstatus = True
'''

customer = fc.Customer(customerid, name, address, email, phone, memberstatus)
ordertotal = 0

print()
print(f'Customer Name: {customer.get_name()}')
print(f'Phone: {customer.get_phone()}')

for info in dict.values():
    transaction = fc.Transaction(info[0], info[1], info[2], info[3])

    if transaction.get_customerid() == customer.get_customerid():
        print(
            f'Order Item: {transaction.get_itemname()}  Price: ${transaction.get_cost():.2f}')
        ordertotal += info[2]
print(f'Total Cost: ${ordertotal:.2f}')

if customer.get_memberstatus() == True:
    discount = ordertotal * .2
    newprice = ordertotal - discount
    print(f'Member Discount: ${discount:.2f}')
    print(f'Total Cost after discount: ${newprice:.2f}')

print()
