# password
password = input(" input your password : ")
confirm = input(" confirm your password : ")
def passw_conf():
    if password == confirm:
        print(" confirmed ")
    else:
        print(" wrong ")
passw_conf()