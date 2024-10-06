from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class Login(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30, choices=(("user", "user"), ("vet", "vet")))
    added_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class UserDetail(models.Model):
    uid = models.ForeignKey(Login, on_delete=models.CASCADE)
    dob = models.CharField(max_length=30)
    address = models.TextField()
    photo = models.ImageField(upload_to="profiles")

    def user_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.photo.url))


# class ServiceCategories(models.Model):
#     cate_name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.cate_name
#
#
# class Service(models.Model):
#     category = models.ForeignKey(ServiceCategories, on_delete=models.CASCADE)
#     name = models.CharField(max_length=60)
#     desc = models.TextField()
#     price = models.FloatField()
#     duration = models.IntegerField()
#     available = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_featured = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.name
#
#
# class ServiceBooking(models.Model):
#     user = models.ForeignKey(Login, on_delete=models.CASCADE)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     date_booked = models.DateTimeField(auto_now_add=True)
#     # scheduled_date = models.DateTimeField()
#     is_confirmed = models.BooleanField(default=False)
#     # total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#
#     def __str__(self):
#         return f" {self.id}  {self.service.name}  {self.user.name}"
#
#
#
# class Card(models.Model):
#     uid = models.ForeignKey(Login, on_delete=models.CASCADE)
#     cardholder_name = models.CharField(max_length=255)
#     card_number = models.CharField(max_length=16)
#     expiration_date = models.DateField()
#     cvv = models.CharField(max_length=4)
#
#
#     def __str__(self):
#         return self.cardholder_name
#
#
# class Payment(models.Model):
#     user = models.ForeignKey(Login, on_delete=models.CASCADE)
#     booking = models.ForeignKey(ServiceBooking, on_delete=models.CASCADE)
#     payment_method = models.CharField(max_length=50, choices=(('Cash', 'Cash'), ('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card')))
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     transaction_id = models.CharField(max_length=100, null=True)
#     payment_status = models.CharField(max_length=50, choices=(('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')))
#     payment_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Payment {self.id} - {self.user.name} - {self.amount} - {self.payment_method}"
#
#
# class Vet(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.TextField()
#     phone_number = models.CharField(max_length=20)
#     email = models.EmailField()
#     specialization = models.CharField(max_length=255)
#     # available_services = models.ManyToManyField(Service, blank=True)
#     about = models.TextField()
#     image = models.ImageField(upload_to='vet_images/')
#     operating_hours = models.CharField(max_length=255, null=True)
#     social_media_links = models.URLField(null=True)
#     languages_spoken = models.CharField(max_length=100)
#
#
#     def vet_photo(self):
#         return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))
#
#
# class PetProductShop(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.TextField()
#     phone_number = models.CharField(max_length=20)
#     email = models.EmailField()
#     about = models.TextField()
#     # products_offered = models.ManyToManyField(Product, blank=True)
#     image = models.ImageField(upload_to='pet_shop_images/')
#     operating_hours = models.CharField(max_length=255, null=True, blank=True)
#     social_media_links = models.URLField(null=True, blank=True)
#     website = models.URLField(null=True, blank=True)
#     # Add other relevant fields as needed
#
#     def __str__(self):
#         return self.name
#
#
#
# class BlogCategory(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Blog(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
#     publication_date = models.DateTimeField(auto_now_add=True)
#     image = models.ImageField(upload_to='blog_images/')
#     is_featured = models.BooleanField(default=False)
#     status = models.CharField(max_length=20, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
#     # slug = models.SlugField(unique=True)
#     # Add other relevant fields as needed
#
#     def __str__(self):
#         return self.title
#
#
#
#
# class AnimalType(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Animal(models.Model):
#     name = models.CharField(max_length=255)
#     animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
#     description = models.TextField()
#     age = models.IntegerField()
#     gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('unknown', 'Unknown')])
#     color = models.CharField(max_length=50)
#     size = models.CharField(max_length=20, choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])
#     weight = models.FloatField(null=True, blank=True)
#     health_records = models.TextField(null=True, blank=True)
#     breed = models.CharField(max_length=100, null=True, blank=True)
#     available_for_adoption = models.BooleanField(default=True)
#     image = models.ImageField(upload_to='animal_images/', null=True, blank=True)
#     shelter = models.ForeignKey('AnimalShelter', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.name} ({self.animal_type.name})"
#
#
# class Adoption(models.Model):
#     user = models.ForeignKey(Login, on_delete=models.CASCADE)
#     animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
#     adoption_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
#
#     def __str__(self):
#         return f"{self.user.name} adopted {self.animal.name}"
#
#
#
# class AnimalShelter(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.TextField()
#     phone_number = models.CharField(max_length=20)
#     email = models.EmailField()
#     about = models.TextField()
#     # animals_supported = models.ManyToManyField(AnimalType, blank=True)
#     # available_animals = models.ManyToManyField(Animal, blank=True)
#     image = models.ImageField(upload_to='animal_shelter_images/', null=True, blank=True)
#     operating_hours = models.CharField(max_length=255, null=True, blank=True)
#     social_media_links = models.URLField(null=True, blank=True)
#     website = models.URLField(null=True, blank=True)
#     # Add other relevant fields as needed
#
#     def __str__(self):
#         return self.name
#
#
# class RescueCenter(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.TextField()
#     phone_number = models.CharField(max_length=20)
#     email = models.EmailField()
#     about = models.TextField()
#     website = models.URLField(null=True, blank=True)
#     image = models.ImageField(upload_to='rescue_center_images/', null=True, blank=True)
#     operating_hours = models.CharField(max_length=255, null=True, blank=True)
#     social_media_links = models.URLField(null=True, blank=True)
#     # Add other relevant fields as needed
#
#     def __str__(self):
#         return self.name
#
# class Feedback(models.Model):
#     user = models.ForeignKey(Login, on_delete=models.CASCADE)
#     rating = models.PositiveIntegerField()
#     comments = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Feedback from {self.user.name}"
#
#
# class Contact(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     subject = models.CharField(max_length=255)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('resolved', 'Resolved')], default='pending')
#
#     def __str__(self):
#         return f"Contact from {self.name}"
