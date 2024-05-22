n,k=map(int, input().split()) #25 3
count =0
while True:
    #(N==K로 나누어 떨어지는 수)가 될 때까지 1씩 뺴기
    target = (n//k) *k # 8*3=24
    count += (n-target) # 25-24=1
    n=target # n=24
    #N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n<k:
        break
    #K로 나누기
    count += 1
    n//=k

#마지막으로 남은 수에 대하여 1씩 빼기
count  += (n-1)
print(count)