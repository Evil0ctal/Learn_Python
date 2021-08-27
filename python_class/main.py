class Users():
    """创建一个简单地用户类，包含姓名，生日属性"""

    # 初始化类属性
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = (first_name + ' ' + last_name).title()

    # 简单概括用户信息
    def describe_user(self):
        print('Name: %s Age: %s' % (self.full_name, self.age))

    # 打印一条友好的问候
    def greet_user(self):
        print("Nice to meet you %s. Hope you enjoy the Python!" % self.full_name)


def main():
    # 创建Users类的实例
    user = Users('Adam', 'Tan', 20)
    # 调用Users类的describe_user()方法
    user.describe_user()
    user.greet_user()
    # 打印格式化后的全名
    print(user.full_name)

if __name__ == '__main__':
    main()