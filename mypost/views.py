from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Postdata, Category, Comment
from django.urls import reverse_lazy, reverse
from .forms import PostForm
from django.http import HttpResponseRedirect




# Create your views here.

#def home(request):
#   return render(request, 'home.html', {})

class Homeview(ListView):
    model = Postdata
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Postdata
    template_name = 'a-details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Postdata, id=self.kwargs['pk'])
        total_likes = stuff.total_like()

        # This block of code is used to effect the unlike post in the article details page
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class BlogPostView(CreateView):
    model = Postdata
    form_class = PostForm
    template_name = 'blog_post.html'
    #fields = '__all__'


class AddCommentView(CreateView):
    model = Comment
    #form_class = PostForm
    template_name = 'add_comment.html'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.post.id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')

class UpdateBlogPost(UpdateView):
    model = Postdata
    template_name = 'update_post.html'
    fields = ['title', 'title_tag', 'body', 'header_image']

class DeleteBlogPost(DeleteView):
    model = Postdata
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home') # This redirects you back to homepage after deleting post

def LikeView(request, pk):
    post = get_object_or_404(Postdata, id=request.POST.get('post_id'))
    # The block of code below is for unliking a post
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-details', args=[str(pk)]))

    
