'''
입력: 0 4 2 5 6
검증수는 각각 5자리숫자를 제곱한 수의 합을 10으로 나눈 나머지 
'''

#입력받기
number = input()
고유번호 = list(map(int,number.split()))
검증수 = (sum(n**2 for n in 고유번호))%10
print(검증수)



