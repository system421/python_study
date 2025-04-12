count = 0
def recursive_function():
    global count
    count += 1
    print('재귀함수 호출')
    print(count)
    if(count <10):
        recursive_function()
recursive_function()