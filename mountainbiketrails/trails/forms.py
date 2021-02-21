from django.forms import ModelForm, TextInput, SelectDateWidget
from django.core.exceptions import ValidationError
from .models import Trail


class TrailForm(ModelForm):
    class Meta:
        model = Trail
        fields = '__all__'
        widgets = {
            'visited_on': SelectDateWidget,
            'difficulty_level': TextInput(attrs={"type": "number", "min":"0", "max": "10"}),
            'my_rating': TextInput(attrs={"type": "number", "min": "0", "max": "5"})
        }

    def clean_length(self):
        l = self.cleaned_data.get("length")

        if l < 0:
            raise ValidationError("Trail cannot be a negative length.")

        return l

    def clean(self):
        visited = self.cleaned_data.get('visited')
        fields = ['visited_on', 'my_rating', 'top_ten']

        if visited:
            self.fields_required(fields)

        return self.cleaned_data

    def fields_required(self, fields):
        for field in fields:
            if not self.cleaned_data.get(field, ''):
                msg = ValidationError("This field is required.")
                self.add_error(field, msg)