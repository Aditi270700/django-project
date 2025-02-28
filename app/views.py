from django.shortcuts import render
from .models import Student
from .models import St
# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

def registration(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        name=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        print(name,email,phone,password,cpassword)
        user = Student.objects.filter(email=email)
        if user:
            x = "Email already exist"
            return render(request, 'register.html', {'msg': x})
        else:
            pass
        if password==cpassword:
            Student.objects.create(name=name,email=email,phone=phone,password=password)
            x = "Resgistration succesfully"
            return render(request,'login.html',{'msg':x})
        else:
            x = "password and cpassword not match"
            return render(request,'register.html',{'msg':x,'name':name,'email':email,'phone':phone,})
    else:
        return render(request, 'registration.html')
def login(request):
    print(request.method)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = Student.objects.filter(email=email)
        print(user)
        if user:
            data=Student.objects.get(email=email)
            user_data={
                'name':data.name,
                'email':data.email,
                'phone':data.phone,
                'password':data.password,
            }
            print(user_data)
            pass1 = data.password
            if pass1 == password:
                return render(request, 'dashboard.html',{'name':data.name,'email':data.email,'data':user_data})
            else:
                msg = "Email and password not match"
                return render(request, 'login.html',{'msg':msg,'oldemail':email})
        else:
            msg = "Email id not exist"
            return render(request,'login.html',{'msg':msg})  
    else:
        return render(request,'login.html')
    


def table(request):
    stu = St.objects.all()
    print(stu)
    return render(request,'table.html',{'data':stu})

def delete(request,pk):
    data = St.objects.get(id=pk)
    data.delete()
    stu = St.objects.all()
    return render(request, 'table.html',{'data':stu})

# def edit(request,pk):
#     data= St.objects.get(id=pk)
#     stu=St.objects.all()
#     return render(request, 'table.html',{'data':stu,'data1':data})

# def update(request,pk):
#     if request.method=="POST":
#         x = St.objects.get(id=pk)
#         p = request.POST.get('name')
#         q = request.POST.get('email')
#         r = request.POST.get('city')
#         s = request.POST.get('contact')
#         x.stu_city = r
#         x.stu_contact = s
#         x.stu_email = q
#         x.stu_name = p
#         x.save()
#         stu=St.objects.all()
#         return render(request, 'table.html',{'data':stu})
def update(request,pk):
    
    x=St.objects.get(id=pk)
    print(x)
    
    
    
    return render(request,'update.html',{'data4':x})
    # if request.method=="POST":
    #     x = St.objects.get(id=pk)
    #     p = request.POST.get('name')
    #     q = request.POST.get('email')
    #     r = request.POST.get('city')
    #     s = request.POST.get('contact')
    #     x.stu_city = r
    #     x.stu_contact = s
    #     x.stu_email = q
    #     x.stu_name = p
    #     x.save()
    #     stu=St.objects.all()
    #     return render(request, 'table.html',{'data4':stu})
    # # return render(request,'table.html')
