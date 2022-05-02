from dataclasses import field
from django import forms

from common.models import Customer, Seller


class CustomerRegForm(forms.ModelForm):
    # gender=(('m','male'),('f','female'),)


    cust_name = forms.CharField(label='name',widget=forms.TextInput(attrs={'class':'form-control'}))
    email_id = forms.CharField(label='email',widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_no = forms.CharField(label='phone no',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    
    class Meta:
        
        model= Customer
        fields=('cust_name','email_id','phone_no','password')    # select required field
        # field='_all_'  # select all field
        # exclude=('cust_id',) #select all field excluding cust_id

    def clean_password(self):
        psw = self.cleaned_data['password']

        if len(psw)<8:
            raise forms.ValidationError('password should be minimum 8 characters')
        return psw

class SellerRegForm(forms.ModelForm):
    # gender=(('m','male'),('f','female'),)


    seller_name = forms.CharField(label='name',widget=forms.TextInput(attrs={'class':'form-control'}))
    email_id = forms.CharField(label='email',widget=forms.TextInput(attrs={'class':'form-control'}))
    acc_holedr = forms.CharField(label='accholder',widget=forms.TextInput(attrs={'class':'form-control'}))
    acc_no = forms.CharField(label='accno',widget=forms.TextInput(attrs={'class':'form-control'}))
    ifsc = forms.CharField(label='ifsc',widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_no = forms.CharField(label='phone',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        
        model= Seller
        fields=('seller_name','email_id','acc_holedr','acc_no','ifsc','phone_no','password')    # select required field
        # field='_all_'  # select all field
        # exclude=('cust_id',) #select all field excluding cust_id

    def clean_password(self):
        psw = self.cleaned_data['password']

        if len(psw)<8:
            raise forms.ValidationError('password should be minimum 8 characters')
        return psw