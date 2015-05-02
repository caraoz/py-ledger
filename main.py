import je
import tools
import io

def tb():
    a = []
    for line in open(file['Asset'],'r'):
        a.append(int(line.split('|')[0]))
        
    print('TOTAL ASSETS: ' + str(sum(a)))

q = input('What do you want to do? (1:Journal Entry, 2:Trial balance)')

print('General Journal Entry input format: Asset.Cash 4000')
print('Make sure you use commas in your account names')
q = int(q)
file = {'Asset' : 'assets.txt',
        'Liability':'liability.txt',
        'Expense':'expense.txt',
        'Revenue':'revenue.txt',
        'Equity':'equity.txt',
        'Other':'other.txt'}


if q == 2:
    tb()
else:
    pass


while True:
    dr = input('insert debit, type credit to insert credits\n')
    if dr == 'credit':
        break
    account = dr.split(' ')[0]
    category = account.split('.')[0]
    name = account.split('.')[1]
    amt = dr.split(' ')[1]
    if category == 'Asset':
        f = open(file['Asset'],'a')
        f.write(amt + '|' + name + '\n')
        f.close()
    elif category == 'Expense':
        f = open(file['Expense'],'a')
        f.write(amt + '|' + name + '\n')
        f.close()


while True:
    cr = input('insert credit, type tb to view a trial balance\n')
    if cr == 'tb':
        break
    account = cr.split(' ')[0]
    category = account.split('.')[0]
    name = account.split('.')[1]
    amt = cr.split(' ')[1]
    if category == 'Liability':
        f = open(file['liability'],'a')
        f.write(amt + '|' + name + '\n')
        f.close()
    elif category == 'Revenue':
        f = open(file['Revenue'],'a')
        f.write(amt + '|' + name + '\n')
        f.close()
    elif category == 'Equity':
        f = open(file['Equity'],'a')
        f.write(amt + '|' + name + '\n')
        f.close()




