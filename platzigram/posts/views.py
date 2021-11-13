from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#Forms
from posts.forms import PostForm

#Models
from posts.models import Post

from datetime import datetime

# posts = [
#     {
#         'title': 'Mont Blanc',
#         'user': {
#             'name': 'Yésica Cortés',
#             'picture': 'https://picsum.photos/60/60/?image=1027'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/800/800?image=1036',
#     },
#     {
#         'title': 'Via Láctea',
#         'user': {
#             'name': 'Christian Van der Henst',
#             'picture': 'https://picsum.photos/60/60/?image=1005'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/800/800/?image=903',
#     },
#     {
#         'title': 'Nuevo auditorio',
#         'user': {
#             'name': 'Uriel (thespianartist)',
#             'picture': 'https://picsum.photos/60/60/?image=883'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/800/800/?image=1076',
#     }
# ]


@login_required()
def list_posts(request):
    """List existing posts"""
    posts = Post.objects.all().order_by('-created') #-created -> Descendent
    return render(request, 'posts/feed.html', {'posts':posts})

@login_required
def create_post(request):
    """Create new post view"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form':form,
            'user': request.user,
            'profile':request.user.profile
        }
    )