import os
import re

dir_path = r"c:\Users\sindhu\OneDrive\Documents\cloud kitchen\cloud kitchen\owner (1)\owner\customer\templates"

owner_menu = """
<nav class="sidebar-nav">
    <a href="{% url 'owner_home' %}"><span class="nav-icon">🏠</span><span>Home</span></a>
    <div class="sidebar-nav-label">Management</div>
    <a href="{% url 'insertkitchen' %}"><span class="nav-icon">🏪</span><span>Add Kitchen</span></a>
    <a href="{% url 'showkitchen' %}"><span class="nav-icon">📋</span><span>View Kitchens</span></a>
    <a href="{% url 'insertmenucategory' %}"><span class="nav-icon">📂</span><span>Add Category</span></a>
    <a href="{% url 'showmenucategory' %}"><span class="nav-icon">📋</span><span>View Categories</span></a>
    <a href="{% url 'insertmenuitem' %}"><span class="nav-icon">🍔</span><span>Add Menu Item</span></a>
    <a href="{% url 'showmenuitem' %}"><span class="nav-icon">📋</span><span>View Menu Items</span></a>
    <a href="{% url 'insertingredient' %}"><span class="nav-icon">🥬</span><span>Add Ingredient</span></a>
    <a href="{% url 'showingredient' %}"><span class="nav-icon">📋</span><span>View Ingredients</span></a>
    <a href="{% url 'insertcoupon' %}"><span class="nav-icon">🎟️</span><span>Add Coupon</span></a>
    <a href="{% url 'showcoupon' %}"><span class="nav-icon">📋</span><span>View Coupons</span></a>
    <div class="sidebar-nav-label">Operations</div>
    <a href="{% url 'showorder' %}"><span class="nav-icon">📦</span><span>Orders</span></a>
    <a href="{% url 'showpayment' %}"><span class="nav-icon">💳</span><span>Payments</span></a>
    <a href="{% url 'showreview' %}"><span class="nav-icon">⭐</span><span>Reviews</span></a>
    <a href="{% url 'showindex' %}"><span class="nav-icon">🚪</span><span>Logout</span></a>
</nav>
"""

customer_menu = """
<nav class="sidebar-nav">
    <a href="{% url 'customer_home' %}"><span class="nav-icon">🏠</span><span>Home</span></a>
    <div class="sidebar-nav-label">Browse</div>
    <a href="{% url 'showkitchen' %}"><span class="nav-icon">🏪</span><span>Kitchens</span></a>
    <a href="{% url 'showmenucategory' %}"><span class="nav-icon">📂</span><span>Categories</span></a>
    <a href="{% url 'showmenuitem' %}"><span class="nav-icon">🍔</span><span>Menu</span></a>
    <div class="sidebar-nav-label">My Activity</div>
    <a href="{% url 'insertorder' %}"><span class="nav-icon">🛒</span><span>Place Order</span></a>
    <a href="{% url 'showorder' %}"><span class="nav-icon">📦</span><span>My Orders</span></a>
    <a href="{% url 'insertpayment' %}"><span class="nav-icon">💳</span><span>Make Payment</span></a>
    <a href="{% url 'insertreview' %}"><span class="nav-icon">⭐</span><span>Add Review</span></a>
    <a href="{% url 'showcoupon' %}"><span class="nav-icon">🎟️</span><span>Coupons</span></a>
    <a href="{% url 'shownotification' %}"><span class="nav-icon">🔔</span><span>Notifications</span></a>
    <a href="{% url 'showindex' %}"><span class="nav-icon">🚪</span><span>Logout</span></a>
</nav>
"""

with open(os.path.join(dir_path, 'owner_menu.html'), 'w', encoding='utf-8') as f:
    f.write(owner_menu)

with open(os.path.join(dir_path, 'customer_menu.html'), 'w', encoding='utf-8') as f:
    f.write(customer_menu)

owner_files = ['kitchen.html', 'viewkitchen.html', 'menucategory.html', 'viewmenucategory.html', 
               'menuitem.html', 'viewmenuitem.html', 'ingredient.html', 'viewingredient.html', 
               'viewingreditent.html', 'coupon.html', 'viewcoupon.html', 'delivery.html', 
               'viewdelivery.html', 'userlogin.html', 'viewuserlogin.html', 
               'userregistration.html', 'viewuserregistration.html']

customer_files = ['order.html', 'vieworder.html', 'orderitem.html', 'vieworderitem.html', 
                  'payment.html', 'viewpayment.html', 'review.html', 'viewreview.html', 
                  'notification.html', 'viewnotification.html']

public_files = ['index.html', 'login.html', 'register.html', 'forget.html', 'change.html', 'owner_home.html', 'customer_home.html']

for filename in os.listdir(dir_path):
    if not filename.endswith('.html') or filename in public_files or filename in ['owner_menu.html', 'customer_menu.html']:
        continue
        
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if filename in owner_files:
        replacement = "{% include 'owner_menu.html' %}"
    else:
        replacement = "{% include 'customer_menu.html' %}"
        
    new_content = re.sub(r'<nav class="sidebar-nav">.*?</nav>', replacement, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

owner_home_html = """<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Owner Dashboard</title>
    <link rel="stylesheet" href="{% static 'style.css' %}">
</head>
<body>
    <header class="header">
        <nav class="navbar">
            <a href="{% url 'owner_home' %}" class="logo">
                <span class="logo-icon">🍽️</span>
                <span class="logo-text">CloudKitchen Owner</span>
            </a>
            <div class="nav-auth">
                <a href="{% url 'showindex' %}" class="btn btn-outline">Logout</a>
            </div>
        </nav>
    </header>
    <div class="dashboard-wrapper">
        <aside class="sidebar">
            <div class="sidebar-brand">
                <span class="logo-icon">👨‍🍳</span>
                <span class="logo-text">Owner Portal</span>
            </div>
            {% include 'owner_menu.html' %}
        </aside>
        <main class="dashboard-content">
            <div class="page-header">
                <h1>Welcome to <span>Owner Dashboard</span></h1>
                <p>Manage your kitchen, menu, orders, and ingredients efficiently.</p>
            </div>
        </main>
    </div>
</body>
</html>"""

customer_home_html = """<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Dashboard</title>
    <link rel="stylesheet" href="{% static 'style.css' %}">
</head>
<body>
    <header class="header">
        <nav class="navbar">
            <a href="{% url 'customer_home' %}" class="logo">
                <span class="logo-icon">🍽️</span>
                <span class="logo-text">CloudKitchen Customer</span>
            </a>
            <div class="nav-auth">
                <a href="{% url 'showindex' %}" class="btn btn-outline">Logout</a>
            </div>
        </nav>
    </header>
    <div class="dashboard-wrapper">
        <aside class="sidebar">
            <div class="sidebar-brand">
                <span class="logo-icon">👤</span>
                <span class="logo-text">Customer Portal</span>
            </div>
            {% include 'customer_menu.html' %}
        </aside>
        <main class="dashboard-content">
            <div class="page-header">
                <h1>Welcome to <span>Customer Dashboard</span></h1>
                <p>Order fresh, delicious meals delivered to your doorstep.</p>
            </div>
        </main>
    </div>
</body>
</html>"""

with open(os.path.join(dir_path, 'owner_home.html'), 'w', encoding='utf-8') as f:
    f.write(owner_home_html)

with open(os.path.join(dir_path, 'customer_home.html'), 'w', encoding='utf-8') as f:
    f.write(customer_home_html)

print('Done replacing.')
