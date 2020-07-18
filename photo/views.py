from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from .models import Photo

@login_required
def photo_list(request):  #함수형 뷰의 첫 매개변수는 항상 request
    #보여줄 사진 데이터
    photos = Photo.objects.all() #objects는 orm관련 매니저 관련 기본이름
    return render(request, 'photo/list.html', {'photos':photos}) #photo밑이 아니라 template밑부터임


from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.shortcuts import redirect #upload에 필요

class PhotoUploadView(LoginRequiredMixin,CreateView):
    model = Photo
    fields = ['photo','text'] # 작성자(author), 작성시간(created)
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            #데이터가 올바르다면 저장을 한다.
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

class PhotoDeleteView(LoginRequiredMixin,DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'
        
class PhotoUpdateView(LoginRequiredMixin,UpdateView):
    model = Photo
    fields=['photo','text']
    template_name='photo/update.html'