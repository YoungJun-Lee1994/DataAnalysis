#! /usr/bin/env python
#210701
"""
l_range = [1,2,5]
i= '*'
for a in l_range: 
    print(i)
print('done!')

#이러면 for문에 a가 l_range에 걸리는데 거기에는 요소 3개가 있다.
#그래서 print i 를 하면 i가 3번 출력된다.

l_range = [1,2,5]
i= '*'
for a in l_range: 
    print(a)
    print(i)
print('done!')
#이렇게 하면 1*2*3*done! 이렇게 나온다
#for문 안에 if문 넣어보기


l_range = [1,2,5,3,1,7]

for i in l_range:
    #print('current i:', i)
    if i == 1:    # indent required 여기선 i가 1인 애들만 출력했다.
        print(i)
    else :
        #print('not 1!')
        #break
        continue   #아무것도 하지 말고 넘어가라는 명령어
    print('current i:', i) #이거를 여기에 쓰면 1만 출력된다
                           # continue는 나오는 순간 for문 처음으로 돌아간다.                           # 보면 1일 때 print(i)하고 else는 넘어간 다음 print 'current i:' , i 를 실행함 그런데 2같은 경우 else문에 걸려서 continue 때문에 다시 for문으로 돌아간다. 그래서 current i: i 이거 시행이 안됨



print('done!')
"""
"""
print(range(5))  #range(5)는 여기서 다르더라
print(list(range(5)))
#for i in range(2) : #for 문을 두 번 반복해달라는 뜻임.
#    print("*")


print('hello'[0:2])
print('hello'[::-1])
print('0123456789'[0:5:1])
print(list(range(2,5,1)))
range(0,5,1) #range 0부터 5까지라는 뜻이고 맨 뒷자리는 1씩 차이나게 라는 뜻

print(list(range(5,1,-2)))
print(list(range(0,9)))


totalSum = 0
for i in range(0,3,1):
    totalSum += i
    print(i)

print('totalSum:', totalSum)

#pass 와 continue 차이
#pass는 아직 구현 안했는데 test해볼 때 쓰는거다. 실제 사용할 때 pass는 안쓴다
for i in range(3):
    if i == 2:
        print(i)
    else:
        pass
        #continue
    print('current i:', i)


for i,j in enumerate(['a','b','c',[1,2]]): #enumerate쓰면 튜플이 return된다.
    print(i,j)


line 75에 설명 하자면
저 리스트는
0 a
1 b
2 c

잖아. 이거를 enumerate하면
[(0,'a'), (1,'b'), (2,'c')]
라서 75번 줄 결과는 81~83처럼 나온다
enumerate쓰는 이유가 뭐 전체 크기 확인도 하고 인덱스 확인도 할 때 쓴다네

#강사님 이메일 taeyoonkim macrogen python ORCID 검색하면 찾을 수 있다.
#나중에 모르는거 물어봐도 됨
#구구단 출력하기

gugu = input('gugu?')
while not gugu.isdigit():
    gugu = input('gugu is not digit!:')
#print("gugu!!!: ", gugu)
#gugu가 digit이 아닐 때를 미리 처리한거임 이제 이 상태에서 처리하면
gugu = int(gugu)

for i in range(1,10):
    dan = i * gugu
    print('{}*{}: {}'.format(gugu, i, dan))

#2~19 구구단 출력. 강사님도 풀다 넘어감

gugu = input('gugu?')
while not gugu.isdigit()
    gugu = input('gugu is not digit!:')
gugu = int(gugu)
#gugu is integer

while not (2<= gugu <=19):
    gugu = input('[2,19]:')
gugu = int(gugu)

for i in range(1,10):
    dan = i * gugu
    print('{}*{}: {}'.format(gugu, i, dan))
"""
#print(sum([1,2,3]))
"""
#1
total=0
for i in range(101,200,2):
    total += i
print(total)
#2
myList = []
for i in range(101,200):
    if i % 2 == 1: #if문으로 2로 나눴을 때 나머지가 1인 숫자들만 append함.
        myList.append(i)
print(sum(myList))
#3   이건 걍 더한거
print(sum(range(101,200,2)))   

#여기서 인풋 관련한거 물어봐서 설명 추가 
inStr = input('a()b:')
a, b = inStr.split()

myList = []
for i in range(int(a), int(b)):
    if i % 2 == 1:
        myList.append(i)
print(sum(myList))
#여기는 이제 회문구조 판
#여기 다시 한 번 봐라별
inseq = input('Give me sequence!: ') #스트링을 받아온거
s_inseq = ' '.join(inseq)      #join으로 문자 사이를 띄어준 다음
l_inseq = s_inseq.split(' ')   #그럼 이제 ['A','G','C','T'] 리스트가 됨
d_nuc1 = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}
outseq = []
for i in l_inseq[::-1]:
    outseq += d_nuc1[i]
if ( outseq == l_inseq):
    print('{} is palindromic'.format(inseq))
else:
    print('no')
#강사님이 하신거
inseq = input('Give me sequence!: ')
d_nuc1 = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}
outseq = ''
for i in inseq[::-1]:
    outseq += d_nuc1[i]
if (outseq == inseq):
    print('{} is palindromic'.format(inseq))
else:
    print('{} is not palindromic'.format(inseq))

#다른 버젼
inseq = input('Give me sequence!: ')
d_nuc1 = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}

for i in range(len(inseq)):
    print(inseq[i]) #앞에서부터
    print(d_nuc1[inseq[-(i+1)]])  #뒤에서부터complement한거
    if (inseq[i] == d_nuc1[inseq[-i-1]]):
        print('Okay')
    else:
        print('Not a palindromic')


#여기는 잘하긴 했는데 and 1 이라는 결과 데이터를 이후에 사용할 수 없다.
toCount = 'We tried list and we tried dicts also we tried Zen'
l_toCount = toCount.split(' ')
s_toCount = list(set(l_toCount))

for i in s_toCount:
    save = l_toCount.count(i)
    print(i, save)

"""
#그래서 강사님은 이렇게 하신다
#{단어(key):개수(value)} 딕셔너리 만들어서 할거다
"""
toCount = 'We tried list and we tried dicts also we tried Zen'
d_Count = dict()    #이건 빈 딕셔너리 하나 만든거임

l_toCount = toCount.split()

for key in l_toCount: #단어리스트
    #print(key.strip())  #단어 확인

    if key not in d_Count:  #딕셔너리 키 유무
        d_Count[key] = 1    #없으면 1
    else:
        d_Count[key] += 1   #있으면 +1
for i in d_Count:
    print(i, d_Count[i])

for k, v in d_Count.items():
    print(k, v)

#이건 엄청 빠른 라이브러리
#Counter == 딕셔너리 처럼!
#namedtuple -> tuple처럼
from collections import Counter
toCount = 'We tried list and we tried dicts also we tried Zen'

l_toCount = toCount.split()
cnt = Counter(l_toCount)   #cnt 얘는 딕셔너리가 됨

print(cnt)
cnt['tried'] += 100
print(cnt)


#여기서부턴 함수. 파이썬의 영역은 아님.
def showHello():   #def는 함수 선언 () 안은 매개 변수
    print("Hello") #실행코드
    return '1'     #str 1 을 돌려주는 것임
#여기까진 함수가 있다고 선언만 한것

#print(showHello())
a = showHello()             #228에서 str 1 이 231의 showHello(여기) 에 들어감

print("number?")            #이건 그대로 출력된다.
print(a)                    #print(1)의 결과가 나온다 왜냐면 a가 1이기 때문

#a,b는 매개변수
def add(a,b):
    print('add', a, 'and', b)
    print('%d + %d =' % (a,b), a+b)
    return a+b

result = add(3,4)
print('result: ', result)


def add(a, b) -> int : 
    return

print(hello())

def add(a, b=3):   #b 자리에 입력 안하면 기본값3으로 설정하는 거임
    return a+b

print(add(3))
"""
"""
def book_0(name, age, book1, book2):
    print('name : {0} age : {1}'.format(name, age), end = ' ')
    print('book: ', book1, book2)

def book_1(name, age, *books):
    print('name : {0} age : {1}'.format(name, age), end = ' ')
    print('book: ', end = ' ')
    for book in books:
        print(book, end = ' ')
    print()

book_0('yune', 5, 'python', 'basic')
book_1('yune', 5, 'python', 'basic')
book_1('yune', 5, 'python', 'basic', 'photo')

#book_0('yune', 5, 'python', 'basic', 'photo') #error


print('lambda: ', (lambda a, b: a+b ) (3,4))  #람다의 목적은 함수를 짧게 쓰려고. 함수를 한 번 선언하고 밑에 써줘야하는데 람다 쓰면 한번에 출력

def add(a,b) : return a+b

print('add: ', add(3,4))
"""
