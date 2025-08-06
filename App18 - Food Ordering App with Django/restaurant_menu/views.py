from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE


class MenuList(generic.ListView):
    # queryset variable stores list of data. Different because it's a ListView
    queryset = Item.objects.order_by("-date_created") # predefined variable
    template_name = "index.html"

    def get_context_data(self, **kwargs): # Name the method exactly like this
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context


class MenuItemDetail(generic.DetailView):
    # Predefined variable
    model = Item
    template_name = "menu_item_detail.html"


