from django.shortcuts import render

# Create your views here.
def indexpage(request):
    return render(request,"index.html")

def fetchcontactdetail(request):
    uname = request.POST.get('username')
    uemail = request.POST.get('useremail')
    uphone = request.POST.get('userphone')
    umsg = request.POST.get('usermsg')
    content={
       'pname': uname,
        'pmail':uemail,
        'pno':uphone,
        'pmsg':umsg
    }
    return render(request,"index.html",content)