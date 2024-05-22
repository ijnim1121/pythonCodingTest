#큰 수의 법칙 문제
#배열의크기 N, 숫자가더해지는 횟수 M
#다양한 수로 이루어진 배열이 있을 때, 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
#단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없음

#N,M,K를 공백으로 구분하여 입력받기
#n, m, k = map(int, input().split())
n=5
m=8
k=3
#N개의 수를 공백으로 구분하여 입력받기
#data = list(map(int, input().split()))
data=[2,4,5,4,6]
data.sort()  #입력받은 수들 정렬하기
first = data[n-1] #가장 큰 수
second = data[n-2] #두 번째로 큰 수

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)


##횟수를 구해서 최종 답안 출력

#N,M,K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
#N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()  #입력받은 수들 정렬하기
first = data[n-1] #가장 큰 수
second = data[n-2] #두 번째로 큰 수

#가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
#count += m % (k+1)

result2 = 0
result2 += (count) * first
result2 += (m-count) * second

print(result2)
