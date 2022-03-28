from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, "index.html")

def edit(request):
    if request.method == "POST":
        try:
            edit_file = open(request.POST["filepass"], "r")
            result = {"file": edit_file.read(), "pass": request.POST["filepass"]}
            edit_file.close()
        
        except:
            result = {"ERROR": True}

        return render(request, "edit.html", result)
    
    result = {"ERROR": True}
    return render(request, "edit.html", result)

@csrf_exempt
def override(request):
    if request.method == "POST":
        try:
            edit_file = open(request.POST["pass"], "w")
            edit_file.write(request.POST["edit-file"])
            edit_file.close()
        except:
            return JsonResponse({"res": "ERROR"})
        return JsonResponse({"res": "SUCCESS"})
    return JsonResponse({"res": "ERROR"})