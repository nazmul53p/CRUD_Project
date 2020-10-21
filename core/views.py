from django.shortcuts import render, redirect
from .models import Info, EditorialBody


# Create your views here.
def home(request):
    if request.method == 'POST':
        serial = request.POST['Serial']
        information = Info.objects.all().get(serial_no=serial)
        params = {'all': information}
        return render(request, 'index.html', params)
    else:
        return render(request, 'index.html')


def info(request):
    allinfo = EditorialBody.objects.all()
    params = {'all': allinfo}
    return render(request, 'info.html', params)


def students(request):
    if request.method == "GET":
        allinfos = Info.objects.all().order_by('id')
        params = {'all': allinfos}
        return render(request, 'student.html', params)
    if request.method == 'POST':
        name = request.POST.get('Name')
        university = request.POST.get('University')
        topic = request.POST.get('Topic')
        serial = request.POST.get('Serial')
        editorial = request.POST.get('Editorial')
        c = Info(Full_Name=name, university=university, topic=topic, serial_no=serial,
                 editorial_body=editorial)
        c.save()
        return redirect('info')
