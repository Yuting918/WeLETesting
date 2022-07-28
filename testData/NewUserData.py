class NewUserData:
    new_student_user = [
        {'ID': 'stu001',
        'f_name': 'StuFName1',
        'l_name': 'StuLName1'},

        {'ID': 'stu002',
         'f_name': 'StuFName2',
         'l_name': 'StuLName2'},

        {'ID': 'stu003',
         'f_name': 'StuFName3',
         'l_name': 'StuLName3'},

        {'ID': 'stu004',
         'f_name': 'StuFName4',
         'l_name': 'StuLName4'},

        {'ID': 'stu005',
         'f_name': 'StuFName5',
         'l_name': 'StuLName5'},

        {'ID': 'stu006',
         'f_name': 'StuFName6',
         'l_name': 'StuLName6'},

        {'ID': 'stu007',
         'f_name': 'StuFName7',
         'l_name': 'StuLName7'},

        {'ID': 'stu008',
         'f_name': 'StuFName8',
         'l_name': 'StuLName8'},

        {'ID': 'stu009',
         'f_name': 'StuFName9',
         'l_name': 'StuLName9'},

        {'ID': 'stu010',
         'f_name': 'StuFName10',
         'l_name': 'StuLName10'},
    ]


    def gen_user(self, role, number):
        new_user = []
        for i in range(1,number):
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
        return new_user


