from testData.NewUserData import NewUserData


class AsStudentTestData:
    @staticmethod
    def gen_id(s,e):
        user_ids_answers = []
        for i in range(s,e):
           id = 'TestStudent' + str(i)
           user_ids_answers.append({'ID':id,'dup':1})
           user_ids_answers.append({'ID': id, 'dup': 2})
        return user_ids_answers



