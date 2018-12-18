from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class DeviceInfo(models.Model):
    DeviceID = models.CharField(verbose_name=_("DeviceID"), max_length=20, unique=True)
    Eey = models.CharField(verbose_name=_("Eey"), max_length=30)
    eKey = models.CharField(verbose_name=_('eKey'), max_length=30)
    ADDR = models.CharField(verbose_name=_("ADDR"), max_length=30)
    MACaddress = models.CharField(verbose_name=_("MACaddress"), max_length=30, null=True)
    CCID = models.CharField(verbose_name=_("CCID"), max_length=30, null=True)
    RegTimes = models.DateTimeField(verbose_name=_("RegTimes"), auto_now_add=True)
    RecTimes = models.DateTimeField(verbose_name=_("RecTimes"), auto_now=True)
    BeatTimes = models.DateTimeField(verbose_name=_("BeatTimes"), auto_now=True)
    class Meta:
        verbose_name = _('DeviceInfo')
        verbose_name_plural = _('DeviceInfo')

    def __str__(self):
        return '设备信息'

class Organization(models.Model):
    cname = models.CharField(verbose_name=_("中文名"),null=True,max_length=50)
    ename = models.CharField(verbose_name=_("English Name"),null=True,max_length=50)
    country = models.CharField(verbose_name=_("Country"),null=True,max_length=20)
    province = models.CharField(verbose_name=_("Province"),null=True,max_length=20)
    city = models.CharField(verbose_name=_("city"),null=True,max_length=50)
    district = models.CharField(verbose_name=_("district"),null=True,max_length=50)
    address = models.CharField(verbose_name=_("address"),null=True,max_length=50)
    website = models.URLField(validators=_("website"))

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
    deviceInfo = models.ForeignKey(DeviceInfo,on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('subclass details')
        verbose_name_plural = _("subclass details")

    def __str__(self):
        return '交易记录'


