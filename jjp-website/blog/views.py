'''
Copyright 2021 by John Carter
Created: 2021/08/07 21:12:00
Last modified: 2021/09/10 22:41:16
'''
from django.shortcuts import render
import boto3

from .models import BlogPost

PHOTO_URL = 'https://johnjohnphotos-media.s3.amazonaws.com'


def jjp_blog(request):
    '''
    Display listing of most current blog posts
    '''
    latest_post_list = BlogPost.objects.order_by('-pub_date')[:5]
    context = {
        'photo_url': PHOTO_URL,
        'latest_post_list': latest_post_list,
    }
    return render(request, 'jjp_blogs.html', context)


def blog_post(request, post_id):
    '''
    Display one blog post
    '''
    post = BlogPost.objects.get(id=post_id)
    context = {
        'photo_url': PHOTO_URL,
        'post': post
    }
    return render(request, 'blog_post.html', context)