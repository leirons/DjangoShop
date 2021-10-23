from django.db import models
from django.utils.translation import ugettext_lazy as _


class Tax(models.Model):
    """Represent a tax rate.

       **Attributes**:

       rate
           The tax rate in percent.

       description
           The description of the tax rate.
       """
    rate:models.FloatField = models.FloatField(_("Rate"),default=0)
    description:models.TextField = models.TextField(_("Description"))

    def __str__(self):
        return f"%self.rate"

