# 함수 선언 부분 #
def multi(v1, v2):
    retList = []    # 반환할 리스트
    res1 = v1 + v2
    res2 = v1 - v2
    res3 = v1 * v2
    res4 = v1 // v2
    res5 = v1 % v2
    res6 = v1 ** v2
    retList.append(res1)
    retList.append(res2)
    retList.append(res3)
    retList.append(res4)
    retList.append(res5)
    retList.append(res6)
    return retList

# 전역 변수 선언 부분 #
myList = []
hap, sub, times, quotient, remain, square = 0,0,0,0,0,0

# 메인 코드 부분 #
myList = multi(100, 20)
hap = myList[0]
sub = myList[1]
times = myList[2]
quotient = myList[3]
remain = myList[4]
square = myList[5]
print("multi()에서 반환한 값 ==> %d, %d, %d, %d, %d, %d" % (hap, sub, times, quotient, remain, square))
