from django import forms
from seatalloc.models import Candidate, Preference

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        exclude=()

    roll= forms.CharField(max_length=9 , help_text = "please enter your roll no")
    CHOICES=[(0,"GE"),(1,"OBC"),(2,"SC"),(3,"ST"),(4,"Foreign National")]
    BoolChoices=[(True,"Yes"),(False,"No")]
    cat=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    pd = forms.ChoiceField(choices=BoolChoices, widget=forms.RadioSelect())
    ds = forms.ChoiceField(choices=BoolChoices, widget=forms.RadioSelect())
    
class PreferenceForm(forms.ModelForm):
    #candidate = forms.CharField(max_length)
    INSTITUTES=[('B',"IIT-BOMBAY"),('A','bbbb')]
    institute = forms.ChoiceField(choices=INSTITUTES)
    program = forms.ChoiceField(choices=INSTITUTES)
    class Meta:
        model = Preference
        exclude=('candidate',)
       
