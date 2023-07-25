from django import forms
from .models import Comentarios

class ComentariosForm(forms.ModelForm):

    class Meta:
      model = Comentarios
      fields = ['texto']
