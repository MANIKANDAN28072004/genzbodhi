from django.contrib.auth.models import User
from profiles.models import profiles 

def user_profile(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            profile = profiles.objects.get(user=user)
            return {
                'profile': profile,
            }
        except:
            pass
    else:
        return {}