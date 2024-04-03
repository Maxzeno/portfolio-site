from django.shortcuts import render
from django.views import View
from main import models

# Create your views here.


class Index(View):
    def get(self, request):
        profile = models.PortfolioModel.objects.last()
        experiences = models.ExperienceModel.objects.order_by('-show_first')
        projects = models.ProjectModel.objects.order_by('-show_first')
        educations = models.EducationModel.objects.order_by('-show_first')
        tools = models.LanguageToolsModel.objects.order_by('-show_first')
        workflows = models.WorkflowModel.objects.order_by('-show_first')
        interests = models.InterestsModel.objects.order_by('-show_first')
        others = models.OthersModel.objects.order_by('-show_first')
        blogs = models.BlogModel.objects.order_by('-show_first')

        return render(request, 'index.html', {
            'profile': profile,
            'experiences': experiences,
            'projects': projects,
            'educations': educations,
            'tools': tools,
            'workflows': workflows,
            'interests': interests,
            'others': others,
            'blogs': blogs,
        })


class Index2(View):
    def get(self, request):
        profile = models.PortfolioModel.objects.last()
        experiences = models.ExperienceModel.objects.order_by('-show_first')
        projects = models.ProjectModel.objects.order_by('-show_first')
        educations = models.EducationModel.objects.order_by('-show_first')
        tools = models.LanguageToolsModel.objects.order_by('-show_first')
        workflows = models.WorkflowModel.objects.order_by('-show_first')
        interests = models.InterestsModel.objects.order_by('-show_first')
        others = models.OthersModel.objects.order_by('-show_first')

        return render(request, 'index2.html', {
            'profile': profile,
            'experiences': experiences,
            'projects': projects,
            'educations': educations,
            'tools': tools,
            'workflows': workflows,
            'interests': interests,
            'others': others,
        })
