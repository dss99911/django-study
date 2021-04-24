from django.contrib import admin

# Register your models here.
from .models import Question, Choice


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    # by default, it shows str(). with mention of the columns, it shows those columns
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
