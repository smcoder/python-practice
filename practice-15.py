class JustCounter:
    __serachCount = 0 # 私有变量
    publicCount = 0 # 公有变量

    def count(self):
        self.__serachCount += 1
        self.publicCount += 1
        print(self.__serachCount)

counter = JustCounter()
counter.count()
counter.count()

print(counter.publicCount)  