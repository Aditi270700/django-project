from django.shortcuts import render
from .models import Student
from .models import St
from django.http import HttpResponse
# Create your views here.
def landingpage(request):
    adminemail="adity@gmail.com"
    adminpassword="adity"
    email= request.POST.get('email')
    password = request.POST.get('password')
    user=Student.objects.filter(email=email)
    if(email==adminemail and password==adminpassword):
        return render(request,'admindashboard.html')
    if user.exists():
        data=Student.objects.get(email=email)
        pass1=data.password
        if password ==pass1:
            return render(request,'userdashboard.html',{'name':data.name,'email':data.email} )
        else:
            return render(request,'landingpage.html',{'message':'email and password does not match'})
    return render(request,'landingpage.html')
    



def admindashboard(request):
    return render(request,'admindashboard.html')
            
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
            return render(request, 'registration.html', {'msg': x})
        else:
            pass
        if password==cpassword:
            Student.objects.create(name=name,email=email,phone=phone,password=password)
            x = "Resgistration succesfully"
            return render(request,'registration.html',{'msg':x})
        else:
            x = "password and cpassword not match"
            return render(request,'registration.html',{'msg':x,'name':name,'email':email,'phone':phone,})
    else:
        return render(request, 'registration.html')
def logout(request):
    return render(request,'landingpage.html')
   

def table(request):
    stu = Student.objects.all()
    print(stu)
    return render(request,'table.html',{'data':stu})

def delete(request,pk):
    data = St.objects.get(id=pk)
    data.delete()
    stu = St.objects.all()
    return render(request, 'table.html',{'data':stu})

def update(request,pk):
    if request.method=="POST":
         x = Student.objects.get(id=pk)
         p = request.POST.get('name')
         q = request.POST.get('email')
         r = request.POST.get('phone')
         s = request.POST.get('password')
         x.name = p
         x.email = q
         x.phone = r
         x.password = s
         x.save()
         stu=Student.objects.all()
    x=Student.objects.get(id=pk)
    print(x)
    
    return render(request,'update.html',{'data4':x})
    
