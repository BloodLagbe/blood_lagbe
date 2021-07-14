from django import forms
from address.models import (
    Division, District, Upazila
)
from accounts.models import Profile
from core.models import Blood



class SearchDoner(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super(SearchDoner, self).__int__(*args, **kwargs)
        division_choices = [(0, 'Select Event')]
        district_choices = [(0, 'Select Event')]
        upazila_choices = [(0, 'Select Event')]
        blood_choices = [(0, 'Select Event')]

        division_choices_model = [
            (ev.pk, ev.div_name) for ev in Division.objects.all()
        ]
        district_choices_model = [
            (ev.pk, ev.dist_name) for ev in District.objects.all()
        ]
        upazila_choices_model = [
            (ev.pk, ev.upazila_name) for ev in Upazila.objects.all()
        ]
        blood_choices_model = [
            (ev.pk, ev.name) for ev in Blood.objects.all()
        ]

        division_choices.extend(division_choices_model)
        district_choices.extend(district_choices_model)
        upazila_choices.extend(upazila_choices_model)
        blood_choices.extend(blood_choices_model)

        self.fields['division'].choices = division_choices
        self.fields['district'].choices = district_choices
        self.fields['upazila'].choices = upazila_choices
        self.fields['blood'].choices = blood_choices

    class Meta:
        model = Profile
        fields = [
            'division',
            'district',
            'upazila',
            'blood',
        ]
        widgets = {

            'division': forms.Select(attrs={
                'id': 'division'
            }),
            'district': forms.Select(attrs={
                'id': 'district'
            }),
            'upazila': forms.Select(attrs={
                'id': 'upazila'
            }),
            'blood': forms.Select(attrs={
                'id': 'blood',
            }),

        }





