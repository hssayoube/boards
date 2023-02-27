from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import View
from .forms import UserUpdateForm, ProfileUpdateForm

# class ProfileView(LoginRequiredMixin, UpdateView):
#     model = User
#     fields = ('first_name', 'last_name', 'email', )
#     template_name = 'profile.html'
#     success_url = reverse_lazy('profile')
#     def get_object(self):
#         return self.request.user
    

class UserProfile(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        
        return render(request, 'profile.html', context)
    
    def post(self,request):
        user_form = UserUpdateForm(
            request.POST, 
            instance=request.user
        )
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            return redirect('profile')
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            
            return render(request, 'profile.html', context)
