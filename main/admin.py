from django.contrib import admin
from main import models

# Register your models here.

admin.site.site_header = 'Profolio Admin'
admin.site.site_title = 'Profolio Admin Portal'
admin.site.index_title = 'Welcome to my profolio'


admin.site.register(models.PortfolioModel)
admin.site.register(models.ExperienceModel)
admin.site.register(models.ProjectModel)
admin.site.register(models.EducationModel)
admin.site.register(models.LanguageToolsModel)
admin.site.register(models.WorkflowModel)
admin.site.register(models.InterestsModel)
admin.site.register(models.OthersModel)
admin.site.register(models.BlogModel)
