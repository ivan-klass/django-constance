from constance import settings

if settings.BACKEND == 'constance.backends.DatabaseBackend':

    from django.db import models
    from django.core.exceptions import ImproperlyConfigured

    from django.utils.translation import ugettext_lazy as _

    try:
        from picklefield import PickledObjectField
    except ImportError:
        raise ImproperlyConfigured("Couldn't find the the 3rd party app "
                                   "django-picklefield which is required for "
                                   "the constance database backend.")

    class Constance(models.Model):
        key = models.TextField()
        value = PickledObjectField()

        class Meta:
            verbose_name = _('constance')
            verbose_name_plural = _('constances')
            db_table = 'constance_config'

