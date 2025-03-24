class Singleton:
    """
    单例模式的实现类。

    通过重写 `__new__` 方法确保一个类只有一个实例。
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        控制实例化过程，确保同一类只有一个实例被创建。

        :param args: 类初始化参数（可选）
        :param kwargs: 类初始化关键字参数（可选）
        :return: 单例实例
        """
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

# 示例用法
if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)  # 输出: True


# 写一个加减法
class Calculator:
    def __init__(self):
        self.num = 0
    def add(self, num):
        self.num += num
        #
        return self.num
    def sub(self, num):
        self.num -= num
        #
        return self.num

