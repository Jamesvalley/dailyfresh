from django.shortcuts import render,redirect
from user.models import User


# Create your views here.


def register(request):
    """  显示注册页面  """
    return render(request, 'register.html')


def register_handle(request):
    """  显示注册页面提交的表单  """
    print('*'*50)

    # 接收数据
    username = request.POST.get('user_name')
    pwd = request.POST.get('pwd')
    email = request.POST.get('email')

    if 1:#not [username,pwd,email]:
        # 数据不完整
        return render(request, 'register.html',{"errmsg":"数据不完整"})
    # 校验用户名
    # 校验pwd
    # 校验email

    return render(request, 'register.html')
