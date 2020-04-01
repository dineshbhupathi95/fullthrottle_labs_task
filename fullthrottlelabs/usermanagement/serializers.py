from rest_framework.serializers import *
from .models import *



class UserActivitySerializer(ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ["start_time","end_time"]

class UserSerializer(ModelSerializer):
    activity = UserActivitySerializer(many=True)
    class Meta:
        model = User
        fields = ["id","real_name","tz","activity"]

    def to_representation(self, instance):
        # instance is the model object. create the custom json format by accessing instance attributes normaly and return it
        identifiers = dict()
        activity_obj = ActivityPeriod.objects.filter(activity_periods=instance.id).values("start_time","end_time")
        identifiers['id'] = instance.id
        identifiers['real_name'] = instance.real_name
        identifiers['tz'] = instance.tz
        identifiers['activity_periods'] = activity_obj
        representation = {
            'members':[ identifiers,]
        }

        return representation