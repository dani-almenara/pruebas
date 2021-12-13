from django import forms
from django.forms.widgets import HiddenInput

class SearchForm(forms.Form):
  ciudad = forms.CharField(label='city', max_length=100, widget=forms.TextInput(
    attrs={'id': 'CitySearch', 'name': 'CitySearch'}))
  # Campos ocultos
  # Google place_id
  place_id = forms.CharField(label='place_id',
    widget=forms.HiddenInput(attrs={'id': 'place_id', 'name': 'place_id'}), required=False)
  # Pais
  country = forms.CharField(label='country',
    widget=forms.HiddenInput(attrs={'id': 'country', 'name': 'country'}), required=False)
  # Comunidad
  administrative_area_level_1 = forms.CharField(label='administrative_area_level_1',
    widget=forms.HiddenInput(attrs={'id': 'administrative_area_level_1', 'name': 'administrative_area_level_1'}), required=False)
  # Provincia
  administrative_area_level_2 = forms.CharField(label='administrative_area_level_2',
    widget=forms.HiddenInput(attrs={'id': 'administrative_area_level_2', 'name': 'administrative_area_level_2'}), required=False)
  # Ciudad
  locality = forms.CharField(label='locality',
    widget=forms.HiddenInput(attrs={'id': 'locality', 'name': 'locality'}), required=False)