from django.db import models
from django.utils.text import slugify

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_upload(instance,filename):
    imageName , extension = filename.split(".")
    return 'jobs/%s.%s'%(instance.id,extension)


class Job(models.Model):
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=15, choices = JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    #category Forienkey relationship
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to = image_upload)
    
    
    slug = models.SlugField(blank=True,null=True)
    
    def save(self,*args,**kwargs):
        self.slug =slugify(self.title)
        super (Job,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    
class Apply(models.Model):
    
    job = models.ForeignKey(Job,related_name='apply', on_delete=models.CASCADE)
    name = models.CharField(max_length=50,blank=True, null=True)
    email = models.EmailField(max_length=100,blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    file = models.FileField(upload_to='apply/',blank=True, null=True)
    coverText = models.TextField(max_length=500,blank=True, null=True)
    created_at =models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name