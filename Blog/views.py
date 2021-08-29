from django.shortcuts import get_object_or_404, render
from Account.models import User
from taggit.models import Tag
from Paper.models import My_Papers
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def blog(request, tag_slug=None):
    html        = 'blog/blog.html'
    tag         = None
    user        = get_object_or_404(User,id=1)
    tags        = Tag.objects.all()
    papers      = My_Papers.objects.all()
    last_papers    = My_Papers.objects.all()[:5]

    if tag_slug:
        tag      = get_object_or_404(Tag, slug=tag_slug)
        papers = papers.filter(tag__in=[tag])
        
    paginator = Paginator(papers , 1 )
    page = request.GET.get('page')
    
    try:
        papers = paginator.page(page)
    except PageNotAnInteger:
        papers = paginator.page(1)
    except EmptyPage:
        papers = paginator.page(paginator.num_pages)
        
    data = {    'user'  :user ,
                'papers' :papers ,
                'tags' :tags ,
                "last_papers":last_papers , 
                'page':page,
            }
    
    return render(request,html,data);
