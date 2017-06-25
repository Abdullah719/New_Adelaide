from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import User
from first_app.forms import FormName,UserProfile
from .models import Post
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
from bs4 import BeautifulSoup

# Create your views here.

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


def post_detail(request,id):
    query = get_object_or_404(Post,id=id)
    data1 = {
        'instance':query
    }
    return render(request,'first_app/post_detail.html',context=data1)

def index(request):
    queryset_list =Post.objects.all().order_by('-timestamp')
    paginator = Paginator(queryset_list, 2) # Show 25 contacts per page
    page = request.GET.get('page')

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    data = {
        'data':queryset
    }

    return render(request,'first_app/index.html',context=data)

@login_required
def special(request):
    return HttpResponse('YOU ARE LOG IN!')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def help(request):
    helpdir = {'help_dir':'i am from views.py'}
    return render(request,'first_app/help.html')



def forms_view(request):
    register = False
    # form = forms.FormName()

    if request.method == 'POST':
        user_info_form = FormName(data=request.POST)
        user_pro = UserProfile(data=request.POST)

        if  user_info_form.is_valid() and user_pro.is_valid():

            user=user_info_form.save()
            user.set_password(user.password)
            user.save()

            # profile  = user_pro.save(commit=False)
            # profile.user =  user
            #
            # if 'profile.pic' in request.FILES:
            #     profile.pic = request.FILES['profile_pics']
            #
            #     profile.save()
            #
            #  request = True
        else:
            print('error')
    else:
        user_info_form = FormName()
        user_pro = UserProfile()

    return render(request,'first_app/form.html',{'user_info_form':user_info_form,
                                                 'user_pro':user_pro,
                                                 'registered':register})


def user_login(request):

    if  request.method == 'POST':
        useername = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=useername,password=password)

        if user:
            if user.is_active:
                login(request,user)
                print('Login comrplete!')
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            raise user.ValidationError("User does not exist.")
    else:
        return render(request,'first_app/login.html',{})



def maan(request):
    rrr = requests.get('https://hamariweb.com/islam/adelaide_prayer-timing8425.aspx')
    r = rrr.content
    soup = BeautifulSoup(r, "html.parser")
    data = soup.find_all('div', {'class': 'col-xs-6 col-sm-6 col-lg-12'})
    dic1 = {}
    list1 = []
    null_list = []
    names = ['fajar', 'sunrise', 'zohar', 'asr', 'magrib', 'isha']

    for i in data:
        try:
            temp = i.find_all('span', {'class': 'h5'})[0].text

            if temp != None:
                list1.append(temp)
            else:
                null_list.append(temp)
        except:
            pass

    for i in range(0, len(list1)):
        dic1[names[i]] = list1[i]
    print(dic1)

    return render(request,'first_app/main.html',context=dic1)