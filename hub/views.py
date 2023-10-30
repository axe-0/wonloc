from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms import ValidationError
from django import forms
from bounties.models import Bounty, ApplicationForm , Fund , Apply 
from threads.models import Post, Comment
from resources.models import LibraryItem
from django.http import JsonResponse
# Create your views here.
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']
    
#get all bounties threads and library objects and parse them into content
bounties = Bounty.objects.all()
threadz= Post.objects.all()
library = LibraryItem.objects.all()
comments = Comment.objects.all()


#context for diffrent app objects 
context = {
        'bounties' : bounties,
        'threadz':threadz,
        'library': library,
        'comments': comments,
    }

def music_page(request):
    form = CommentForm()
    user = request.user
    context['form'] = form
    context['user'] = user
    return render(request, 'music_hub.html',context)

def bounty_details(request, bount_id):
    bounty_dets = get_object_or_404(Bounty, pk=bount_id)
    context['bounty_dets']= bounty_dets
    return render(request, 'bounty_details.html', context)


class ApplicationSubmission(forms.ModelForm):

    class Meta:
        model = ApplicationForm
        fields = ['name','email','resume','cover_letter','portfolio']



def apply_bounty(request,apply_id):
    application_info = get_object_or_404(Apply,pk=apply_id)
    context['application_info']= application_info
    form = ApplicationSubmission()
    context['form']=form
    context['success'] = False
    return render(request,'application.html', context)

def fund_bounty(request,fund_id):
    fund_info = get_object_or_404(Fund,pk=fund_id)
    context['fund_info']= fund_info
    return render(request, 'fund_bounty.html',context)

#Bounty submitted applications ----------------------------

def application_submission(request):
    if request.method == 'POST':
        form = ApplicationSubmission(request.POST, request.FILES)
        if form.is_valid():
            #save to the database
            new_application = form.save()
            context['success'] = True

            # Redirect to a success page
            return render(request,'application.html', context) 

    else:

        form = ApplicationSubmission()
        context['form'] = form

        return render(request,'application.html', context) 

#like button ----------------------------

def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    num = post.likes.count()
    
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        num = post.likes.count()
        print(f"user {request.user} unliked post\n likes:{num}")
        liked = False
    else:
        post.likes.add(request.user)
        num = post.likes.count()
        print(f"user {request.user} liked post \n likes:{num}")
        liked = True
   
    return JsonResponse({'liked': liked})

#Comment area ----------------------------

def comment_sub(request ,post_id):
    main_post = get_object_or_404(Post,pk=post_id)
    if request.method =='POST': 
        try:
            comment_content = CommentForm(request.POST)
            if comment_content.is_valid():
                content = comment_content.cleaned_data['content']
                print("it's working")
                new_comment = Comment(user=request.user, post=main_post, content=content)
                new_comment.save()
            else:
                # Handle form validation errors
                print("not working")
                raise ValidationError("Form is invalid.")
                
        except Exception as e:
                print(f"Error creating comment: {e}")
                print(comment_content.errors)

        # Retrieve the comments associated with the main post

    comments = Comment.objects.filter(post=main_post)
    context['comments'] = comments

        
    return HttpResponseRedirect(reverse('hub:music_hub'))

