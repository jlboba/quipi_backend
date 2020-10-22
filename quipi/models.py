from django.db import models

# =========================
#         PROMPTS
# =========================
class Prompt(models.Model):
    text = models.CharField(max_length=300)
    creator_name = models.CharField(max_length=200)
    accepted = models.BooleanField(default=False)

    class Meta:
        db_table = 'prompt'

    def __str__(self):
        return self.text 

# =========================
#         QUIPS
# =========================
class Quip(models.Model):
    text = models.CharField(max_length=300)
    times_played = models.IntegerField(default=0)
    times_chosen = models.IntegerField(default=0)
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE, related_name='quips')
    creator_name = models.CharField(max_length=200)
    accepted = models.BooleanField(default=False)

    class Meta: 
        db_table = 'quip'

    def __str__(self):
        return self.text 