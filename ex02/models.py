from django.db import models


class HistoryEntry(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return '{} : {}'.format(self.created, self.text)
