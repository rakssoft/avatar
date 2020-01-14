from django.shortcuts import render
from django.views.generic import TemplateView
from accounts.models import *
from accounts.forms import PointAForm, IncomeDailyForm
from django.shortcuts import redirect
from django.http import HttpResponse
from Base.models import PointA, IncomeDaily
from collections import Counter

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
            achiv = Achievement.objects.get(id=1)
            profile = Profile.objects.get(user=request.user)
            profile.achievement = achiv
            profile.save()
            context = {

                'profile': profile
                 }
            return render(request, 'goals/finsec.html', context)
        elif some_var == ['2']:
            achiv = Achievement.objects.get(id=2)
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
            доходы = form.cleaned_data['income']
            расходы = form.cleaned_data['costs']
            долги = form.cleaned_data['debts']
            активы = form.cleaned_data['assets']
            дельта = доходы - расходы
            капитал = активы - долги
            # print(дельта)
            b = PointA(capital=капитал, debts=долги, costs=расходы)
            c = PointA.objects.all()
            c.delete()
            b.save()
            return redirect('/Base/money/finsecurity')
        else:
            return HttpResponse(u'Куда прёшь?', status_code=400)
    else:
        form = PointAForm()

        return render(request, 'goals/finsecA.html', {'form': form})

def fin_daily(request):
    if request.method == "POST":
        form_daily = IncomeDailyForm(request.POST)
        if form_daily.is_valid():
            доходы_в_день = form_daily.cleaned_data['income_daily']
            подушка_безопасности = form_daily.cleaned_data['pillow_all']
            долги_итог = form_daily.cleaned_data['debts_all']

            form_daily.save()
            return redirect('/Base/money/findaily')
        else:
            return HttpResponse(u'Куда прёшь?', status_code=400)
    else:
        form_daily = IncomeDailyForm()
        all_pointb = IncomeDaily.objects.all()
        income_day = all_pointb.last().income_daily
        # pillow_all = sum(all_pointb.values('pillow_all'))
        all = all_pointb.values('pillow_all')
        # for value in all.values():
        #     print(value)
        #     print(key)

        total_pillow = Counter()
        for d in all:
            total_pillow.update(d)
            print(total_pillow)

            # total_pillow =total_pillow + value  # Accumulate the values in total_income

    #    return render(request, 'goals/findaily.html', {'form': form_daily})
        return render(request, 'goals/findaily.html', {'form': form_daily, 'income_day': income_day, 'total_pillow':total_pillow})

def finsecurity(request):
    all_pointb = IncomeDaily.objects.all()
    profile = Profile.objects.get(user=request.user)
    all = PointA.objects.all()
    cost = all[0].costs    # расоходы
    point_capital = all[0].capital
    dbs = PointA.objects.all()
    db = dbs[0].debts  # долг общий
    pillow = cost*6    # подушка  умноженная на 6 расходов
    context = {

        'pillow': pillow,
        'profile': profile,
        'db': db,
        'point_capital': point_capital
    }
    return render(request, 'goals/finsecurity.html', context)

def finstab(request):

    return render(request, 'goals/finstab.html')

def finind(request):

    return render(request, 'goals/finind.html')

def finfree(request):

    return render(request, 'goals/finfree.html')