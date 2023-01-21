import django_filters
from .models import *
from bootstrap_datepicker_plus import DatePickerInput
from django.db.models import Q
from functools import reduce
import operator

'''the filters set displaying on the pet stories list page; showing the search results after entering phrases with 
a pet_name, an author or an user name and after choosing post entry dates from the date picker and pet_species 
from the list'''


class PetFilter(django_filters.FilterSet):
    pet_name = django_filters.CharFilter(field_name='pet_name', lookup_expr='icontains', label='Imię zwierzaka')
    start_date = django_filters.DateFilter(field_name='publ_date', lookup_expr='gte', label='Data publikacji od:',
                                           widget=DatePickerInput(format='%Y-%m-%d', options={'locale': 'pl-pl',
                                                                                              'showClose': False,
                                                                                              'showClear': False,
                                                                                              'showTodayButton': False
                                                                                              }))
    end_date = django_filters.DateFilter(field_name='publ_date', lookup_expr='lte', label='Data publikacji do:',
                                         widget=DatePickerInput(format='%Y-%m-%d', options={'locale': 'pl-pl',
                                                                                            'showClose': False,
                                                                                            'showClear': False,
                                                                                            'showTodayButton': False}))
    author_user = django_filters.CharFilter(label='Autor', method='author_user_filter')

    class Meta:
        model = PetPost
        fields = ['pet_species']

    # the function enabling the filtering of both non-logged-in author and logged-in user

    def author_user_filter(self, queryset, name, value):
        lookups = ['author__icontains', 'user__username__icontains']
        or_queries = [Q(**{lookup: value}) for lookup in lookups]
        return PetPost.objects.filter(reduce(operator.or_, or_queries))


'''the filters set displaying on the Lulu stories list page; showing the search results after entering phrases with 
an author or an user name and after choosing post entry dates from the date picker'''


class LuluFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='publ_date', lookup_expr='gte', label='Data publikacji od:',
                                           widget=DatePickerInput(format='%Y-%m-%d', options={'locale': 'pl-pl',
                                                                                              'showClose': False,
                                                                                              'showClear': False,
                                                                                              'showTodayButton': False
                                                                                              }))
    end_date = django_filters.DateFilter(field_name='publ_date', lookup_expr='lte', label='Data publikacji do:',
                                         widget=DatePickerInput(format='%Y-%m-%d', options={'locale': 'pl-pl',
                                                                                            'showClose': False,
                                                                                            'showClear': False,
                                                                                            'showTodayButton': False
                                                                                            }))
    author_user = django_filters.CharFilter(label='Autor', method='author_user_filter')

    # the function enabling the filtering of both non-logged-in author and logged-in user

    def author_user_filter(self, queryset, name, value):
        lookups = ['author__icontains', 'user__username__icontains']
        or_queries = [Q(**{lookup: value}) for lookup in lookups]
        return LuluPost.objects.filter(reduce(operator.or_, or_queries))
