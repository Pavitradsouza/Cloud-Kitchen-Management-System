from django.test import TestCase, Client
from django.urls import reverse
from customer.models import menucategory, menuitem, review, kitchen
from django.core.files.uploadedfile import SimpleUploadedFile

class MenuFlowTestCase(TestCase):
    def test_insert_menu_category_flow(self):
        c = Client()
        # 1. Post a new menu category
        response = c.post(reverse('insertmenucategory'), {
            't1': 'Kitchen A',
            't2': 'Beverages',
            't3': 'Cool drinks',
            't4': '1',
            't5': 'active'
        })
        # Check that it redirected to insertmenuitem
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.endswith(reverse('insertmenuitem')))
        
        # Check that 'catname' is stored in the session
        self.assertEqual(c.session.get('catname'), 'Beverages')
        
        # 2. Access the insertmenuitem page (GET) and check that 'catname' is prefilled in context
        response = c.get(reverse('insertmenuitem'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['catname'], 'Beverages')
        
        # 3. Post a new menu item with a photo upload
        dummy_photo = SimpleUploadedFile("test_photo.jpg", b"file_content", content_type="image/jpeg")
        response = c.post(reverse('insertmenuitem'), {
            't1': 'Kitchen A',
            't2': 'Beverages',
            't3': 'Iced Coffee',
            't4': 'Cold brewed coffee',
            't5': '5.00',
            't6': '4.50',
            't7': '5 mins',
            't8': 'veg',
            't9': 'mild',
            't10': dummy_photo,
            't11': 'yes'
        })
        
        # Check that menu item is created
        self.assertEqual(menuitem.objects.count(), 1)
        item = menuitem.objects.first()
        self.assertEqual(item.item_name, 'Iced Coffee')
        self.assertEqual(item.category, 'Beverages')
        # Check that photo is saved
        self.assertTrue('test_photo' in item.photo.name)
        
        # Check that session 'catname' is cleared
        self.assertNotIn('catname', c.session)

    def test_insert_review_photo_flow(self):
        c = Client()
        dummy_photo = SimpleUploadedFile("test_review_photo.jpg", b"review_file_content", content_type="image/jpeg")
        response = c.post(reverse('insertreview'), {
            't1': 'Alice',
            't2': 'Kitchen A',
            't3': 'Iced Coffee',
            't4': 'Order123',
            't5': '5',
            't6': 'Incredible drink!',
            't7': '2026-05-31',
            't8': dummy_photo
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(review.objects.count(), 1)
        rev = review.objects.first()
        self.assertEqual(rev.customer, 'Alice')
        self.assertEqual(rev.review_text, 'Incredible drink!')
        self.assertTrue('test_review_photo' in rev.photo.name)

    def test_insert_kitchen_logo_flow(self):
        c = Client()
        dummy_logo = SimpleUploadedFile("test_kitchen_logo.jpg", b"kitchen_logo_content", content_type="image/jpeg")
        response = c.post(reverse('insertkitchen'), {
            't1': 'John Doe',
            't2': 'Gourmet Kitchen',
            't3': 'Italian',
            't4': '123 Main St',
            't5': '9876543210',
            't6': 'LIC12345',
            't7': '5',
            't8': 'active',
            't9': dummy_logo
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(kitchen.objects.count(), 1)
        kit = kitchen.objects.first()
        self.assertEqual(kit.owner, 'John Doe')
        self.assertEqual(kit.kitchen_name, 'Gourmet Kitchen')
        self.assertTrue('test_kitchen_logo' in kit.logo.name)
