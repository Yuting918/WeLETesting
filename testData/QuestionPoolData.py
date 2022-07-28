class QuestionPoolData:
    @staticmethod
    def pool_name_generator(number):
        pool_names = []
        for i in range(number):
            if i < 10:
                n = '00' + str(i)
            elif 10 <= i < 100:
                n = '0' + str(i)
            else:
                n = str(i)
            name = 'TestPool' + n
            pool_names.append(name)
        return pool_names