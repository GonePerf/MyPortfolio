from django.forms import ModelForm
from .models import Tool

class ToolForm(ModelForm):
    class Meta:
        model = Tool
        fields = '__all__'
        exclude = [ 'host', 'participants' ]