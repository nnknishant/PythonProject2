from Functions.functions_expenses import total_expense_sergey

# def sum_all(*args):
#     total = 0
#     for num in args:
#         total += num
#     return  total
# total = sum_all(1,2,3,4,5,6)
#
# print(total)
# def company_info(**kwargs):
#     if 'tickers' in kwargs:
#         print("Tickers:",kwargs['tickers'])
#     if 'ceo' in kwargs:
#         print("CEO:", kwargs['ceo'])
#     if 'revenue' in kwargs:
#          print("Revenue:", kwargs['revenue'])
# company_info(tickers = 'AAPL', ceo = 'Tim Cook', revenue = "280 billions")

# def company_info(**kwargs):
#     for key in kwargs:
#         print(key, kwargs[key])
#
# company_info(tickers = 'AAPL', ceo = 'Tim Cook', revenue = "280 billions", pe = 200)

# def find_square(a):
#     return a*a
#
# x = lambda a : a*a
# print(x(5))
# print(x(10))
#
#
# x = lambda a , b: a + b
# print(x(5, 6))
# print(x(10, 8))

expenses = [30,45, 70, 90]

total = sum(expenses)
print(total)








