from urllib import request
if __name__ == '__main__':
    a=[1,2,5]
    print(a)
    with request.urlopen("http://www.baidu.com") as f:
        print(f.read())