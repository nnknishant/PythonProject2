def find_total(expenses):

    '''

    :param expenses: input list containing the numbers
    :return:total sum of all the numbers in the input list
    '''
    
    total = 0
    for expense in expenses:
        total += expense
    return  total



expenses_sergey = [30,45,70,90]
expenses_sunder = [40,23,10,85]

total_expense_sergey = find_total(expenses_sergey)
total_expense_sunder = find_total(expenses_sunder)
print("Total Sergey expense:", total_expense_sergey)
print("Total sunder expense:", total_expense_sunder)
print(help(find_total))