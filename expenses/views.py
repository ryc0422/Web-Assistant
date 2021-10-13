from django.db import models
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from expenses.models import Expense
from expenses.forms import ExpenseForm

# Create your views here.
#支出紀錄列表
class ExpenseList(LoginRequiredMixin, ListView):
    model = Expense
    ordering = ['-id']
    paginate_by = 5

#新增支出紀錄
class ExpenseCreate(LoginRequiredMixin, CreateView):
    # model = Expense
    # fields = '__all__'
    form_class = ExpenseForm
    template_name = 'form.html'
    def get_success_url(self):
        return reverse('expense_list')

#修改支出紀錄
class ExpenseUpdate(LoginRequiredMixin, UpdateView):
    model = Expense
    #fields = '__all__'
    form_class = ExpenseForm
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('expense_list')

#刪除支出紀錄
class ExpenseDelete(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = 'confirm_delete.html'
    def get_success_url(self):
        return reverse('expense_list')



