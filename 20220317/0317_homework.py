#001 print 기초
print("Hellow World")

#002 print 기초
print("Mary's cosmetics")

#003 print 기초
print('선씨가 소리쳤다. "도둑이야".')

#004 print 기초
print('"C:\Windows"')

#005 print 기초
print("안녕하세요. \n만나서\t\t반갑습니다.")
#\n은 줄바꿈이고 \t은 일정간격을 띄워줍니다.

#051 리스트 생성
movie_rank = ["닥터 스트레인지","스플릿","럭키"]
print(movie_rank)

#052 리스트에 원소 추가
movie_rank.insert(3,"배트맨") 
print(movie_rank)

#053
movie_rank.insert(1,"슈퍼맨")
print(movie_rank) 

#058
nums = [1,2,3,4,5]
print(sum(nums))

#059
cook = ["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","소시지","라면","팥빙수","김치전"]
print(len(cook))

#060
avg = sum(nums)/len(nums)
print(avg)

#102
print(3==5) #3과 5는 다르니 거짓

#103
print(3<5) #3은 5보다 작으니 참

#104
x = 4
print(1 < x < 5) #4는 1보다 크고 5보다 작으니 참

#105
print((3==3)) and (4!=3) #3은 3과 같고 4와 다르니 참
