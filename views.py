from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'


def goals(request):

    # product = Product.objects.get()
    # profile = Profile.objects.get(user=request.user)
    # # achievement = Profile.objects.get(achievement=request.user)
    #
    # context = {
    #     'product': product,
    #     # 'achievement': achievement,
    #     'profile': profile
    #
    # }

    return render(request, 'goals/goals.html')

def money(request):
    some_var = request.GET.getlist('checks[]')

    if (request.GET.get('print_btn')):
        if some_var == ['1']:
            return render(request, 'goals/finsec.html')
        elif some_var == ['2']:
            return render(request, 'goals/finstab.html')
        elif some_var == ['3']:
            return render(request, 'goals/finind.html')
        elif some_var == ['4']:
            return render(request, 'goals/finfree.html')
        else:
            print("error")
    return render(request, 'goals/money.html')

def hello(self):
    print('Hello!' )

def finsec(request):
    print("finsecurity")
    return render(request, 'goals/finsec.html')

def finstab(request):

    return render(request, 'goals/finstab.html')

def finind(request):

    return render(request, 'goals/finind.html')

def finfree(request):

    return render(request, 'goals/finfree.html')
