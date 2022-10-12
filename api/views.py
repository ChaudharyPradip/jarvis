import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.urls import reverse
from .Jarvis import jarvis

def login(req):
    if req.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message" : "Invalid Credentials."
            })
    return HttpResponse("Succesfully logged in")

def logout(req):
    logout(req)
    return HttpResponse("Succesfully logged out")

def register(req):
    return HttpResponse("Succesfully registered")

@csrf_exempt
def ask(req):
    if req.method == "POST":
        response = {}
        response['status'] = 404
        response['message'] = 'Data not found'
        message = json.loads(req.body.decode('utf-8'))['message']
        try:
            res = jarvis.request(message)
            response["status"] = 200
            response["message"] = "Response successfull"
            response["data"] = res
        except Exception as e:
            print(e)
        return JsonResponse(response)
