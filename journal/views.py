from django.shortcuts import render
from django.urls.base import clear_script_prefix
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from journal.models import Journal
from journal.forms import JournalForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class JournalList(LoginRequiredMixin, ListView):
    model = Journal
    ordering = ['-id']
    paginate_by = 5

class JournalCreate(LoginRequiredMixin, CreateView):
    # model = Journal
    # fields = ['content'] #產生表單僅顯示content的欄位
    form_class = JournalForm
    success_url = '/journal/' #操作成功後重新導向journallist的頁面
    template_name = 'form.html'

class JournalUpdate(LoginRequiredMixin, UpdateView):
    model = Journal #不可刪除 因為會先載入欲修改的紀錄、才放到表單上
    # fields = ['content'] #產生表單僅顯示content的欄位
    form_class = JournalForm
    success_url = '/journal/'
    template_name = 'form.html'

class JournalDelete(LoginRequiredMixin, DeleteView):
    model = Journal
    success_url = '/journal/'
    template_name = 'confirm_delete.html'