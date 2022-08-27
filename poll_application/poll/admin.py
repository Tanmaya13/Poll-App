from django.contrib import admin

from .models import Poll

class PollAdmin(admin.ModelAdmin):
    list_display = ('userid', 'question' , 'option_one' , 'option_two' , 'option_three' , 'option_four' , 'option_one_count' , 'option_two_count' , 'option_three_count' , 'option_four_count')   
    ordering = ('id',) 

admin.site.register(Poll, PollAdmin)
