# password
password = input(" input your password : ")
confirm = input(" confirm your password : ")
def passw_conf():
    if password == confirm:
        print(" confirmed ")
    else:
        print(" wrong ")
passw_conf()

# passw v 1.1
def pas_conf(a, b):
    a = input(" input your password : ")
    b = input(" confirm your password : ")
    if a == b:
        print(" confirmed ")
    else:
        print(" wrong ")
pas_conf("passw", "conf")
