from rest_framework import serializers

from .models import Posts , Events , User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ('bio', 'dob',  'city', 'photo')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('id','username','email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.user = profile_data.get('user', profile.user)
        profile.bio = profile_data.get('bio', profile.bio)
        profile.dob = profile_data.get('dob', profile.dob)
        profile.city = profile_data.get('city', profile.city)
        profile.photo = profile_data.get('photo', profile.photo)
        profile.save()

        return instance

class PostsSerializer(serializers.ModelSerializer):
    def get_username(self, obj):
        return obj.user.username
    
    username = serializers.SerializerMethodField()
    class Meta:
        fields = ('id' ,'user', 'username', 'image', 'image1','image2','image3','image4','discerption','comments', 'likes','created_at')
        model = Posts


class EventsSerializer(serializers.ModelSerializer):

    def get_username(self, obj):
        return obj.user.username
    
    username = serializers.SerializerMethodField()

    class Meta:
        fields = ('id','user', 'title', 'username', 'image','image1','image2','image3','image4','image5',
        'image6','image7','image8','image9','image10','image11','image12','image13','image14','image15','image16',
        'image17','image18','image19','image20','discerption', 'date')
        model = Events