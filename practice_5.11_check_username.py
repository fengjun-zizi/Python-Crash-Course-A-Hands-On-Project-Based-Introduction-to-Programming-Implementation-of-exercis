current_users = ['Apple' , 'Banana' , 'waaa' ,'what' , 'steve jobs' ]
new_users = ['adimn' , 'Banana' , 'dancer' , 'apple pencil' , 'steve jobs']

current_user = [user.lower() for user in current_users]

for new_user in new_users :
    if new_user.lower() in current_user :
        print('次用户名未被使用')
    else :
        print('抱歉，该用户名以使用')