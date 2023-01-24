from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.contrib import messages


def blog(request):
    """A view to return the blog page"""
    return render(request, 'blog/blog.html')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'blog_detail.html',
            {
                'post': post,
                'liked': liked,
            },
        )


    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'blog_detail.html',
            {
                'post': post,
                'liked': liked,
            },
        )


class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(self.request.user)
            liked = False
        else:
            post.likes.add(self.request.user)

        return HttpResponseRedirect(reverse('blog_detail', args=[slug]))


def add_item(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('PostList')
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'add_blog.html', context)


def edit_item(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return redirect('PostList')
    form = PostForm(instance=post)
    context = {
        'form': form
    }
    return render(request, 'edit_blog.html', context)


def toggle_item(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST)
    if request.method == 'POST':
        post.done = not post.done
        form.save()
        return redirect('PostList')


def delete_item_view(request, slug):
    text_type = 'post'
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post, 'text_type': text_type}
    return render(request, 'delete_blog.html', context)


def delete_post(request, slug):
    """ Method to delete a post"""
    post = get_object_or_404(Post, slug=slug)
    if post.author.id == request.user.id:
        post.delete()
        messages.success(request, "Post deleted! Feel free to post a new one")
        return (redirect("home"))
