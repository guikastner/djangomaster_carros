from django import forms
from cars.models import Brand, Car


    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        #fields = ['model', 'brand', 'factory_year', 'model_year', 'value', 'plate', 'photo']

    def clean_value(self): #serl é a instancia do form que está sendo validado
        value = self.cleaned_data['value']
        if value < 2000:
            self.add_error('value', 'Valor deve ser maior que R$ 2000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data['factory_year']
        year = 1975
        if factory_year < year:
            self.add_error('factory_year', f'Ano de fabricação inválido - deve ser maior que ${year}')
        return factory_year
    
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if not photo:
            raise forms.ValidationError("O campo 'photo' é obrigatório.")
        return photo
