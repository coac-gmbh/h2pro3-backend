from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class GroupMixin(models.Model):
    GROUP_TYPE_CITY = 'C'
    GROUP_TYPE_COMPANY = 'Q'
    GROUP_TYPE_INSTITUTION = 'I'
    GROUP_TYPE_UNIVERSITY = 'U'

    GROUP_TYPES = (
        (GROUP_TYPE_CITY, 'City'),
        (GROUP_TYPE_COMPANY, 'Company'),
        (GROUP_TYPE_INSTITUTION, 'Institution'),
        (GROUP_TYPE_UNIVERSITY, 'University'),
    )
    group_type = models.CharField(blank=True, null=True, choices=GROUP_TYPES, max_length=1)
    about_us = models.TextField(_('about us'), max_length=settings.GROUP_RULES_MAX_LENGTH,
                                blank=True, null=True)
    website = models.URLField(_('website'), max_length=settings.GROUP_WEBSITE_MAX_LENGTH,
                              blank=True, null=True)
    # City fields
    population = models.CharField(_('population'), max_length=settings.GROUP_POPULATION_MAX_LENGTH,
                                  blank=True, null=True)
    area = models.CharField(_('area'), max_length=settings.GROUP_AREA_MAX_LENGTH,
                            blank=True, null=True)
    energy_demand = models.CharField(_('energy demand'), max_length=settings.GROUP_ENERGY_DEMAND_MAX_LENGTH,
                                     blank=True, null=True)
    # Company fields
    industry = models.CharField(_('industry'), max_length=settings.GROUP_INDUSTRY_MAX_LENGTH,
                                blank=True, null=True)
    employee = models.CharField(_('employee'), max_length=settings.GROUP_EMPLOYEE_MAX_LENGTH,
                                blank=True, null=True)
    location = models.CharField(_('location'), max_length=settings.GROUP_LOCATION_MAX_LENGTH,
                                blank=True, null=True)
    # University fields
    institution = models.CharField(_('institution'), max_length=settings.GROUP_INSTITUTION_MAX_LENGTH,
                                   blank=True, null=True)
    department = models.CharField(_('department'), max_length=settings.GROUP_DEPARTMENT_MAX_LENGTH,
                                  blank=True, null=True)

    def set_categories_with_names(self):
        pass

    class Meta:
        abstract = True
