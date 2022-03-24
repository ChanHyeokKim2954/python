#001
from winreg import KEY_READ


letters = 'python'
print(letters[0])
print(letters[2])

#002
string = "PYTHON"
print(string[::-1])

#003
url = "http://sharebook.kr"
name = input("특정 문자열을 입력하시오: ")
index =url.rfind(name)
num = len(name)
print(index)
domain = url[index:index+num]
print(domain)

#004
file_name = "보고서.xlsx"
print(file_name.endswith('xlsx'))

#005
file_names = "2020_보고서.xlsx"
print(file_names.startswith('2020'))

#006
score = int(input("학점을 입력하시오: "))
if 80<score<=100 :
    print("학점: A")
elif 60<score<=80 :
    print("학점: B")
elif 40<score<=60 :
    print("학점: C")
elif 20<score<=40 :
    print("학점: D")
elif 0<score<=20 :
    print("학점: E")

#007
cook = ["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","소시지","라면","팥빙수","김치전"]
print(len(cook))

#008
warn_investment_list = ["Microsoft","Google","Naver","Kakao","SAMSUNG","LG"]
list1 = input("투자 경고 종목을 입력하시오: ")
if warn_investment_list.count(list1) > 0 :
    print("투자 경고 종목입니다.")
else :
    print("투자 경고 종목이 아닙니다")

#009
list2 = [100,200,300]
for i in range(3):
    print(list2[i]+10)

#010
list3 = ["SK하이닉스","삼성전자","LG전자"]
for i in range(3):
    print(len(list3[i]))

