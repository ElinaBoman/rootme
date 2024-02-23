from django.shortcuts import render


def profile_view(request):
    """
    Display user profiles.
    """

    template = 'profiles/profile.html'
    context = {}


    return render(request, template, context)
