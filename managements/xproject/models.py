from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class subclass_details(models.Model):
    STATE_CHOICES = (
        ('to poy','to poy '),
        ('To be paid','To be paid'),
        ('Refund','Refund'))
    TYPE_CHOICES = (('BANK','bank'),('Alipay','alipay'),('WeChat','wechat'))

    number = models.CharField(verbose_name=('Serial number'),max_length=30,unique=True)
    name = models.CharField(verbose_name=_('name'),max_length=120)
    Devicename = models.CharField(verbose_name=_('Device name'),max_length=30)
    Areaname = models.CharField(verbose_name=_('Area name'),max_length=120)
    Devicenumber = models.IntegerField(verbose_name=_('Device number'),max_length=10)
    State = models.CharField(verbose_name=_('State'),max_length=10,default='To be paid',choices=STATE_CHOICES)
    Type = models.CharField(verbose_name=_('Transaction type'),max_length=10,default='BANK',choices=TYPE_CHOICES)
    Money = models.DecimalField(verbose_name=_('Amount of money'),decimal_places=2,max_digits=8)
    Duration = models.IntegerField(verbose_name=_('Transaction duration'),max_length=10)
    paymenttime = models.DateTimeField(verbose_name=_("Payment time"),auto_now_add=True)
    endtime = models.DateTimeField(verbose_name=_("Payment time"),auto_now=True)
    POnumber = models.IntegerField(verbose_name=_("Payment order number"),max_length=20)
    Remarks = models.TextField(verbose_name=_('Remarks'),max_length=100,null=True,blank=True)
    # run = models.CharField(verbose_name=_('RUN'),max_length=10,)

    class Meta:
        verbose_name = _('subclass details')
        verbose_name_plural = _("subclass details")

    def __str__(self):
        return 'subclass details'

# class Organization(models.Model):
#     cname = models.CharField()



