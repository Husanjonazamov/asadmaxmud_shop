from rest_framework import serializers
from ...models import UserModel

class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        exclude = [
            "created_at",
            "updated_at",
        ]
        

class ListUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        pass

class RetrieveUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        pass

class CreateUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        pass
