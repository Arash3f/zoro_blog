from django.shortcuts import get_object_or_404, render
from taggit.models import Tag
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from Paper.forms import Comment_From
from Paper.models import My_Papers
from Comment.models import Comment
from Account.models import User

def paper_detail(request,year,month,day,post):
    tags        = Tag.objects.all()
    user        = get_object_or_404(User,id=1)
    another_papers    = My_Papers.objects.all()[:5]
    paper       = get_object_or_404(My_Papers, slug=post , publish__year=year, publish__month=month, publish__day=day)
    comments    = Comment.objects.filter(paper = paper).order_by('-Date')
    new_comment = None

    paper.view_plus(request)

    if request.method == 'POST':
        comment_form = Comment_From(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.paper = paper
            new_comment.user = request.user
            new_comment.save()
            comment_form = Comment_From()
    else:
        comment_form = Comment_From()
        
    paginator = Paginator(comments , 10 )
    page = request.GET.get('page')

    try:
        com = paginator.page(page)
    except PageNotAnInteger:
        com = paginator.page(1)
    except EmptyPage:
        com = paginator.page(paginator.num_pages)
    
    data = {    'user'  :user ,
                'paper' :paper ,
                'comments':comments,
                'page':page,
                'comment_form':comment_form,
                "another_papers":another_papers , 
                'tags' :tags ,
            }
    
    return render(request, 'Paper/details.html' , data)

