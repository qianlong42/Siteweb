import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from Siteweb.models import UserInfo
from django.contrib.auth import authenticate, login as auth_login


# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    # 解析请求中的JSON数据
    data = json.loads(request.body)

    user = data.get("username")
    email = data.get("email")
    password = data.get("password")

    UserInfo.objects.create(username=user, email=email, password=password)

    return JsonResponse({"message": "Félicitations, vous êtes inscrit avec succès."})



def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        print("Username:", username)  # 添加这一行
        print("Password:", password)  # 添加这一行
        user = authenticate(request, username=username, password=password)
        print("Authenticated user:", user)

        if user is not None:
            auth_login(request, user)
            return JsonResponse({"status": "success", "message": "登录成功"})
        else:
            return JsonResponse({"status": "error", "message": "登录失败，用户名或密码不正确"})
    else:
        return render(request, 'user_login.html')



def info_list(request):
    data_list = UserInfo.objects.all()
    print(data_list)

    return render(request,"info_list")


def orm(request):
    #UserInfo.objects.create(username="shuai",email="123@123.com",password="123",)
    #UserInfo.objects.create(username="haha", email="456@456.com", password="456", )
    #UserInfo.objects.create(username="xixi", email="789@789.com", password="789", )
    data_list1 = UserInfo.objects.all()
    for obj in data_list1:
        print(obj.id, obj.username, obj.email, obj.password)
    return HttpResponse('成功')



def info_add(request):
    if request.method == 'GET':
        return render(request,'register.html')
    user = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")

    UserInfo.objects.create(username=user, email=email, password=password, )

    return HttpResponse("添加成功")
