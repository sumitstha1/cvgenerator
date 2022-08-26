from multiprocessing import context
from django.shortcuts import render, redirect

from app_cvgenerator.forms import UserCvForm
from .models import User

# Create your views here.
def cv_index(request):
    users = User.objects.all()
    context = {'users': users}
    template = 'cvgen/index.html'
    return render(request, template, context)

def cv_create(request):
    create_form = UserCvForm
    context = {'form': create_form}
    if request.method == 'POST':
        user = User()

        user.first_name = request.POST.get('first_name')
        user.middle_name = request.POST.get('middle_name')
        user.last_name = request.POST.get('last_name')
        user.contact = request.POST.get('contact')
        user.email = request.POST.get('email')
        user.dob = request.POST.get('dob')
        user.quali = request.POST.get('quali')
        user.hobby = request.POST.get('hobby')
        user.objective = request.POST.get('objective')

        user.save()

        context.setdefault("msg", "Successfully Added")
        template = 'cvgen/create.html'
        return render(request, template, context)
    template = 'cvgen/create.html'
    return render(request, template, context)

def cv_show(request, id):
    template = 'cvgen/show.html'
    users = User.objects.get(id=id)
    context = {'users': users}
    return render(request, template, context)

def cv_edit(request, id):
    user = User.objects.get(id=id)
    template = 'cvgen/edit.html'
    context = {'user': user}
    return render(request, template, context)

def cv_update(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST.get('id'))

        user.first_name = request.POST.get('first_name')
        user.middle_name = request.POST.get('middle_name')
        user.last_name = request.POST.get('last_name')
        user.contact = request.POST.get('contact')
        user.email = request.POST.get('email')
        user.dob = request.POST.get('dob')
        user.quali = request.POST.get('quali')
        user.hobby = request.POST.get('hobby')
        user.objective = request.POST.get('objective')
        user.user_id = 1

        user.save()

        return redirect('cv.index')
    return redirect('cv.index')

def cv_delete(request, id):
    user = User.objects.get(id=id)
    user.delete()

    return redirect('cv.index')