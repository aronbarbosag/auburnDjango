from django import forms
from .models import Marca, Car


class CarroForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_preco(self):
        valor = self.cleaned_data['preco']
        if valor < 5000:
            self.add_error(
                'preco', 'Valor mínimo do carro deve ser de R$5000,00'
            )
        return valor
