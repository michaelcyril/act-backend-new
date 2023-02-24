from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'event'


class EventFile(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    file = models.BinaryField()

    def __str__(self):
        return f'{self.event_id.title}'

    class Meta:
        db_table = 'event_file'


class New(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'new'


class NewFile(models.Model):
    new_id = models.ForeignKey(New, on_delete=models.CASCADE)
    file = models.BinaryField()

    def __str__(self):
        return f'{self.new_id.title}'

    class Meta:
        db_table = 'new_file'
