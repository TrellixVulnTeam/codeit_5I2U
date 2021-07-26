# 리스트의 값을 변경시켜보기
numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)

# 문자열의 값을 변경시켜보기
name = 'codeit'
name[0] = 'C'
print(name)

# 오류나는 이유가 무엇일까?
#   그것은 바로 리스트는 수정이 가능하지만 문자열은 수정이 불가능하기 때문이다.


# 그렇다면 이코드는 왜 실행이 가능한것인가?
name = 'codeit' + 'it'
print(name)

# 이유는 이 코드는 수정을 한것이아니라 문자열두개를 이용해 새로운 문자열을 생성해내었기 때문이다.