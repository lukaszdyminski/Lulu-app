import django_filters
from .models import *
from bootstrap_datepicker_plus import DatePickerInput
from django.db.models import Q
from functools import reduce
import operator


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

    def author_user_filter(self, queryset, name, value):
        lookups = ['author__icontains', 'user__username__icontains']
        or_queries = [Q(**{lookup: value}) for lookup in lookups]
        return PetPost.objects.filter(reduce(operator.or_, or_queries))


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

    def author_user_filter(self, queryset, name, value):
        lookups = ['author__icontains', 'user__username__icontains']
        or_queries = [Q(**{lookup: value}) for lookup in lookups]
        return LuluPost.objects.filter(reduce(operator.or_, or_queries))
