from django.db import models
from django.urls import reverse

from accounts.models import MyUser


class Customer(models.Model):

    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_at',)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):

    customer = models.ForeignKey(Customer,
                 on_delete=models.SET_NULL,
                 blank=True, null=True)
    
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,
                null=True, blank=False)
    transaction_id = models.CharField(max_length=200,
                    null=True)

    def __str__(self):
        return str(self.customer)

    # @property
    # def get_cart_items(self):
    #     orderitems = self.orderitem_set.all()
    #     return {
    #         'items':
    #         [orderitem.product.name for orderitem in orderitems],
    #         'quantity':
    #         sum([orderitem.quantity for orderitem in orderitems]),
    #         'total':
    #         sum([orderitem.product.price*orderitem.quantity for orderitem in orderitems]) 
    #     }

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        items = [orderitem.product for orderitem in orderitems]
        return items

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = [int(item.quantity)*item.product.price for item in orderitems]
        return sum(total)

    @property
    def get_cart_quantity(self):
        orderitems = self.orderitem_set.all()
        total = [int(item.quantity) for item in orderitems]
        return sum(total)


class OrderItem(models.Model):

    product = models.ForeignKey(Product,
                on_delete=models.SET_NULL,
                blank=True, null=True)
    order = models.ForeignKey(Order,
                on_delete=models.SET_NULL,
                blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    date_add = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,
                null=True, blank=False)
    transaction_id = models.CharField(max_length=200,
                    null=True)                   

    @property
    def get_total(self):
        return self.quantity * self.product.price

    def get_price(self):
        return self.product.price

    @property
    def add(self):
        self.quantity += 1

    @property
    def remove(self):
        self.quantity -= 1

    def __str__(self):
        return self.product.name


class ShippingAddress(models.Model):

    customer = models.ForeignKey(Customer, 
                on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order,
                on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_add = models.DateTimeField(auto_now_add=True)

    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.address

