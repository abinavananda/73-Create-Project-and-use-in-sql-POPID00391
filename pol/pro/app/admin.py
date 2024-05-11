from django.contrib import admin
from . models import Question, Choice

# Register your models here.

admin.site.register(Question)

class PollAdmin(admin.ModelAdmin):
    list_display =('question','option','vote','image')
admin.site.register(Choice,PollAdmin)
