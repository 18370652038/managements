# -*- coding: utf-8 -*-
from django import forms


# class editForm(forms.Form): #已作废
#     number = forms.CharField(label='流水号', max_length=30 , required=True,widget=forms.TextInput(attrs={'class':'guo-deit-input'}),error_messages={'required': "此项为必填项"})
#     name = forms.CharField(label='用户昵称',max_length=120, required=True,widget=forms.TextInput(attrs={'class':'guo-deit-input'}),error_messages={'required': "此项为必填项"})
#     Devicename = forms.CharField(label='设备名称',max_length=30, required=True,widget=forms.TextInput(attrs={'class':'guo-deit-input'}),error_messages={'required': "此项为必填项"})
#     Areaname = forms.CharField(label='区域名称',max_length=120, required=True,widget=forms.TextInput(attrs={'class':'guo-deit-input'}),error_messages={'required': "此项为必填项"})
#     Devicenumber = forms.IntegerField(label='设备号',max_value=100000000000, required=True,widget=forms.TextInput(attrs={'class':'guo-deit-input'}),error_messages={'required': "此项为必填项"})
#     State = forms.ChoiceField(label='状态',choices=(('to poy','to poy'),('To be paid','To be paid'),('Refund','Refund')), widget=forms.Select())
#     Type = forms.ChoiceField(label='交易类型',widget=forms.Select(),choices=(('BANK','bank'),('Alipay','alipay'),('WeChat','wechat')))
#     Money = forms.DecimalField(label='交易金额',decimal_places=2,max_digits=8,widget=forms.TextInput(attrs={'class':'guo-deit-input'}),required=True,error_messages={'required': "此项为必填项"})
#     Duration = forms.IntegerField(label='交易时长',max_value=1000000000,widget=forms.TextInput(attrs={'class':'guo-deit-input'}),required=True,error_messages={'required': "此项为必填项"})
#     paymenttime = forms.DateTimeField(label='支付时间')
#     endtime = forms.DateTimeField(label='交易完成时间')
#     POnumber = forms.IntegerField(label='支付订单号:',max_value=10000000000,required=True,error_messages={'required': "此项为必填项"})
#     Remarks = forms.CharField(label='帮助',max_length=300,widget=forms.Textarea(),required=False,error_messages={'required': "此项为必填项"})