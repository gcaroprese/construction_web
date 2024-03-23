from django.views.generic import (ListView, DetailView)
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from utils.views import MobileAwareTemplateMixin

from .models import Project

# --------------------------------------------------------------------------------------------------

class ProjectListView(MobileAwareTemplateMixin, ListView):
    context_object_name = 'projects'

    template_name = 'projects/list.html'
    mobile_template_name = 'projects/mobile-list.html'

    def get_queryset(self):
        return Project.objects.active()

# --------------------------------------------------------------------------------------------------

class ProjectDetailView(MobileAwareTemplateMixin, DetailView):
    context_object_name = 'project'

    template_name = 'projects/detail.html'
    mobile_template_name = 'projects/mobile-detail.html'

    def get_queryset(self):
        return Project.objects.active()

    def get_object(self, queryset=None):
        return get_object_or_404(self.get_queryset(), slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)

        paginator = Paginator(self.get_queryset(), 1)
        project_index = list(self.get_queryset()).index(self.object)
        current_page = paginator.page(project_index + 1)

        next_project = self.get_queryset().first()
        if current_page.has_next():
            next_project = paginator.page(current_page.number + 1).object_list.first()

        previous_project = self.get_queryset().last()
        if current_page.has_previous():
            previous_project = paginator.page(current_page.number - 1).object_list.first()

        context.update({
            'next_project': next_project,
            'previous_project': previous_project
        })
        return context

# --------------------------------------------------------------------------------------------------


