from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .models import TeachersInfo
# Create your views here.
def index(request):
    return render(request,"Teachers/index.html")

#Register new teachers views
def Alta(request):
    return render(request,"Teachers/registerTeachers.html")

def NewTeacher(request):
    newT = TeachersInfo(name=request.POST['newName'], lastname1=request.POST['newLastName1'], lastname2=request.POST['newLastName2'],
                        age=request.POST['newAge'], maleOrFemale=request.POST['sexo'], contractType=request.POST['contractType'])
    newT.save()
    
    return HttpResponseRedirect(reverse('Teachers:details', args=(newT.pk,)))

#Update teachers info views
def Update(request, teacher_id):
    teacher_info = get_object_or_404(TeachersInfo, pk=teacher_id)
    return render(request,"Teachers/update.html",{'teacher':teacher_info})

def SaveUpdate(request, teacher_id):
    teacher = get_object_or_404(TeachersInfo, pk=teacher_id)
    
    teacher.name = request.POST['newName']
    teacher.lastname1 = request.POST['newLastName1']
    teacher.lastname2 = request.POST['newLastName2']
    teacher.age = request.POST['newAge']
    teacher.maleOrFemale = request.POST['sexo']
    teacher.contractType = request.POST['contractType']

    teacher.save()
    
    return HttpResponseRedirect(reverse('Teachers:details',args=(teacher.pk,)))

#Delete teachers views
def Delete(request, teacher_id):
    TeachersInfo.objects.filter(pk=teacher_id).delete()
    return HttpResponseRedirect(reverse('Teachers:search'))
    
#Visualize info views
def Search(request):
    allTeachers = TeachersInfo.objects.all()
    return render(request,"Teachers/search.html",{"teachers_list": allTeachers})
    
def Details(request, teacher_id):
    teacher = get_object_or_404(TeachersInfo, pk=teacher_id)
    return render(request,"Teachers/details.html",{"teacher":teacher})


#test view
def navbar(request):
    return render(request,"Teachers/registerTeachers.html")