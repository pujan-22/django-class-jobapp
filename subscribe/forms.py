from django import forms

from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _

class SubscribeForm(forms.ModelForm):
    use_required_attribute = False
    class Meta:
        model=Subscribe
        fields='__all__'
        # exclude=('first_name',)

        labels={
            'first_name':_('Enter first name'),
            'last_name':_('Enter last name'),
            'email':_('Enter Email')
        }
        error_messages={
            'first_name':{
                'required':_('Enter first name')
            }
        }
        

# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError("Invalid last name")
#     return value

# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100, validators=[validate_comma])
#     email = forms.EmailField(max_length=100)

#     def clean_first_name(self):
#         data = self.cleaned_data['first_name']
#         if ',' in data:
#             raise forms.ValidationError("Invalid first name")
#         return data