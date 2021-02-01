from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.
from .models import Course, UsersStats
from .models import Card
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import ModelForm
def index(request):
    num_cards = Card.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_cards':num_cards},
    )

class CourseListView(generic.ListView):
    model = Course

class CourseDetailView(generic.DetailView):
    model = Course

class CardListView(generic.ListView):
    model = Card

    def get_queryset(self):
        id = self.kwargs.get('pk')
        return Card.objects.filter(course=id)

class CardDetailView(generic.DetailView):
    model = Card

class CourseCreate(PermissionRequiredMixin, CreateView):
    model = Course
    permission_required = 'courses.can_mark_returned'
    fields = '__all__'

class UserCreate(PermissionRequiredMixin, CreateView):
    model = User
    permission_required = 'courses.can_mark_returned'
    fields = '__all__'