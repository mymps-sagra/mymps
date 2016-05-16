from rest_framework import serializers

from rest.models import Period, Rest


class PeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Period
        fields = "__all__"
        # fields = ('name', 'data', 'comment')
        

class RestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rest
        fields = (
            'period', 
            'item' , 'design', 'packing', 'unit', 'store', 'target', 'part', 
            'rest_total',
        )
