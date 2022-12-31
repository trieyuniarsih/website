from django.shortcuts import render
from .forms import ContactForm
from .models import blog

def Data_baru(request):
    if request.POST:
        Form = ContactForm(request.POST, request.FILES)
        if Form.is_valid():
            Form.save()
            Form = ContactForm()
            pesan = "Data Berhasil Diupload"
            context = {
                'Form': Form,
                'pesan': pesan,
            }
            return render(request, 'tambah.html', context)
    else:
        Form = ContactForm()

        context = {
            'Form': Form,
        }

    return render(request, 'tambah.html', context)

def index(request):
    context = {
        'content': 'selamat datang',
    }
    return render(request, 'index.html', context)


def blogs(request):
    blogs = blog.objects.all()

    context = {
        'blogs': blogs,
    }
    return render(request, 'home.html', context)
