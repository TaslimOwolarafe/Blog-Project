from urllib import request
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect

from .models import Category, Post, User
from .forms import PostForm, UpdatePostForm, CommentForm
# Create your views here.

# def home(request):
#     return render(request, 'home.html', context={})
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('theBlog:article_detail', args=[str(pk)]))


# def UnlikeView(request, pk):
#     post_u = get_object_or_404(Post, id=request.POST.get('post_id_u'))
#     post_u.likes.remove(request.user)
#     return HttpResponseRedirect(reverse('theBlog:article_detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
    # ordering = ('-post_time', '-post_date')


    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        # context = super(HomeView, self).get_context_data(*args, **kwargs)
        context = super().get_context_data(*args, **kwargs)

        context["cat_menu"] = cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    form = CommentForm

    

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)

        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse("theBlog:article_detail", args=[str(post.id)]))

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        post_like = get_object_or_404(Post, id=self.kwargs['pk'])
        # context = super(HomeView, self).get_context_data(*args, **kwargs)
        total_no_likes = post_like.total_likes()
        context = super().get_context_data(*args, **kwargs)
        liked = False
        if post_like.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context["cat_menu"] = cat_menu
        context["post_likes"] = total_no_likes
        context['liked_post'] = liked
        context["comment_form"] = self.form
        return context
    
    

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'



class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = ['name']

def CategoryView(request, cat):
    category_posts = Post.objects.filter(category=cat)
    return render(request, 'categories.html', context={'cat_dict': cat, 'cat_posts':category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'categoriesList.html', context={'cat_list': cat_menu_list})


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm 
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body'] not allowed

# class UpdateCategoryView(UpdateView):
#     model = Category
#     # form_class = UpdateForm 
#     template_name = 'update_category.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('theBlog:home')

