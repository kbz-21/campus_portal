# from dj_rest_auth.registration.serializers import RegisterSerializer
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class CustomRegisterSerializer(RegisterSerializer):
#     username = serializers.CharField(max_length=150, required=True)

#     def get_cleaned_data(self):
#         data = super().get_cleaned_data()
#         data['username'] = self.validated_data.get('username', '')
#         return data


from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    def save(self, request):
        user = super().save(request)
        # Auto-assign Student role
        student_group, _ = Group.objects.get_or_create(name='Student')
        user.groups.add(student_group)
        user.save()
        return user







#this is serilizer