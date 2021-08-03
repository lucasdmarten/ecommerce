from django import forms

from store.models import *


class UserInformation(forms.ModelForm):

    address = forms.CharField(label='address',max_length=100)
    zipcode = forms.CharField(label='zipcode',max_length=100)                 
    city = forms.CharField(label='city',max_length=100)                 
    state = forms.CharField(label='state',max_length=100)                 


    class Meta:
        model = ShippingAddress
        fields = ('address','zipcode','city','state',)

    def __init__(self, *args, **kwargs):
        super(UserInformation, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['address'].widget.attrs['style'] = 'width: 99% !important; resize: vertical !important;'
        self.fields['zipcode'].widget.attrs['style'] = 'width: 99% !important; resize: vertical !important;'
        self.fields['city'].widget.attrs['style'] = 'width: 99% !important; resize: vertical !important;'
        self.fields['state'].widget.attrs['style'] = 'width: 99% !important; resize: vertical !important;'

    def save(self, customer, order):
        data = dict(
            address=self.cleaned_data['address'],
            zipcode=self.cleaned_data['zipcode'],
            city=self.cleaned_data['city'],
            state=self.cleaned_data['state']
            )
        shipping, created = ShippingAddress.objects.get_or_create(
            customer=customer, order=order,
            address=data['address'], zipcode=data['zipcode'],
            city=data['city'], state=data['state']
            )        
        return data