from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import Task, ChangingStatus, Reminder


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class TaskSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'performer', 'observer',
                  'status', 'started_at', 'planning_completed_at', 'completed_at'
                  ]
        read_only_fields = ['started_at', 'completed_at']


class ChangingStatusSerializer(ModelSerializer):
    class Meta:
        model = ChangingStatus
        fields = ['id', 'previous_status', 'next_status', 'task', 'changed_by']
        read_only_fields = ['previous_status', 'changed_by']


class ReminderSerializer(ModelSerializer):

    class Meta:
        model = Reminder
        fields = ['id', 'task', 'text', 'users']
