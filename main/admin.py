from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.PortfolioModel)
admin.site.register(models.ExperienceModel)
admin.site.register(models.ProjectModel)
admin.site.register(models.EducationModel)
admin.site.register(models.LanguageToolsModel)
admin.site.register(models.WorkflowModel)
admin.site.register(models.InterestsModel)
admin.site.register(models.OthersModel)