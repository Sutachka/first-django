from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_checked') # что видеть в списке
    list_editable = ('is_checked',) # чтобы ставить галочку прямо в списке