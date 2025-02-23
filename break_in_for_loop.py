monthly_sales = [42,38,33,38,40,45]

month = ["Jan", "Feb", "Mar","Apr", "may","Jun"]

threshold = 35

for sales_amount, month in zip(monthly_sales, month):
    if sales_amount < threshold:
        print(f"sales_amount {sales_amount} is less than threshold in {month}")
        break
    else:
        print(f" Sales amount{sales_amount} is greater than threshold in {month}")



# #
# monthly_Sales2 = [956,320,256,290,480,258,415,478,514,389,547,1200,1580,1458]
#
# threshold2 = 900
#
# for sales_amount2 in monthly_Sales2:
#     if sales_amount2 < threshold2:
#         print(f"f Sales_amount {sales_amount2} is less than threshold")
#         break
#     else:
#         print(f"f Sales_amount {sales_amount2} is greater than threshold")
#
#
#
#
#
#
#
#
