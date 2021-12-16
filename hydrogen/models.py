from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class GroupMixin(models.Model):
    GROUP_TYPE_CITY = 'C'
    GROUP_TYPE_COMPANY = 'Q'
    GROUP_TYPE_INSTITUTION = 'I'
    GROUP_TYPE_RESEARCH = 'U'  # U because it was previously University and renamed to Research
    GROUP_TYPE_PROJECT = 'P'
    GROUP_TYPE_EVENT = 'E'

    GROUP_TYPES = (
        (GROUP_TYPE_CITY, 'City'),
        (GROUP_TYPE_COMPANY, 'Company'),
        (GROUP_TYPE_INSTITUTION, 'Institution'),
        (GROUP_TYPE_RESEARCH, 'Research'),
        (GROUP_TYPE_PROJECT, 'Project'),
        (GROUP_TYPE_EVENT, 'Event'),
    )
    group_type = models.CharField(blank=False, null=False, choices=GROUP_TYPES, max_length=1)
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
    departments = models.TextField(_('departments'), max_length=settings.GROUP_DEPARTMENT_MAX_LENGTH,
                                   blank=True, null=True)
    closed = models.BooleanField(_('closed group'),
                                 help_text=_('only administrators can publish on closed groups'),
                                 default=False)
    # Project fields
    project_partners = models.TextField(_('project partners'), blank=True, null=True)
    project_duration = models.CharField(_('project duration'), max_length=settings.GROUP_PROJECT_DURATION,
                                        blank=True, null=True)
    lessons_learned = models.TextField(_('lessons learned'), blank=True, null=True)

    class Meta:
        abstract = True
