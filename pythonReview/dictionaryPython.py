arr = [2,6,3,8,4]
arr[0]


emoji_dic = {
':)' : 'happy',
'<3' : 'heart',
':(' : 'not too happy',
'lol' : 'laughing out loud',
'._.' : 'unimpressed',
';)' : 'some creepy person'
}

def dictionary():
    emoji = raw_input("Which emoji would you like me to define? ")
    if (emoji in emoji_dic):
        print 'This means ' + emoji_dic[emoji]
    else:
        print "You either can't spell emojis, of all things, or are totally irrelevant. This emoji does not exist"

dictionary()
#
# print emoji_dic['lol']
# print 'Checking for <3'
# print '<3' in emoji_dic
# print 'Checking for :p'
# print ':p' in emoji_dic

user = users.get_current_user()
if user is None:
    render_dict = {
        'logon' : 'Log In'
    }
else:
   render_dict = {
         'logon' : 'Log Out'
    }
