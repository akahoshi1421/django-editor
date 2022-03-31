from cgitb import text
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from subprocess import run, check_output, STDOUT
import sys

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

@csrf_exempt
def pyexecute(request):
    if request.method == "POST":
        pypass = request.POST["pass"]
        res = check_output("python3 {}".format(pypass), shell=True, stderr=STDOUT)
        result = {"res": res.decode()}
        return JsonResponse(result)
    
    return JsonResponse({"res": "ERROR"})

@csrf_exempt
def gcc(request):
    if request.method == "POST":
        cpass = request.POST["pass"]
        cfile = cpass.split("/")[-1]
        compiledfile = cfile.split(".")
        del compiledfile[-1]
        res = run("gcc -o {} {}".format("".join(compiledfile) ,cpass), capture_output=True, shell=True, text=True)
        result = {"res": res.stderr}
        print(res.stderr)
        return JsonResponse(result)
    
    return JsonResponse({"res": "ERROR"})

@csrf_exempt
def c(request):
    if request.method == "POST":
        cpass = request.POST["pass"]
        compiledfile = cpass.split(".")
        del compiledfile[-1]
        print("".join(compiledfile))
        res = check_output("{}".format("".join(compiledfile)), shell=True, stderr=STDOUT)
        result = {"res": res.decode()}
        return JsonResponse(result)
    
    return JsonResponse({"res": "ERROR"})

@csrf_exempt
def js(request):
    if request.method == "POST":
        pypass = request.POST["pass"]
        res = check_output("node {}".format(pypass), shell=True, stderr=STDOUT)
        result = {"res": res.decode()}
        return JsonResponse(result)
    
    return JsonResponse({"res": "ERROR"})