#001
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(i,price_list[i])

#002
for i in range(3):
    print(i*10+100,price_list[i])

#003
years = 2002
for i in range(13):
    print(years + (i*4))

#004
for i in range(10):
    print(i/10)

#005
ticker = "btc_krw"
print(ticker.upper())

#006
file_name = "보고서.xlsx"
print(file_name.endswith('.xlsx'))

#007
a = "hellow world"
print(a.split())

#008
date = "2020-05-01"
div = date.split('-')
print("Year:",div[0])
print("Month:",div[1])
print("Day:",div[2])

#009
Sam = "5,969,782,550"
print(int(Sam.replace(",","")))

#010
a = "hellow world"
print(a.split())

#011
price = ['20180728','100','130','140','150','160','170']
print(price[1:6])

#012
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[1::2])

#013
lists = [3,100,23,44]
for i in range(4):
    if lists[i]%3 == 0 :
         print(lists[i])