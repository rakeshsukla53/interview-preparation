

class profilePictures(models.Model):
    userName = models.CharField(max_length=30, primary_key=True)
    picture = models.ImageField(upload_to='ProfilePictures', blank = True)
