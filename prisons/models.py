from django.db import models

# Info for populating individual prison templates
class Prison(models.Model):
    name = models.CharField(max_length=50)
    agency = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    security_level = models.CharField(max_length=25)
    population = models.SmallIntegerField()
    population_updated = models.DateTimeField()
    warden = models.CharField(max_length=20)
    google_maps = models.URLField()
    visitation_hours = models.TextField()
    jpay = models.URLField()

    def __str__(self):
        return self.name

    def getArticles(self):
        return self.newsarticle_set.all() #pylint: disable=no-member

# News articles with tags(foreign keys) for specific prisons
class NewsArticle(models.Model):
    headline = models.CharField(max_length=255)
    article_url = models.URLField()
    img_url = models.URLField(null=True)
    prisons = models.ManyToManyField(Prison)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.headline