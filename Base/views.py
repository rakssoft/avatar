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