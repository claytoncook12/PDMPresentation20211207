from pathlib import Path
from django.db import models
from django.core.exceptions import ValidationError

class MP3Audio(models.Model):
    file_name = models.CharField("File Name", max_length=300)
    mp3_audio_file = models.FileField(upload_to="")
    ip_address = models.GenericIPAddressField(default= "0.0.0.0")
    
    def clean(self, *args, **kwargs):
        super().clean()
        if Path(self.mp3_audio_file.path).suffix != ".mp3":
            raise ValidationError('Reference Audio MP3 file must be .mp3')