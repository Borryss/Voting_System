from django.shortcuts import render



def index(request):
    # data = {
    #     'title': 'Main page',
    #     'values': ['Hello', 'Some']
    # }
    return render(request, 'main/main.html')

