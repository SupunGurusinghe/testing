from django.db import models


# create supplier table to store suppliers details
class Suppliers(models.Model):
    # data columns with its constraints
    supplier_id = models.CharField(max_length=10, primary_key=True)
    supplier_name = models.CharField(max_length=255)
    license_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15)
    organization_type = models.CharField(max_length=255)
    bank = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    account_no = models.IntegerField


# create requisitions table to store order requisitions details
class OrderRequisitions(models.Model):
    list_id = models.CharField(max_length=20, primary_key=True)
    month_required = models.IntegerField
    supplier_name = models.CharField(max_length=255)
    date = models.DateTimeField
    created_employee = models.CharField(max_length=20)


# create items table to store item details which required for requisitions and orders
class Items(models.Model):
    REQUISITION = 'requisitions'
    DEFICIENCY_LIST = 'deficiencyLists'

    # List for select the list type
    LIST_TYPE_CHOICES = [
        (REQUISITION, 'requisition'),
        (DEFICIENCY_LIST, 'deficiency list'),
    ]

    row_id = models.IntegerField(primary_key=True)
    # create foreign key constraints
    list_id = models.ForeignKey(OrderRequisitions, on_delete=models.PROTECT)
    list_type = models.CharField(max_length=255, choices=LIST_TYPE_CHOICES, default=REQUISITION)
    item_id = models.CharField(max_length=20)
    item_description = models.CharField(max_length=150)
    quantity = models.IntegerField
    unit_price = models.DecimalField(null=True, max_digits=13, decimal_places=2)
    amount = models.DecimalField(null=True, max_digits=13, decimal_places=2)


# create purchase orders table to store order details
class PurchaseOrders(models.Model):
    order_id = models.CharField(max_length=20, primary_key=True)
    supplier_name = models.CharField(max_length=255)
    required_date = models.DateTimeField
    shipping_method = models.CharField(max_length=200)
    grand_total = models.DecimalField(null=False, max_digits=13, decimal_places=2)


# create invoices table to store invoices details which are sent by suppliers
class Invoices(models.Model):
    invoice_id = models.CharField(max_length=20, primary_key=True)
    order_id = models.ForeignKey(PurchaseOrders, on_delete=models.PROTECT)
    # create foreign key constraints
    supplier_id = models.ForeignKey(Suppliers, on_delete=models.PROTECT)
    sub_total = models.DecimalField(null=False, max_digits=9, decimal_places=2)
    tax = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    discount = models.CharField(max_length=10)
    grand_total = models.DecimalField(null=False, max_digits=13, decimal_places=2)
    payment_term= models.CharField(max_length=200)
    payment_method = models.CharField(max_length=200)


# create OrdersRequisitionInvoice table to store orders,requisitions and invoices details
class OrderRequisitionInvoice(models.Model):
    # create foreign key constraints
    list_id = models.ForeignKey(OrderRequisitions, on_delete=models.PROTECT)
    invoice_id = models.ForeignKey(Invoices, on_delete=models.PROTECT)
    order_id = models.ForeignKey(PurchaseOrders, on_delete=models.PROTECT)

# create composite key
    class Meta:
        unique_together = (('list_id', 'invoice_id', 'order_id'),)