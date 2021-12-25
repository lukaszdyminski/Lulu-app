from django import forms
from .models import *
from django.core import validators
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LuluForm(forms.Form):
    lulu_form_sender = forms.CharField(widget=forms.TextInput(attrs={'class': 'name-nick-title',
                                                                     'placeholder': 'Wpisz swoje imię / swój nick...',
                                                                     }),
                                       max_length=50,
                                       validators=[validators.MinLengthValidator(limit_value=2,
                                                                                 message='Wpisz przynajmniej 2 znaki'
                                                                                         ' w polu AUTOR.')])
    lulu_form_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'name-nick-title',
                                                                    'placeholder': 'Wpisz tytuł swojej story...'}),
                                      max_length=50, required=True)
    lulu_form_content = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea',
                                                                     'placeholder': 'Proszę, wpisz/wklej swoją story...',
                                                                     'rows': 15}), required=True)
    lulu_form_mail = forms.EmailField(widget=forms.TextInput(attrs={'class': 'name-nick-title',
                                                                    'placeholder': 'Wpisz swój adres e-mail...'}),
                                      required=True)


class PetForm(ModelForm):
    class Meta:
        model = PetPost
        fields = ('author', 'title', 'pet_name', 'pet_species', 'pet_species_other',
                  'content', 'lulu_pic', 'pic_caption', 'e_mail')
        widgets = {'author': forms.TextInput(attrs={'class': 'name-nick-title',
                                                    'placeholder': 'Wpisz swoje imię / swój nick...'}),
                   'title': forms.TextInput(attrs={'class': 'name-nick-title',
                                                   'placeholder': 'Wpisz tytuł swojej story...'}),
                   'pet_name': forms.TextInput(attrs={'class': 'name-nick-title',
                                                      'placeholder': 'Wpisz imię swojego zwierzaka...'}),
                   'pet_species': forms.RadioSelect(attrs={'id': 'pet-species'}),
                   'pet_species_other': forms.TextInput(attrs={'id': 'other-pet',
                                                               'placeholder': 'Wpisz gatunek, jeśli brak go powyżej...'}),
                   'content': forms.Textarea(attrs={'class': 'textarea',
                                                    'placeholder': 'Proszę, wpisz/wklej swoją story...',
                                                    'rows': 15}),
                   'lulu_pic': forms.FileInput(attrs={'id': 'pet-pic', 'required': False}),
                   'pic_caption': forms.TextInput(attrs={'class': 'name-nick-title',
                                                         'placeholder': 'Tu możesz podpisać zdjęcie...',
                                                         'required': False}),
                   'e_mail': forms.TextInput(attrs={'class': 'name-nick-title',
                                                    'placeholder': 'Wpisz swój adres e-mail...'}),
                   }


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {'username': "Użyj maksymalnie 150 znaków. "
                                  "Możesz wziąć pod uwagę: litery, cyfry oraz znaki: @ . + - _"}

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields[
            'password1'].help_text = "Użyj przynajmniej 8 znaków. Twoje hasło nie może składać się z samych cyfr."
        self.fields['email'].help_text = "Adres mailowy przyda się, by potwierdzić rejestrację Twojego profilu."


class LoggedLuluForm(ModelForm):

    class Meta:
        model = LuluPost
        fields = ('title', 'content')
        widgets = {'title': forms.TextInput(attrs={'class': 'name-nick-title',
                                                   'placeholder': 'Wpisz tytuł swojej story...'}),
                   'content': forms.Textarea(attrs={'class': 'textarea',
                                                    'placeholder': 'Proszę, wpisz/wklej swoją story...',
                                                    'rows': 15})}


class LoggedPetForm(ModelForm):

    class Meta:
        model = PetPost
        fields = ('title', 'pet_name', 'pet_species', 'pet_species_other',
                  'content', 'lulu_pic', 'pic_caption')
        widgets = {'title': forms.TextInput(attrs={'class': 'name-nick-title',
                                                   'placeholder': 'Wpisz tytuł swojej story...'}),
                   'pet_name': forms.TextInput(attrs={'class': 'name-nick-title',
                                                      'placeholder': 'Wpisz imię swojego zwierzaka...'}),
                   'pet_species': forms.RadioSelect(attrs={'class': 'pet-species'}),
                   'pet_species_other': forms.TextInput(attrs={'id': 'other-pet',
                                                               'placeholder': 'Wpisz gatunek, jeśli brak go powyżej...'}),
                   'content': forms.Textarea(attrs={'class': 'textarea',
                                                    'placeholder': 'Proszę, wpisz/wklej swoją story...',
                                                    'rows': 15}),
                   'lulu_pic': forms.FileInput(attrs={'id': 'pet-pic', 'required': False}),
                   'pic_caption': forms.TextInput(attrs={'class': 'name-nick-title',
                                                         'placeholder': 'Tu możesz podpisać zdjęcie...',
                                                         'required': False})}


class LuluPostCommentForm(forms.ModelForm):
    class Meta:
        model = LuluPostComment
        fields = ('content', 'rate')
        widgets = {'content': forms.Textarea(attrs={'class': 'textarea',
                                                    'placeholder': 'Proszę, wpisz/wklej swój komentarz...',
                                                    'rows': 10}),
                   'rate': forms.RadioSelect(attrs={'class': 'pet-species'})}


class PetPostCommentForm(forms.ModelForm):
    class Meta:
        model = PetPostComment
        fields = ('content', 'rate')
        widgets = {'content': forms.Textarea(attrs={'class': 'textarea',
                                                    'placeholder': 'Proszę, wpisz/wklej swój komentarz...',
                                                    'rows': 10}),
                   'rate': forms.RadioSelect(attrs={'class': 'pet-species'})}
