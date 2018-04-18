#from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from blog.models import Post
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList
from django.views.generic.edit import FormView
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

# Create your views here. 각 class마다 default로 html이 지정되어있음
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 5

class PostDV(DetailView):
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'
    paginate_by = 10

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True
    paginate_by = 10

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'

class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'

class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        schWord = '%s' % self.request.POST['search_word']
        #post_list = Post.objects.filter(Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()
        post_list = Post.objects.filter(Q(title__icontains=schWord) | Q(description__icontains=schWord)).distinct()
        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list
        return render(self.request, self.template_name, context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tag']
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PostCreateView, self).form_valid(form)

class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'blog/post_change_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(owner = self.request.user)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tag']
    success_url = reverse_lazy('blog:index')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')
