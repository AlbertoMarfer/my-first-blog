from django import forms

from .models import Post, School



class PostSchool(forms.ModelForm):

    class Meta:
        model = School
        fields = ('name', 'description', 'rating', 'laungagues',)
        
#class PostForm(forms.ModelForm):
#
#    class Meta:
#        model = Post
#        fields = ('title', 'text',)
