from django.shortcuts import render

def main_views(request):
    if request.method=="GET":
        return render(request,'main/index.html')

    elif request.method=='POST':

        try:
            amount=int(request.POST['w3school'])
            return render(request,'main/index.html',{'info':info,'posts':posts})
        except :
            pass