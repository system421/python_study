def recursive_function(i):
    if i == 100:
        return
    print(i,'번째 재귀함수에서',i+1,'번째 재귀함수 호출')
    recursive_function(i+1)
    print(i,'번째 재귀 함수 종료')

recursive_function(1)