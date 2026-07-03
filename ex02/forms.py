from django import forms


class InputForm(forms.Form):
    text = forms.CharField(label='Text', max_length=255,
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Type something...'}))
