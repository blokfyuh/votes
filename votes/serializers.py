
""" Serializers for api support on Votes app. """

# Third party imports
from rest_framework import serializers

# Imports form Vote app
from .models import Vote


class VoteSerializer(serializers.ModelSerializer):

    """ Returns serialized data of Vote instances. """

    class Meta:
        model = Vote
        fields = '__all__'
        
