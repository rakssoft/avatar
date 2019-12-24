from django.shortcuts import render
from django.views.generic import TemplateView
from accounts.models import *

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
            # ava = Achievement.objects.get(id=2)
            # print(ava)
            profile = Profile.objects.get(user=request.user)
            context = {
                # 'achievement': achievement,
                'profile': profile
            }
            print("Профиль итд ..." +  profile.achievement.name)
            Profile.achievement = Achievement.objects.get(id=2)
            Profile.achievement._save_parents(Achievement.objects.get(id=2), Profile.achievement)

            print(profile.achievement.name)
            # Profile.achievement.save()


            return render(request, 'goals/finsec.html', context)
        elif some_var == ['2']:
            profile = Profile.objects.get(user=request.user)
            context = {
                # 'achievement': achievement,
                'profile': profile
            }
            print("Профиль итд ..." + profile.achievement.name)
            Profile.achievement = Achievement.objects.get(id=1)
            print(profile.achievement.name)
            Profile.achievement.save()
            return render(request, 'goals/finstab.html')


        elif some_var == ['3']:
            return render(request, 'goals/finind.html')
        elif some_var == ['4']:
            return render(request, 'goals/finfree.html')
        else:
            print("error")
    return render(request, 'goals/money.html')



def finsec(request):
    print("finsecurity")

    profile = Profile.objects.get(user=request.user)
    context = {

        # 'achievement': achievement,
        'profile': profile

    }

    return render(request, 'goals/finsec.html', context,)

def finstab(request):

    return render(request, 'goals/finstab.html')

def finind(request):

    return render(request, 'goals/finind.html')

def finfree(request):

    return render(request, 'goals/finfree.html')
