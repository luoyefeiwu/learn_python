


try:
    f = open('test.txt', 'r', encoding='utf-8')
    print(f.read())
finally:
    if f:
        f.close()
