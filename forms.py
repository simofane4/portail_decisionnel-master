from django import forms

FAILURES = (
    ('', 'Select...'),
    ('1', '1 ans'),
    ('2', '2 ans'),
    ('3', '3 ans'),
    ('4', 'Jamais')
)


SEX = (
    ('', 'Select...'),
    ('0', 'Homme'),
    ('1', 'Femme')
)

NIVEAU = (
    ('', 'Select...'),
    ('1', 'illettré'),
    ('2', 'primaire'),
    ('3', 'Collège'),
    ('4', 'lycée'),
    ('5', 'Etude supérieur')
)

FAMILLE = (
    ('', 'Select...'),
    ('1', 'Très mauvaise'),
    ('2', 'Mauvaise'),
    ('3', 'Moyenne'),
    ('4', 'Bonne'),
    ('5', 'Excellente')
)
ABSENCE = (
    ('', 'Select...'),
    ('1', 'Inférieur à 5'),
    ('2', 'entre 6 et 10'),
    ('3', 'entre 11 et 15'),
    ('4', 'Supérieur à 16')
)

Age = (
    ('', 'Select...'),
    ('1', 'Inférieur à 15'),
    ('2', 'entre 15 et 16'),
    ('3', 'entre 16 et 17'),
    ('4', 'entre 17 et 18'),
    ('5', 'Supérieur à 18')
)

TRAVAIL = (
    ('', 'Select...'),
    ('1', 'Professeur'),
    ('2', 'Santé'),
    ('3', 'Services publiques'),
    ('4', 'à la maison'),
    ('5', 'Autres')
)

GOOUT = (
    ('', 'Select...'),
    ('1', 'Jamais'),
    ('2', 'peu'),
    ('3', 'Moyenne'),
    ('4', 'Beaucoup'),
    ('5', 'Enorme')
)
HEURES = (
    ('', 'Select...'),
    ('0', 'Non'),
    ('1', 'Oui'))
CHOIX = (
    ('', 'Select...'),
    ('1', 'Proche de la maison'),
    ('2', 'Réputation'),
    ('3', 'Qualité de cours'),
    ('4', 'Autres'))

SCHOOLSUP = (
    ('', 'Select...'),
    ('0', 'Oui'),
    ('1', 'Non'))

class myForm(forms.Form):
    name = forms.CharField(max_length=100)
    sex = forms.ChoiceField(choices=SEX)
    failure = forms.ChoiceField(choices=FAILURES)
    fedu = forms.ChoiceField(choices=NIVEAU)
    schoolsup = forms.ChoiceField(choices=SCHOOLSUP)
    medu = forms.ChoiceField(choices=NIVEAU)
    goout = forms.ChoiceField(choices=GOOUT)
    freetime = forms.ChoiceField(choices=GOOUT)
    mjob = forms.ChoiceField(choices=TRAVAIL)
    fjob = forms.ChoiceField(choices=TRAVAIL)
    raison = forms.ChoiceField(choices=CHOIX)
    relation_familiale = forms.ChoiceField(choices=FAMILLE)
    absences = forms.ChoiceField(choices=ABSENCE)
    age = forms.ChoiceField(choices=Age)
    consomation_alcool = forms.ChoiceField(choices=GOOUT)
    sante = forms.ChoiceField(choices=FAMILLE)
"""   new_row = {'Medu': [Medu], 'Fedu': [Fedu], 'famrel': [famrel], 'freetime': [freetime], 'goout': [goout],'Walc': [Walc],
               'health': [health], 'Age': [Age],'Absences': [Absences],'Mjob': [Mjob],'Fjob': [Fjob],'reason': [reason]}"""