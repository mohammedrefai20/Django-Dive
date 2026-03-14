from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.views import View
from .models import Post, Comment
from rest_framework import serializers

# def home(request):
#     return HttpResponse("Hello, this is the Home page.")

    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'body', 'date_added']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['date_added'] = instance.date_added.strftime('%Y-%m-%d')
        return rep



class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True,source='comment_set')
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'date_posted', 'comments'] 
    def to_representation(self, instance):
        rep=super().to_representation(instance)
        rep['date_posted'] = instance.date_posted.strftime('%Y-%m-%d')
        rep['comments_count'] = Comment.objects.filter(post=instance).count()
        return rep


class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
