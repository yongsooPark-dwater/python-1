# 하나의 정수를 입력받아 약수를 출력하는 함수를 만드시오.

def yaksu(num):
   print('약수:')
   for i in range(1, num+1):
       if num%i == 0:
           print(i)

n = int( input('정수입력:'))
yaksu(n)
