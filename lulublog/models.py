from django.db import models
from django.core import validators
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class LuluPost(models.Model):
    author = models.CharField(max_length=40, verbose_name='Autor', null=True, blank=True)
    title = models.CharField(max_length=60, verbose_name='Tytuł')
    content = models.TextField(verbose_name='Twój Post')
    lulu_pic = models.ImageField(upload_to='lulu_images/', null=True, blank=True, verbose_name='Zdjęcie')
    pic_caption = models.CharField(max_length=35, null=True, blank=True, verbose_name='Podpis')
    publ_date = models.DateTimeField(auto_now_add=True, verbose_name='Data publikacji')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True,
                             related_name='lulu_post_user')

    def get_absolute_url(self):
        return reverse('lulu_single_post', kwargs={'pk': self.pk})

    def __str__(self):
        if self.user:
            return 'Lulu story #{} -- titled "{}" -- posted on {} -- by {}'.format(str(self.id), self.title,
                                                                               str(self.publ_date), self.user)
        else:
            return 'Lulu story #{} -- titled "{}" -- posted on {} -- by {}'.format(str(self.id), self.title,
                                                                               str(self.publ_date), self.author)


PET_SPECIES_CHOICES = (
    ("Pies", "Pies"),
    ("Kot", "Kot"),
    ("Chomik", "Chomik"),
    ("Królik", "Królik"),
    ("Żółw", "Żółw"),
    ("Papuga", "Papuga"),
    ("Świnka morska", "Świnka morska"),
    ("Rybki", "Rybki"),
    ("Mysz", "Mysz"),
    ("Szczur", "Szczur"),
    ("Jaszczurka", "Jaszczurka"),
    ("Inny gatunek", "Inny gatunek"),
)


class PetPost(models.Model):
    author = models.CharField(max_length=40, verbose_name='Autor', validators=[validators.MinLengthValidator(limit_value=2,
                                                                                 message='Wpisz przynajmniej 2 znaki'
                                                                                         ' w polu AUTOR.')],
                                                                                null=True,
                                                                                blank=True)
    pet_name = models.CharField(max_length=40, verbose_name='Imię zwierzaka')
    pet_species = models.CharField(max_length=20, choices=PET_SPECIES_CHOICES, default=None,
                                   verbose_name='Wybierz gatunek')
    pet_species_other = models.CharField(max_length=30, blank=True, verbose_name='Inny gatunek', null=True)
    title = models.CharField(max_length=60, verbose_name='Tytuł')
    content = models.TextField(verbose_name='Twój Post')
    lulu_pic = models.ImageField(upload_to='lulu_images/', null=True, blank=True, verbose_name='Zdjęcie')
    pic_caption = models.CharField(max_length=35, null=True, blank=True, verbose_name='Podpis')
    e_mail = models.EmailField(max_length=50, null=False, blank=False, verbose_name='Adres e-mail')
    publ_date = models.DateTimeField(auto_now_add=True, verbose_name='Data publikacji')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True,
                             related_name='pet_post_user')

    def get_absolute_url(self):
        return reverse('pet_single_post', kwargs={'pk': self.pk})

    def __str__(self):
        if self.user:
            if self.pet_species != 'Inny gatunek':
                return 'Pet story #{} -- titled "{}" -- about {} {} -- posted on {} -- by {}'.format(str(self.id),
                                                                                                         self.title,
                                                                                                         self.pet_name,
                                                                                                         self.pet_species,
                                                                                                         str(self.publ_date),
                                                                                                         self.user)
            else:
                return 'Pet story #{} -- titled "{}" -- about {} {} -- posted on {} -- by {}'.format(str(self.id),
                                                                                                         self.title,
                                                                                                         self.pet_name,
                                                                                                         self.pet_species_other,
                                                                                                         str(self.publ_date),
                                                                                                         self.user)
        else:
            if self.pet_species != 'Inny gatunek':
                return 'Pet story #{} -- titled "{}" -- about {} {} -- posted on {} -- by {}'.format(str(self.id),
                                                                                                         self.title,
                                                                                                         self.pet_name,
                                                                                                         self.pet_species,
                                                                                                         str(self.publ_date),
                                                                                                         self.author)
            else:
                return 'Pet story #{} -- titled "{}" -- about {} {} -- posted on {} -- by {}'.format(str(self.id),
                                                                                                         self.title,
                                                                                                         self.pet_name,
                                                                                                         self.pet_species_other,
                                                                                                         str(self.publ_date),
                                                                                                         self.author)


LULU_RATE_CHOICES = (
    ("1 * Lulu rozczarowana", " 1 * LULU ROZCZAROWANA"),
    ("2 ** Lulu marudna", " 2 ** LULU MARUDNA"),
    ("3 *** Lulu zainteresowana", " 3 *** LULU ZAINTERESOWANA"),
    ("4 **** Lulu pobudzona", " 4 **** POBUDZONA"),
    ("5 ***** Lulu podekscytowana", " 5 ***** LULU PODEKSCYTOWANA"),
)


class LuluPostComment(models.Model):
    post = models.ForeignKey(LuluPost, on_delete=models.CASCADE, verbose_name='Komentarz', related_name='comments',
                             null=True, blank=True)
    user = models.ForeignKey(User, editable=False, null=True, blank=True, verbose_name='Autor komentarza', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Treść komentarza', blank=True, null=True)
    publ_date = models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')
    rate = models.CharField(max_length=30, choices=LULU_RATE_CHOICES, default=None,
                            verbose_name='Ocena')

    class Meta:
        ordering = ('-publ_date', )

    def __str__(self):
        return 'Comment by {} on post "{}" date: {}'.format(self.user, self.post.title, self.publ_date)

    def get_absolute_url(self):
        return reverse('lulu_single_post', kwargs={'pk': self.post.pk})


PET_RATE_CHOICES = (
    ("1 * Lulu rozczarowana", " 1 * LULU ROZCZAROWANA"),
    ("2 ** Lulu marudna", " 2 ** LULU MARUDNA"),
    ("3 *** Lulu zainteresowana", " 3 *** LULU ZAINTERESOWANA"),
    ("4 **** Lulu pobudzona", " 4 **** LULU POBUDZONA"),
    ("5 ***** Lulu podekscytowana", " 5 ***** LULU PODEKSCYTOWANA"),
)


class PetPostComment(models.Model):
    post = models.ForeignKey(PetPost, on_delete=models.CASCADE, verbose_name='Komentarz', related_name='comments',
                             null=True, blank=True)
    user = models.ForeignKey(User, editable=False, null=True, blank=True, verbose_name='Autor komentarza', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Treść komentarza', blank=True, null=True)
    publ_date = models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')
    rate = models.CharField(max_length=30, choices=PET_RATE_CHOICES, default=None,
                            verbose_name='Ocena')

    class Meta:
        ordering = ('-publ_date', )

    def __str__(self):
        return 'Comment by {} on post "{}" date: {}'.format(self.user, self.post.title, self.publ_date)

    def get_absolute_url(self):
        return reverse('pet_single_post', kwargs={'pk': self.post.pk})

