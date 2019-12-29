from django.shortcuts import render
from django.views.generic import TemplateView
from accounts.models import *
from accounts.forms import PointAForm
from django.shortcuts import redirect
from django.http import HttpResponse

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
            achiv = Achievement.objects.get(id=2)
            profile = Profile.objects.get(user=request.user)
            profile.achievement = achiv
            profile.save()
            context = {

                'profile': profile
                 }
            return render(request, 'goals/finsec.html', context)
        elif some_var == ['2']:
            achiv = Achievement.objects.get(id=1)
            profile = Profile.objects.get(user=request.user)
            profile.achievement = achiv
            profile.save()
            context = {

                'profile': profile
            }
            return render(request,  'goals/finstab.html', context)
        elif some_var == ['3']:
            return render(request, 'goals/finind.html')
        elif some_var == ['4']:
            return render(request, 'goals/finfree.html')
        else:
            print("error")
    return render(request, 'goals/money.html')

def finsec(request):
    return render(request,  'goals/finsec.html')


def finsecA(request):
    if request.method == "POST":
        form = PointAForm(request.POST)
        if form.is_valid():
            form.save()


            доходы = form.cleaned_data['income']
            расходы = form.cleaned_data['costs']
            дельта = доходы - расходы
            print(дельта)

            return redirect('/')
        else:
            return HttpResponse(u'Куда прёшь?', status_code=400)
            # post = form.save(commit=False)
            # point_a = form.save(commit=False)
            # point_a.author = request.user
            # point_a.save()
  #  return redirect('post_detail', pk=post.pk)
    else:

        form = PointAForm()
        return render(request, 'goals/finsecA.html', {'form': form})


def finstab(request):

    return render(request, 'goals/finstab.html')

def finind(request):

    return render(request, 'goals/finind.html')

def finfree(request):

    return render(request, 'goals/finfree.html')
