from testData.NewUserData import NewUserData


class AsStudentTestData:
    @staticmethod
    def gen_id_answer(s,e,answers):
        user_ids_answers = []
        for i in range(s,e):
            if i < 10:
                n = '000' + str(i)
            elif 10 <= i < 100:
                n = '00' + str(i)
            elif 100 <=i < 1000:
                n = '0' + str(i)
            else:
                n = str(i)
            for answer in answers:
                user_ids_answers.append({'ID':n,
                                 'Answer':answer})
        return user_ids_answers



