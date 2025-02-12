login_flag=False

def login_verify(fn):
    def inner(*args,**kwargs):
        global login_flag
        if login_flag==False:
            print("用户还未完成登录操作")
            while 1:
                username=input("请用户输入用户名")
                password=input("请用户输入密码")
                if username == "admin" and password =="123":
                    print("登录成功")
                    login_flag=True
                    break
                else:
                    print("登录失败")

        ret=fn(*args,**kwargs)
        return ret
    return inner


@login_verify
def add():
    print("添加员工信息")
    
@login_verify     
def delete():
    print("删除员工信息")
    
@login_verify   
def upd():
    print("修改员工信息")
    
@login_verify
def search():
    print("查找员工信息")
    
add()
upd()
delete()
search()