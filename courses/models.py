from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=50, verbose_name="Course name")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Course created at"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Course updated at"
    )
    owner_id = models.IntegerField(null=True, verbose_name="Course creator id")
    owner_name = models.CharField(
        max_length=50, null=True, verbose_name="Course creator name"
    )
    thumb_url = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Course thumb cover url",
    )
    cover_url = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Course cover url"
    )
    description = models.CharField(
        max_length=255, verbose_name="Course description"
    )
    last_activity = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        verbose_name="Last author’s activity",
    )
    total_score = models.IntegerField(
        verbose_name="Max score listener can get"
    )
    total_tasks = models.IntegerField(verbose_name="Number of tasks in course")
    unchangeable = models.BooleanField(verbose_name="Course changeable?")
    include_weekly_report = models.BooleanField(
        verbose_name="Course statistics will be included in the weekly report"
    )
    content_type = models.IntegerField(verbose_name="Course content type")

    def __str__(self):
        return str(self.name)
