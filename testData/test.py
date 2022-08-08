def gen_user(role, s, e):
    new_user = []
    for i in range(s, e):
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

gen_user('Stu',12,20)