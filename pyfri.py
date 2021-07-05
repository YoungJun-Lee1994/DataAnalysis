#! /usr/bin/env python
"""
FILE = open('./test_file.txt', 'r') #이제 file read하면 스트링으로 들어오는걸 알 수 있음.

for i in FILE.readlines(): #[line0, line1, '''']
    #print(i.strip()) #이제 각 라인에서 맨 처음 값만 출력하고 싶으면
    print(i.strip().split()[1])
#파이썬 닫으면 보통 파일은 닫힘
#그런데 같은 파일을 여러 번 열거나 다른 프로그램에서 파일 열려고 할 때
#오류 날 수 있으니까 파일 닫아줘야함.
FILE.close()

FILE = open('./write_file.txt', 'w') #이거 w모드로 열면 열기만 해도 파일 기존 내용 다 날아감.

for i in ['I', 'like', 'an', 'apple']:
    FILE.write(i+' ')
#쓰고 싶은 내용을 FILE.write하고 쓰면 된다
#FILE.write('writeData!!')

FILE.close()

FILE = open('./test_file.txt', 'a') #이거 w모드로 열면 열기만 해도 파일 기>    존 내용 다 날아감.
for i in ['I', 'like', 'an', 'apple']:
    FILE.write(i+' ')

FILE.write('\n')

#파일 매번 닫기 귀찮으니까 while문으로 자동으로 닫게 할 수 있다.

FILE = open('./write_file.txt', 'r') 
with open('./write_file.txt', 'r') as FI:
    for i in FI.readlines():
        print(i.strip())
    print('with out! Bye~')
print('Hi~')  #여기서부터는 파일이 닫힌 상태


#pickle이용

import pickle

l_list = [1, 3, 5, 7]
d_dict = {'a':"A"}  #뭐 여긴 피피티 83 슬라이드 보면 됨

#데이터 처리할 때 형태가 중요한 코딩을 하고 있으면
#우리가 실전에선 약속된 형태가 있는 처리를 하기 때문에 사실 피클 필요는 없음 알아만 두면 될 것 같다.

"""
#class 
#글로 배울 때는 어려운데 나중에 프로그램 커지면 함수 많아진다. 그러면 어디다가 함수 써야할지 모른다. 클래스는 함수 어디다 써야할 지 잘 정할 수 잇는 방법
#다른 언어에서도 쓰인다 
#클래스는 객체 지향 프로그래밍에서 왔다. 
#객체라는 거는 우리가 지금까지 사용했던 문자열, 리스트, 튜플, 세트 등 전부 다 객체다. 
# >>> a = 'apple'
# >>> a
# 'apple'
# >>> a.count('p')
#a라는 객체안에서 객체의 함수인 count를 .으로 붙였다. 이게 클래스...?
#a 치면 'apple'이라는 str data가 나온다
#그런데 a.count라는 함수가 있지. 이 함수는 a라는 객체 안에 숨어있는거다.
#a에는 count라는 함수가 있다. 
#a.split('p')
#a 안에는 split이라는 함수도 있겠지
#그래서 객체 a는 'apple'이라는 데이터를 가지고 있고 split이라는 함수도 가지고 있다. 그래서 a라는 객체에서 'apple'이라는 변수(데이터)고 그게 클래스의 속성이다.
#그리고 split처럼 클래스가 가지고 있는 함수를 메소드라고 함.
#객체랑 인스턴스라는 것도 있다.

#슬라이드 88쪽 보면 클래스의 예시가 나와있다.
#Person이라는 클래스
"""class Person:
    nation = 'A nation'
"""
#class에서는 진짜진짜 지켜야할 불문율
#클래스 명의 첫 캐릭터는 대문자로 시작한다. 이거 DNA complet부분 문제 풀 때 Counter 도 앞에 대문자로 썼었다.
#나 주거욧.... 아니 진짜로 죽는다구요!!

class Person:
    nation = 'A nation'
    def greeting(self):  #greeting은 메소드
        print('(method)greeting: ', 'Hi')
    def hi1(self):
        self.greeting()
    def hi2(self):
        greeting()
"""
def greeting(): #얘는 메소드가 아니라 함수
    print('(function)greeting: ', 'Hello!')
yune = Person()
yune.greeting()
print()
yune.hi1()
yune.hi2()
"""
#init (slide92)
#같은 class의 다른 instance를 쓰는 이유는 걔들이 가지고 있는 속성이 다를 수 있기 때문. 바꾸는 방법은 두 가지
#1. 시작할 때 다르게 지정하던가
#2. 원래 있던걸 바꾸기
#init은 생성자라는 뜻
#__init__ : 초기화 메소드
#인스턴스가 생성될 때 자동으로 초훌됨.
a=1
b='abc' #이것들은 a를 1로 초기화 하고, b를 str abc로 초기화한 것.
#class 클래스:
#    def __init__(self, 매개변수1, 매개변수2):
#        self.속성1 = 매개변수1
#        self.속성2 = 매개변수2
"""
class Person:
    def __init__(self, in_nation):
        self.nation= in_nation

    def showNation(self):
        print(self.nation)
yune = Person('Korea')  #여기 코리아는 in_nation에 들어간다.
yune1 = Person('AAA')

yune.showNation()
yune1.showNation()
"""
#상속 : 클래스를 생성할 때 쓴다.
#다른 클래스에서 ㅇ안에 있는 속성, 메소드를 가지고 올 수 있다.
#언제 사용하냐면, 충분히 잘 짜여져있는 클래스가 있는데 여기서 몇 개 메소드가 필요할 때
#class자식클래스(부모클래스) : 괄호 안에 부모클래스 쓴다.
#메소드 오버라이팅. 부모클래서에서 있는 메소드를 이름은 같은데 다른 기능ㅇ을 하게 하고 싶을 때
#다중상속 : 여러 클래스에서 기능 받아올 수도 있음.
"""
class Cat:
    def __init__(self):
        self.sleepy = True

    def snack(self):
        print('myeo~')

class KoShort(Cat):
    def snack(self):
        print('야옹~')

catcat = Cat()
catcat.snack()
print(catcat.sleepy, end = '\n\n')

meju = KoShort()
meju.snack()
print(meju.sleepy)
"""
#비공개 속성
#self.__비공개속성 으로 사용함 변수명 앞에 언더바 두 개 쓰면 된다
#클래스 안에서만 접근할 수 있다.
#아까 밖에서 슬리피 빼온 것처럼 빼올 수가 없다.
#이거 부가 설명은 나와의카톡에 올린 사진
#학생-점수 클래스 이건 풀어봐~
#사실 어제깢 했던 내용들이 더 중요하다

#모듈은 급하게 설명하고 넘어가심. 피피티에 적어놨다.

#예외처리
fName = input('file name: ')
try:
    FI = open(fName, 'r')
except:
    print('open file', fName, 'failed.')
    exit()
#이거 예시 사진 있는데 봐바. 에러나면 프로그램 종료하지 않고 에러라는거 보여줌. 단점은 어디서 에러났는지 모른대
