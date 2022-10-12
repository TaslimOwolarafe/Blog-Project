# from re import template
from theBlog.models import Profile
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from . forms import ProfilePageForm, SignUpForm, EditProfileForm, PasswordChangingForm
from theBlog.models import Post

# Create your views here.
class CreateProfilePageView(generic.CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile_page.html'
    # fields = "__all__"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('theBlog:home')

class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    # fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url']
    success_url= reverse_lazy('theBlog:home')

class showProfilePageView(generic.DetailView):
    model = Profile
    template_name = 'registration/profile_page.html'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        user_posts = Post.objects.filter(author=page_user.user)

        context["page_user"] = page_user
        context["user_posts"] = user_posts
        return context

    # def showProfilePageView(request, user):
    #     user = request.user.username
    #     return render(request, 'registration/profile_page.html', context={'user': user})

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('members:password_success')
    # success_url = reverse_lazy('theBlog:home')

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('theBlog:home')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('theBlog:home')

    def get_object(self):
        return self.request.user

def password_success(request):
    return render(request, 'registration/password_success.html', context={})


# from django.forms.models import model_to_dict

# def profile(request):
#    profile = model_to_dict(request.user.profile)
#    return render(request, 'registration/profile_page.html', {'profile':profile})