import uuid

def main():
    print("Hello from py-notes!")
    print("测试代码")
    userid = uuid.uuid6()
    print(userid)
    useridV4 = uuid.uuid4()
    print(useridV4)


if __name__ == "__main__":
    main()
