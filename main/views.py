from django.shortcuts import render
from django.views import View
from main import models

from main.forms import ContactForm
# Create your views here.


class Index(View):
    def get_data(self):
        form = ContactForm()

        profile = models.PortfolioModel.objects.last()
        experiences = models.ExperienceModel.objects.order_by('-show_first')
        projects = models.ProjectModel.objects.order_by('-show_first')
        educations = models.EducationModel.objects.order_by('-show_first')
        tools = models.LanguageToolsModel.objects.order_by('-show_first')
        workflows = models.WorkflowModel.objects.order_by('-show_first')
        interests = models.InterestsModel.objects.order_by('-show_first')
        others = models.OthersModel.objects.order_by('-show_first')
        blogs = models.BlogModel.objects.order_by('-show_first')

        return {
            'form': form,
            'profile': profile,
            'experiences': experiences,
            'projects': projects,
            'educations': educations,
            'tools': tools,
            'workflows': workflows,
            'interests': interests,
            'others': others,
            'blogs': blogs,
        }

    def get(self, request):
        return render(request, 'index.html', self.get_data())

    def post(self, request):
        print(request.POST)
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'index.html', self.get_data())
        return render(request, 'index.html', self.get_data())
