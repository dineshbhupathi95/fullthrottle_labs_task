from django.db import models

class User(models.Model):
    import pytz
    TIMEZONES = tuple(zip(pytz.all_timezones,pytz.all_timezones))
    real_name = models.CharField(max_length=225)
    tz = models.CharField(max_length=225,choices=TIMEZONES)



class ActivityPeriod(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    activity_periods = models.ForeignKey('usermanagement.User', on_delete=models.CASCADE, null=True,
                                         blank=True, related_name="activity")