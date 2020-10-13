from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Michael',
        'title':'Our 1st post',
        'content':'This is the beginning of you new way of communicating with our students and sailing fans',
        'date_posted': 'August 22, 2020'

    },
    {
        'author': 'Mary',
        'title': 'Our 2st post',
        'content': 'Our planned courses shcedule and students info will be avaliable vis this site shortly',
        'date_posted': 'August 29, 2020'

    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

