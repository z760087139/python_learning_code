def test(n):
    result = [2]
    for i in range(0,n):
        k = result[-1]+1
        for c in result:
            if k%c == 0:
                if c != result[-1]:
                    continue
                else:
                    result.add(k)
            else:
                k+1
                break
    print(result)

test(3)