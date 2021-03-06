from django.db import models
from django_enumfield import enum


class SocialMedia(models.Model):
    """
    Social media model
    """

    # Class to define social media type
    class SocialMediaType(enum.Enum):
        FACEBOOK = 0
        TWITTER = 1
        LINKEDIN = 2
        INSTAGRAM = 3

        __labels__ = {
            FACEBOOK: "Facebook",
            TWITTER: "Twitter",
            LINKEDIN: "Linkedin",
            INSTAGRAM: "Instagram",
        }

    # class for related type
    class RelatedType(enum.Enum):
        PEOPLE = 0
        CONTACT = 1

        __labels__ = {
            PEOPLE: "People",
            CONTACT: "Contact"
        }

    url = models.CharField(max_length=255)

    # Social media type
    social_media_type = enum.EnumField(
        SocialMediaType,
        verbose_name="Select social media",
        null=True,
        blank=True
    )
    related_type = enum.EnumField(
        RelatedType,
        verbose_name="Select the related type",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Social media"
        verbose_name_plural = "A - Social medias"

    def __str__(self):
        return self.url


class People(models.Model):
    """
    People model
    """

    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    description = models.TextField()
    profile_image = models.ImageField(
        upload_to="people",
        max_length=255,
        null=True,
        blank=True
    )
    social_medias = models.ManyToManyField(
        SocialMedia,
        blank=True
    )

    class Meta:
        verbose_name = "People"
        verbose_name_plural = "B - People"

    def __str__(self):
        return self.name
