from django.shortcuts import  render,redirect ,get_object_or_404
from django.http import HttpResponse,HttpRequest
from .models import registration
from .forms import RegistrationForm
# Create your views here.

def list_registration_items(request):
    context={"registration_list":registration.objects.all()}
    return render(request, "registration/test_list.html", context)

def insert_registration_item(request: HttpRequest):
    if request.method == "POST":
        registration1 = registration(
            Firstname=request.POST.get("firstname"),
            Lastname=request.POST.get("lastname"),
            EmailAddress=request.POST.get("emailaddress"),
            Phone=request.POST.get("phone"),
            City=request.POST.get("city"),
            Country=request.POST.get("country"),
        )
        registration1.save()

    return redirect("/registration/list/")

def edit_registration_item(request, id):
    print(id)
    reg = get_object_or_404(registration, id=id)
    if request.method == "POST":
       fm=RegistrationForm(request.POST,instance=reg)
       print(fm)
       if fm . is_valid():
        fm.save()        
        return redirect("/registration/list/")
    
    return render(request, "registration/edit_registration.html",{"registration": reg})

def delete_registration_item (request, id):
   if request.method=="POST":
    
    reg = get_object_or_404(registration, id=id)
    reg.delete()
    return redirect("/registration/list/")

