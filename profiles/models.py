from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User

districChoice = (

    ('Dhaka', 'Dhaka'),
    ('Faridpur', 'Faridpur'),
    ('Gazipur', 'Gazipur'),
    ('Gopalganj', 'Gopalganj'),
    ('Jamalpur', 'Jamalpur'),
    ('Kishoreganj', 'Kishoreganj'),
    ('Madaripur', 'Madaripur'),
    ('Manikganj', 'Manikganj'),
    ('Munshiganj', 'Munshiganj'),
    ('Mymensingh', 'Mymensingh'),
    ('Narayanganj', 'Narayanganj'),
    ('Narsingdi', 'Narsingdi'),
    ('Netrokona', 'Netrokona'),
    ('Rajbari', 'Rajbari'),
    ('Shariatpur', 'Shariatpur'),
    ('Sherpur', 'Sherpur'),
    ('Tangail', 'Tangail'),
    ('Bogura', 'Bogura'),
    ('Joypurhat', 'Joypurhat'),
    ('Naogaon', 'Naogaon'),
    ('Natore', 'Natore'),
    ('Nawabganj', 'Nawabganj'),
    ('Pabna', 'Pabna'),
    ('Rajshahi', 'Rajshahi'),
    ('Sirajgonj', 'Sirajgonj'),
    ('Dinajpur', 'Dinajpur'),
    ('Gaibandha', 'Gaibandha'),
    ('Kurigram', 'Kurigram'),
    ('Lalmonirhat', 'Lalmonirhat'),
    ('Nilphamari', 'Nilphamari'),
    ('Panchagarh', 'Panchagarh'),
    ('Rangpur', 'Rangpur'),
    ('Thakurgaon', 'Thakurgaon'),
    ('Barguna', 'Barguna'),
    ('Barishal', 'Barishal'),
    ('Bhola', 'Bhola'),
    ('Jhalokati', 'Jhalokati'),
    ('Patuakhali', 'Patuakhali'),
    ('Pirojpur', 'Pirojpur'),
    ('Bandarban', 'Bandarban'),
    ('Brahmanbaria', 'Brahmanbaria'),
    ('Chandpur', 'Chandpur'),
    ('Chattogram', 'Chattogram'),
    ('Cumilla', 'Cumilla'),
    ("Cox's Bazar", "Cox's Bazar"),
    ('Feni', 'Feni'),
    ('Khagrachari', 'Khagrachari'),
    ('Lakshmipur', 'Lakshmipur'),
    ('Noakhali', 'Noakhali'),
    ('Rangamati', 'Rangamati'),
    ('Habiganj', 'Habiganj'),
    ('Maulvibazar', 'Maulvibazar'),
    ('Sunamganj', 'Sunamganj'),
    ('Sylhet', 'Sylhet'),
    ('Bagerhat', 'Bagerhat'),
    ('Chuadanga', 'Chuadanga'),
    ('Jashore', 'Jashore'),
    ('Jhenaidah', 'Jhenaidah'),
    ('Khulna', 'Khulna'),
    ('Kushtia', 'Kushtia'),
    ('Magura', 'Magura'),
    ('Meherpur', 'Meherpur'),
    ('Narail', 'Narail'),
    ('Satkhira', 'Satkhira'),

)

bloodGroup = (
    ('A+', 'A+'),
    ('O+', 'O+'),
    ('B+', 'B+'),
    ('AB+', 'AB+'),
    ('A-', 'A-'),
    ('O-', 'O-'),
    ('B-', 'B-'),
    ('AB-', 'AB-'),



)


class Aprofile(models.Model):
    name = models.CharField(max_length=200, blank=True)
    bio =  models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='avatar.png', upload_to='avatars/')
    address = models.CharField(
        max_length=15, choices=districChoice, default="Dhaka")
    phoneNum = models.BigIntegerField(default=880)
    totalDonate = models.IntegerField(default=0)
    bloodGroup = models.CharField(max_length=3,default="A+", choices=bloodGroup)
    lastGiven = models.DateField(default='2000-08-02') 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.bloodGroup}'
