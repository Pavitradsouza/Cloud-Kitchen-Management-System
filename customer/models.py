from django.db import models
class userregistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    role = models.CharField(max_length=20)  # customer / kitchen_owner / delivery / admin

# 1. User Login
class userlogin(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=20)

# 2. Kitchen
class kitchen(models.Model):
    owner = models.CharField(max_length=100)
    kitchen_name = models.CharField(max_length=100)
    cuisine_type = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    license_number = models.CharField(max_length=50)
    rating = models.CharField(max_length=5)
    status = models.CharField(max_length=20)  # active / inactive / suspended
    logo = models.FileField(upload_to='documents/', null=True, blank=True)

# 3. Menu Category
class menucategory(models.Model):
    kitchen= models.CharField(max_length=100)
    category_name = models.CharField(max_length=50)  # starters / main_course / desserts / beverages
    description = models.CharField(max_length=200)
    display_order = models.CharField(max_length=5)
    status = models.CharField(max_length=20)

# 4. Menu Item
class menuitem(models.Model):
    menuitem = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=20)
    discount_price = models.CharField(max_length=20)
    preparation_time = models.CharField(max_length=20)
    veg_non_veg = models.CharField(max_length=10)
    spice_level = models.CharField(max_length=10)
    photo = models.FileField(upload_to='documents/', null=True, blank=True)
    availability = models.CharField(max_length=20)

# 5. Order
class order(models.Model):
    customer = models.CharField(max_length=100)
    kitchen = models.CharField(max_length=100)
    order_date = models.CharField(max_length=25)
    delivery_address = models.CharField(max_length=200)
    total_amount = models.CharField(max_length=20)
    discount_applied = models.CharField(max_length=20)
    final_amount = models.CharField(max_length=20)
    order_type = models.CharField(max_length=20)  # delivery / pickup
    special_instructions = models.TextField()
    status = models.CharField(max_length=20)  # placed / preparing / ready / delivered / cancelled

# 6. Order Item
class orderitem(models.Model):
    order = models.CharField(max_length=100)
    menu_item = models.CharField(max_length=100)
    quantity = models.CharField(max_length=5)
    unit_price = models.CharField(max_length=20)
    total_price = models.CharField(max_length=20)
    customization = models.CharField(max_length=200)

# 7. Delivery
class delivery(models.Model):
    order = models.CharField(max_length=100)
    delivery_person= models.CharField(max_length=100)
    pickup_time = models.CharField(max_length=25)
    delivery_time = models.CharField(max_length=25)
    estimated_time = models.CharField(max_length=20)
    delivery_address = models.CharField(max_length=200)
    delivery_fee = models.CharField(max_length=20)
    status = models.CharField(max_length=20)  # assigned / picked_up / in_transit / delivered

# 8. Payment
class payment(models.Model):
    order = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)
    amount = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=30)  # UPI / card / cash / wallet
    transaction_id = models.CharField(max_length=100)
    payment_date = models.CharField(max_length=25)
    status = models.CharField(max_length=20)  # paid / pending / refunded / failed

# 9. Coupon / Offer
class coupon(models.Model):
    kitchen = models.CharField(max_length=100)
    coupon_code = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    discount_type = models.CharField(max_length=20)  # percentage / flat
    discount_value = models.CharField(max_length=10)
    min_order_amount = models.CharField(max_length=20)
    max_discount_amount = models.CharField(max_length=20)
    valid_from = models.CharField(max_length=25)
    valid_to = models.CharField(max_length=25)
    usage_limit = models.CharField(max_length=10)
    status = models.CharField(max_length=20)

# 10. Ingredient / Inventory
class ingredient(models.Model):
    kitchen = models.CharField(max_length=100)
    ingredient_name = models.CharField(max_length=100)
    quantity_available = models.CharField(max_length=20)
    unit = models.CharField(max_length=20)  # kg / litre / pieces
    reorder_level = models.CharField(max_length=20)
    supplier_name = models.CharField(max_length=100)
    last_restocked_date = models.CharField(max_length=25)
    cost_per_unit = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

# 11. Review
class review(models.Model):
    customer = models.CharField(max_length=100)
    kitchen = models.CharField(max_length=100)
    menu_item = models.CharField(max_length=100)
    order = models.CharField(max_length=100)
    rating = models.CharField(max_length=5)
    review_text = models.TextField()
    review_date = models.CharField(max_length=25)
    photo = models.FileField(upload_to='documents/', null=True, blank=True)

# 12. Notification
class notification(models.Model):
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    message = models.TextField()
    notification_date = models.CharField(max_length=25)
    read_status = models.CharField(max_length=10)
    notification_type = models.CharField(max_length=30)

