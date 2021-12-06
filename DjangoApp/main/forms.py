from django.forms import ModelForm
from .models import MP3Audio

class MP3AudioForm(ModelForm):
    class Meta:
        model = MP3Audio
        fields = ['file_name', 'mp3_audio_file']
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None) # Now you use self.request to access request object.
        super(MP3AudioForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance =  super(MP3AudioForm, self).save(commit=False)
        instance.ip_address = self.request.META['REMOTE_ADDR']
        if commit:
            instance.save()
        return instance