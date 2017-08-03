from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.db import transaction
from .models import PeopleResurne, Education, Work
from django.core.paginator import Paginator, Page


# Create your views here.
def index(request):
    return redirect('/list_page_1/')


def create_page(request):
    return render(request, 'index.html', {'title': '创建页'})


@transaction.atomic
def create_info(request):
    try:
        if request.method == 'POST':
            sid = transaction.savepoint()
            post = request.POST
            name = post.get('name', '')
            image = request.FILES.get('image', '')
            age = post.get('age', '')
            birthday = post.get('birthday', '')
            identitycard = post.get('identity_card', '')
            identitynum = post.get('identity_num', '')
            phone = post.get('phone', '')
            email = post.get('email', '')
            school = post.getlist('school', '')
            educationinfo = post.getlist('education_inof', '')
            worktimestart = post.getlist('worktime_start', '')
            worktimeend = post.getlist('worktime_end', '')
            company = post.getlist('company', '')
            companyinfo = post.getlist('company_info', '')
            otherinfo = post.get('other_info', '')
            image_url = settings.MEDIA_ROOT +"/images/" + image.name
            with open(image_url, 'wb') as f:
                for data in image.chunks():
                    f.write(data)
            p = PeopleResurne()
            p.ima_url = "images/" + image.name
            p.name = name
            p.age = age
            p.birthday = birthday
            p.identityCard = identitycard
            p.identityNum = identitynum
            p.phone = phone
            p.email = email
            p.other = otherinfo
            p.save()
            for i in range(len(school)):
                education = Education()
                education.people_id = p.id
                education.school = school[i]
                education.educationTitle = educationinfo[i]
                education.save()
            for i in range(len(worktimestart)):
                work = Work()
                work.people_id = p.id
                work.workTimeStart = worktimestart[i]
                work.workTimeEnd = worktimeend[i]
                work.workUnit = company[i]
                work.workTitle = companyinfo[i]
                work.save()
            transaction.savepoint_commit(sid)
            return redirect('/list_page_1/')
    except Exception as res:
        transaction.savepoint_rollback(sid)
        return HttpResponse('错误')


def list_page(request, pindex):
    plist = PeopleResurne.objects.all()
    print(plist)
    paginator = Paginator(plist, 5)
    page = paginator.page(pindex)
    content = {'p': plist, 'title': '列表页', 'page': page, 'paginator': paginator}
    return render(request, 'list.html', content)


def show_information(request, uid):
    p = PeopleResurne.objects.filter(id=uid)[0]
    print(p)
    return render(request, 'show.html', {'title': '展示页', 'p': p})


def edit_info(request, uid):
    p = PeopleResurne.objects.filter(id=uid)[0]
    print(p)
    return render(request, 'editpage.html', {'title': '修改', 'p': p})


@transaction.atomic
def save_info(request, pid):
    try:
        if request.method == 'POST':
            sid = transaction.savepoint()
            post = request.POST
            name = post.get('name', '')
            image = request.FILES.get('image', '')
            age = post.get('age', '')
            birthday = post.get('birthday', '')
            identitycard = post.get('identity_card', '')
            identitynum = post.get('identity_num', '')
            phone = post.get('phone', '')
            email = post.get('email', '')
            school = post.getlist('school', '')
            educationinfo = post.getlist('education_inof', '')
            worktimestart = post.getlist('worktime_start', '')
            worktimeend = post.getlist('worktime_end', '')
            company = post.getlist('company', '')
            companyinfo = post.getlist('company_info', '')
            otherinfo = post.get('other_info', '')
            image_url = settings.MEDIA_ROOT +"/images/" + image.name
            with open(image_url, 'wb') as f:
                for data in image.chunks():
                    f.write(data)

            p = PeopleResurne.objects.filter(id=pid)[0]
            p.ima_url = "images/" + image.name
            p.name = name
            p.age = age
            p.birthday = birthday
            p.identityCard = identitycard
            p.identityNum = identitynum
            p.phone = phone
            p.email = email
            p.other = otherinfo
            p.save()
            for item in p.education_set.all():
                item.delete()
            for item in p.work_set.all():
                item.delete()
            print('*'*20)
            print(school)
            print(len(school))
            for i in range(len(school)):
                education = Education()
                education.people_id = p.id
                education.school = school[i]
                education.educationTitle = educationinfo[i]
                education.save()
            for i in range(len(worktimestart)):
                work = Work()
                work.people_id = p.id
                work.workTimeStart = worktimestart[i]
                work.workTimeEnd = worktimeend[i]
                work.workUnit = company[i]
                work.workTitle = companyinfo[i]
                work.save()
            transaction.savepoint_commit(sid)
            return redirect('/list_page_1/')
    except Exception as res:
        print(res)
        transaction.savepoint_rollback(sid)
        return HttpResponse('错误')
