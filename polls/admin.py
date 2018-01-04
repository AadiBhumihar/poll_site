from django.contrib import admin

from .models import Question ,Choice;

# Register your models here.

class ChoiceInline(admin.TabularInline) :
    model = Choice ;
    extra = 3


class QuestionAdmin(admin.ModelAdmin) :
    fieldsets = [
        (None ,     {'fields':['question_text']}),
        ('Date_Information',    {'fields':['pub_feild'],'classes':['collapse']}),
        ]

    inlines = [ChoiceInline] ;

    list_display = ('question_text','pub_feild','was_published_recently')



admin.site.register(Question,QuestionAdmin)
