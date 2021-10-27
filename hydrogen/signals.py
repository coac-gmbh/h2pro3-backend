from django.db.models.signals import post_save
from django.dispatch import receiver
from hydrogen.models import GroupMixin
from openbook_common.utils.model_loaders import get_category_model
from openbook_communities.models import Community


# Required by Hydrogen to map group types to certain categories
CATEGORIES_MAPPING = {
    GroupMixin.GROUP_TYPE_CITY: "Städte und Kreise",
    GroupMixin.GROUP_TYPE_COMPANY: "Unternehmen",
    GroupMixin.GROUP_TYPE_RESEARCH: "Wissenschaft",
    GroupMixin.GROUP_TYPE_INSTITUTION: "Netzwerke"
}


# Pre save doesn't work because adding categories requires the group to have an ID
@receiver(post_save, sender=Community)
def sync_group_types_categories(sender, instance, **kwargs):
    Category = get_category_model()
    if instance.group_type and instance.group_type in CATEGORIES_MAPPING:
        mapped_group_name = CATEGORIES_MAPPING[instance.group_type]
        # Remove other groups that are mapped to different group types
        categories_names_to_remove = list(set(CATEGORIES_MAPPING.values()) - {mapped_group_name})
        categories_to_remove = Category.objects.filter(name__in=categories_names_to_remove).all()
        if len(categories_to_remove):
            instance.categories.remove(*categories_to_remove)
        # Add the required category by mapping
        valid_category = Category.objects.filter(name=mapped_group_name).first()
        if valid_category:
            instance.categories.add(valid_category)
    else:
        # The group type should not be inside any of the mapped categories because it's invalid
        all_mapped_categories = Category.objects.filter(name__in=list(CATEGORIES_MAPPING.values())).all()
        if len(all_mapped_categories):
            instance.categories.remove(*all_mapped_categories)
