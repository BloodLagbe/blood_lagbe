from django import forms
from address.models import (
    Division, District, Upazila
)


class SearchDoner(forms.Form):
    division_choices = [(0, 'Select Event')]
    district_choices = [(0, 'Select Event')]
    upazila_choices = [(0, 'Select Event')]
    division_choices_model = [
        (ev.id, ev.div_name) for ev in Division.objects.all()
    ]
    district_choices_model = [
        (ev.id, ev.dist_name) for ev in District.objects.all()
    ]
    upazila_choices_model = [
        (ev.id, ev.upazila_name) for ev in Upazila.objects.all(

        )]
    division_choices.extend(division_choices_model)
    district_choices.extend(district_choices_model)
    upazila_choices.extend(upazila_choices_model)

    division = forms.ChoiceField(
        choices=division_choices
    )



