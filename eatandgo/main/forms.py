from django.forms import ModelForm, Textarea, TextInput, FileInput
from .models import FoodCard


class FoodCardForm(ModelForm):
   class Meta:
      model = FoodCard
      fields = ["title", "image", "sostav", "description", 'price', 'category', 'display_sostav']
      widgets = {
         'title':TextInput(attrs={
            'class':"addtitlefield",
            'placeholder':'Введите название',
         }),
         'description':Textarea(attrs={
            'class':'addtextfield',
            'placeholder':'Введите описание',
         }),
         'price': TextInput(attrs={
            'class':"addpricefield",
            'placeholder':'Введите цену',
         }),
         'sostav':TextInput(attrs={
            'placeholder':'Введите состав',
            'class': 'addsostavfield',
         }),
         'image': FileInput(attrs={
            'class': 'addimagefield'
         }),
      }