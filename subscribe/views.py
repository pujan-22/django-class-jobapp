from django.shortcuts import redirect, render
from django.urls import reverse
from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe

# Create your views here.
def subscribe(request):
    subscribe_form = SubscribeForm(request.POST or None)
    
    err_email = ""
    if request.POST:
        if subscribe_form.is_valid():
            subscribe_form.save()
            # print("valid form")
            # email= subscribe_form.cleaned_data['email']
            # first_name= subscribe_form.cleaned_data['first_name']
            # last_name= subscribe_form.cleaned_data['last_name']
            # print(email, first_name, last_name)
            # subscribe = Subscribe(first_name=first_name, last_name=last_name, email=email)
            # subscribe.save()
            return redirect(reverse('thank_you'))
    context={"form":subscribe_form ,"err_email":err_email}
    return render(request, 'subscribe/subscribe.html', context)

def thank_you(request):
    context={}
    return render(request, 'subscribe/thank_you.html', context)