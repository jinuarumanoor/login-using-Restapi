from rest_framework import serializers
from .models import Account

class UserSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField()
    profile_picture = serializers.ImageField()
    

    class Meta:
        model=Account
        fields=['username','email','phone_number','password','profile_picture','date_of_birth']
        extra_kwargs={
            'password':{'write_only':True}
        }
    

   
    def create(self, validated_data):
        user =  Account.objects.create_user(validated_data['username'],validated_data['email'],validated_data['phone_number'],validated_data['password'])
        user.date_of_birth = validated_data['date_of_birth']
        user.profile_picture = validated_data['profile_picture']
        user.save()
        return user

    
class UserLoginSerializer(serializers.ModelSerializer):
    email= serializers.EmailField(max_length=255)
    class Meta:
        model=Account
        fields = ['email','password']

class UserprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email' , 'phone_number','profile_picture','date_of_birth']

     