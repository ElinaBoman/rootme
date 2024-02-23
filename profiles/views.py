from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm


def profile_view(request):
    """
    Display user profiles.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
   
    print('profile', profile)

    orders = profile.orders.all()

    print('order', orders)
    
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders
    }


    return render(request, template, context)
