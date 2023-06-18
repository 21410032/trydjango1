from django import forms
from .models import Article

#*****************************model forms******************************#
# Inherits from forms.ModelForm.
#Uses a model class (Article) to automatically generate form fields based on the model's fields.
# Provides built-in validation based on the model's field types and constraints.
# Handles saving form data directly to the model instance using form.save().
# Simplifies form rendering and processing in views and templates.
# Overall, ModelForm provides a more convenient and streamlined approach to working with forms that are closely tied to models.
class ArticleCreate(forms.ModelForm):
    class Meta:
        model=Article
        fields=['title','content']
    def clean(self):
        data=self.cleaned_data
        title=data.get("title")
        qs=Article.objects.all().filter(title__icontains=title)
        if qs.exists():
            self.add_error('title',"Already Exist")
        return data
#**************************simple forms****************************#
# inherits from forms.Form.
# Manually defines form fields (title and content) as form class attributes.
# Requires explicit validation and cleaning of form data in the view or form itself.
# Needs explicit handling of data saving to the model instance.
# Provides more flexibility in defining custom field types or adding extra form fields not directly tied to a model.
# Requires more code and manual validation compared to ModelForm.
# Suitable for simpler forms or cases where tight integration with a model is not needed.
    class ArticleCreateold(forms.Form):
       title=forms.CharField()
       content=forms.CharField()
    #..................................cleaning and validating data................................#

    # def clean_title(self):
    #     cleaned_data=self.cleaned_data
    #     print(cleaned_data)
    #     title=cleaned_data.get('title')
    #     print(title)
    #     if title.lower().strip()=="the office":
    #         raise forms.ValidationError("this title has already been taken")     #forming fiels error
    #     return cleaned_data    
    # def clean(self):
    #     cleaned_data=self.cleaned_data
    #     print(cleaned_data)
    #     title=cleaned_data.get('title')
    #     print(title)
    #     if title.lower().strip()=="the office":
    #         # raise forms.ValidationError("this title has already been taken")       #forming nonfield error
    #         self.add_error('title',"this title has already been taken")
    #     return cleaned_data