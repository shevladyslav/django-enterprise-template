from django.db import models


class TimeStampedModel(models.Model):
    """
    Abstract base model that provides self-updating
    `created_at` and `updated_at` fields.
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        help_text="Timestamp indicating when the record was created",
        db_comment="Record creation timestamp",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        help_text="Timestamp indicating when the record was last updated",
        db_comment="Record last update timestamp",
    )

    class Meta:
        abstract = True
