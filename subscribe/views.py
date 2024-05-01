from django.shortcuts import render
from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe

# Create your views here.
def subscribe(request):
    subscribe_form = SubscribeForm()
    err_email = ""
    if request.POST:
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        print("Post request: ", email)
        if email == "":
            err_email = "Please enter email"

        subscribe = Subscribe(first_name=first_name, last_name=last_name, email=email)
        subscribe.save()

    context={"form":subscribe_form ,"err_email":err_email}
    return render(request, 'subscribe/subscribe.html', context)