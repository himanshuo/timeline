__author__ = 'himanshu'
#from django.forms import widgets
from rest_framework import serializers
from osft.models import Timeline

class TimelineSerializer(serializers.ModelSerializer):
    """
    NOTE: this is the stuff the tutorial made me do to explain the proces.
    the below ModelSerializer likely does all this internally.
    to revert, make sure to change the inherited class to serializers.Serializer

    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    title = serializers.CharField(required=False,
                                  max_length=100)
    #code = serializers.CharField(widget=widgets.Textarea,
    #                             max_length=100000)
    #linenos = serializers.BooleanField(required=False)
    #language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,
    #                                   default='python')
    #style = serializers.ChoiceField(choices=STYLE_CHOICES,
    #                                default='friendly')
    users = serializers.CharField(required=False, max_length=100)
    wiki = serializers.CharField(widget=widgets.Textarea)
    def restore_object(self, attrs, instance=None):

        Create or update a new Timeline instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.

        if instance:
            # Update existing instance
            instance.title = attrs.get('title', instance.title)
            #instance.code = attrs.get('code', instance.code)
            #instance.linenos = attrs.get('linenos', instance.linenos)
            #instance.language = attrs.get('language', instance.language)
            #instance.style = attrs.get('style', instance.style)
            instance.users = attrs.get('users', instance.users)
            instance.wiki = attrs.get('wiki', instance.wiki)
            return instance

        # Create new instance
        return Timeline(**attrs)
    """
    class Meta:
        model = Timeline
        fields = ('id', 'title', 'author', 'wiki')