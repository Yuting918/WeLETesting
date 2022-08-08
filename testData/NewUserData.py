class NewUserData:
    new_student_user = [{'ID': 'Stu012', 'f_name': 'StuFName012', 'l_name': 'StuLName012'}, {'ID': 'Stu013', 'f_name': 'StuFName013', 'l_name': 'StuLName013'}, {'ID': 'Stu014', 'f_name': 'StuFName014', 'l_name': 'StuLName014'}, {'ID': 'Stu015', 'f_name': 'StuFName015', 'l_name': 'StuLName015'}, {'ID': 'Stu016', 'f_name': 'StuFName016', 'l_name': 'StuLName016'}, {'ID': 'Stu017', 'f_name': 'StuFName017', 'l_name': 'StuLName017'}, {'ID': 'Stu018', 'f_name': 'StuFName018', 'l_name': 'StuLName018'}, {'ID': 'Stu019', 'f_name': 'StuFName019', 'l_name': 'StuLName019'}]


    def gen_user(self, role,s,e):
        new_user = []
        for i in range(s,e):
            if i < 10:
                n = '00' + str(i)
            elif 10 <= i < 100:
                n = '0' + str(i)
            else:
                n = str(i)

            new_user.append({
                'ID': role + n,
                'f_name': role + 'FName' + n,
                'l_name': role + 'LName' + n
            })
        print(new_user)
        return new_user


