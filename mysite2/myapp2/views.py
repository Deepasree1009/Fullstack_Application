# from django.http import HttpResponse

# def home(request):
#         return HttpResponse("<h1>Welcomeo Django World!!! t</h1>")

# Create your views here.


from django.shortcuts import render
import json
from .models import Register

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse


@csrf_exempt
def reg(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        Fname = data.get("Fname")
        Lname = data.get("Lname")
        Phone = data.get("Phone")
        Email = data.get("Email")
        Password = data.get("Password")

        Register.objects.create(
            Fname = Fname,
            Lname = Lname,
            Phone = Phone,
            Email = Email,
            Password = Password
        )
        return JsonResponse({"message":"Registered Successfully"},status = 201)
    return JsonResponse({"error" : "POST METHOD ONLY"},status=405)







@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        Email = data.get("Email")
        Password = data.get("Password")

        user = Register.objects.filter(
            Email = Email,
            Password = Password
        )

        if user:
            return JsonResponse ({"message" : "Login successfully"})
        else:
            return JsonResponse({"message" : "Invalid Email or password"})
    return JsonResponse({"Error" : "POST method only"})




























@csrf_exempt
def get_all_data(request):
    if request.method=='GET':
         user=Register.objects.all()
         data=[]
         for users in user:
             data.append({
                 "Fname":users.Fname,
                 "lastname":users.Lname,
                 "email":users.Email,
                 "password":users.Password,
                 "phone":users.Phone,

             })

         return JsonResponse({"data":data})
    return JsonResponse({"error":"Only Get Method is allowed"})







@csrf_exempt
def delete_data(request):
        if request.method=="DELETE":
            data=json.loads(request.body.decode("utf-8"))
            id=data.get("id")
            remove=Register.objects.filter(id=id)
            if remove.exists():

                remove.delete()
                return JsonResponse({"Message":"data removed Sucessfully"}) 
            else:
                 return JsonResponse({"error":"data removed unsucessfully"}) 
        return JsonResponse({"error":"data not found"})

        

# @csrf_exempt
# def update_data(request):





















@csrf_exempt
def update_data(request):
    if request.method == "PUT":
        data = json.loads(request.body.decode("utf-8"))
        ID = data.get("id")
        Register.objects.filter(id=ID).update(
        Fname = data.get("Fname"),
        Lname = data.get("Lname"),
        Phone = data.get("Phone"),
        Email = data.get("Email"),
        Password = data.get("Password")

        )

        return JsonResponse({"message" : "Updated Successfully"})
    return JsonResponse({"error":"PUT method only"})


        

        





