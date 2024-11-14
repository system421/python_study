data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터
key_list = data.keys()
# 값 데이터
value_list = data.values()
print(key_list)
print(value_list)

# 키에 따른 데이터 출력
for key in key_list:
    print(data[key])