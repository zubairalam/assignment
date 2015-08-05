from django import forms
from .models import Profile, State, City, Pincode


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'state', 'city', 'pincode']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs = {
            'required': 'true',
            'placeholder': 'First and Last name',
            'class': 'form-control'
        }
        self.fields['name'].error_messages = {'required': 'Name is required.'}
        
        data = kwargs.get('data')
        state = city = pincode = None
        if data:
            state = data.get('state', None)
            city = data.get('city', None)
            pincode = data.get('pincode', None)

        self.fields['state'] = forms.ModelChoiceField(queryset=State.objects.all(), empty_label='Select a state')
        
        if state and state.isdigit():
            self.fields['city'] = forms.ModelChoiceField(queryset=State.objects.get(id=int(state)).city.all(), empty_label='Select a city')
        else:
            self.fields['city'] = forms.ChoiceField(choices=[('', 'Select a city')])
        
        if city and city.isdigit():
            self.fields['pincode'] = forms.ModelChoiceField(queryset=City.objects.get(id=int(city)).pincode.all(), empty_label='Select a pincode')
        else:
            self.fields['pincode'] = forms.ChoiceField(choices=[('', 'Select a pincode')])
