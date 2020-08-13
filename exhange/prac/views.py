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
                stock_seller=stocks.objects.get(user=seller)
                stock_buyer=stocks.objects.get(user=buyer)
                if stock=="stock1":
                    stock_seller.stock1-=quantity
                    stock_buyer.stock1+=quantity
                    stock_seller.save()
                    stock_buyer.save()
                elif stock=="stock2":
                    stock_seller.stock2-=quantity
                    stock_buyer.stock2+=quantity
                    stock_seller.save()
                    stock_buyer.save()
                return redirect('prac:home')
        except ObjectDoesNotExist:
            messages.error(self.request, "fill the form correctly")
            return redirect("prac:home")