from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.


#客户信息
class Organization(models.Model):
    cname = models.CharField(verbose_name=_("name"),null=True,max_length=50)
    ename = models.CharField(verbose_name=_("English Name"),null=True,max_length=50)
    country = models.CharField(verbose_name=_("Country"),null=True,max_length=20)
    province = models.CharField(verbose_name=_("Province"),null=True,max_length=20)
    city = models.CharField(verbose_name=_("city"),null=True,max_length=50)
    district = models.CharField(verbose_name=_("district"),null=True,max_length=50)
    address = models.CharField(verbose_name=_("address"),null=True,max_length=50)
    website = models.URLField(verbose_name=_("website"),max_length=200,null=True)
    telphone = models.CharField(verbose_name=_("telphone"),max_length=30,null=True)
    room = models.IntegerField(verbose_name=_("room"),null=True)
    device = models.IntegerField(verbose_name=_('device'),null=True)

    class Meta:
        verbose_name = _('organization')
        verbose_name_plural = _('organization')

    def __str__(self):
        return '客户信息'

#用户信息
class NormalUser(AbstractUser):
    mob = models.CharField(verbose_name=_('mob'),max_length=30,null=True)
    QQ = models.CharField(verbose_name=_('QQ'),max_length=20,null=True)
    Weixin = models.CharField(verbose_name=_('Weixin'),max_length=20,null=True)
    email = models.EmailField(verbose_name=_("email"),max_length=50,null=True)
    AlarmMOB = models.IntegerField(verbose_name=_("AlarmMOB"),null=True)
    AlarmMail = models.EmailField(verbose_name=_("AlarmMail"),max_length=50,null=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'USERS'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "NormalUser"


#设备信息
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
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('deviceInfo')
        verbose_name_plural = _('deviceInfo')

    def __str__(self):
        return '设备信息'

#交易记录
class subclass_details(models.Model):
    STATE_CHOICES = (
        ('to poy','to poy '),
        ('To be paid','To be paid'),
        ('Refund','Refund'))
    TYPE_CHOICES = (('BANK','bank'),('Alipay','alipay'),('WeChat','wechat'))

    number = models.CharField(verbose_name=('Serial number'),max_length=30,unique=True)
    name = models.CharField(verbose_name=_('name'),max_length=120)
    State = models.CharField(verbose_name=_('State'),max_length=10,default='To be paid',choices=STATE_CHOICES)
    Type = models.CharField(verbose_name=_('Transaction type'),max_length=10,default='BANK',choices=TYPE_CHOICES)
    Money = models.DecimalField(verbose_name=_('Amount of money'),decimal_places=2,max_digits=8)
    Duration = models.IntegerField(verbose_name=_('Transaction duration'))
    paymenttime = models.DateTimeField(verbose_name=_("Payment time"),auto_now_add=True)
    endtime = models.DateTimeField(verbose_name=_("Payment time"),auto_now=True)
    POnumber = models.IntegerField(verbose_name=_("Payment order number"))
    deviceInfo = models.ForeignKey(DeviceInfo,on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    normalUser = models.ForeignKey(NormalUser,on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('subclass details')
        verbose_name_plural = _("subclass details")

    def __str__(self):
        return '交易记录'

class Price(models.Model):
    price = models.DecimalField(verbose_name=_("price"),decimal_places=2,max_digits=8)
    starttime = models.CharField(verbose_name=_("start time"),max_length=20)
    endtime = models.CharField(verbose_name=_("endtime"),max_length=20,null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('price')
        verbose_name_plural = _("price")
        ordering = ['starttime']

    def __str__(self):
        return 'price'




