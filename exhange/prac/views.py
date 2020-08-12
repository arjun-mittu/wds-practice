from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .forms import trade_form
from .models import trade,stocks
class home(ListView):
    def get(self, *args, **kwargs):
        form=trade_form
        context = {
            'form':form
        }
        return render(self.request, "index.html", context)
    def post(self,*args, **kwargs):
        form = trade_form(self.request.POST or None)
        try:
            if form.is_valid():
                seller= form.cleaned_data.get('seller')
                quantity= form.cleaned_data.get('quantity')
                stock= form.cleaned_data.get('stock')
                buyer= form.cleaned_data.get('buyer')
                trade_do= trade.objects.create(
                    seller=seller,
                    quantity=quantity,
                    stock=stock,
                    buyer=buyer,
                )
                #Contestant.objects.filter(answer='1').update(age=SqlClause('age+2'))
                stock_seller=stocks.objects.filter(user=seller)
                print(stock_seller)
                for i in stock_seller:
                    print(i.get_attname_column())
                stock_buyer=stocks.objects.filter(user=buyer)
                print(stock_buyer)
                #contact_me.save()
                return redirect('prac:home')
        except ObjectDoesNotExist:
            messages.error(self.request, "fill the form correctly")
            return redirect("prac:home")