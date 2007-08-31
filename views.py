from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponsePermanentRedirect
from models import CourseWork, Education, WorkExperience, Project, Responsibility, SkillHeading, Skill, UserProfile
from django.contrib.auth.models import User
from django.template import RequestContext
from django.conf import settings

import resume_settings
import datetime

from build_pdf import build_pdf

def render_with_request(request, template, context):
    return render_to_response(template, context, context_instance=RequestContext(request))

def resume(request):
    education_list = Education.objects.all()
    experience_list = WorkExperience.objects.order_by('-start_date')
    skillheading_list = SkillHeading.objects.all()
    user = User.objects.get(username=resume_settings.RESUME_USER)

    context = {'education_list': education_list,
               'experience_list': experience_list,
               'skillheading_list': skillheading_list,
               'user': user,
               'user_profile': user.get_profile(),
               }
    return render_with_request(request, 'resume/resume.html', context)

def projects(request):
    project_list = Project.objects.all()
    user = User.objects.get(username=resume_settings.RESUME_USER)
    
    context = {'project_list': project_list,
               'user': user,
               'user_profile': user.get_profile(),
               }
    return render_with_request(request, 'resume/projects/index.html', context)

def project_details(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    user = User.objects.get(username=resume_settings.RESUME_USER)
    
    context = {'project': project,
               'user': user,
               'user_profile': user.get_profile(),
               }
    return render_with_request(request, 'resume/projects/project.html', context)

def render_pdf(request, profile=None):
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = 'resume'
    pdf_file = file_name + '.pdf'
    tex_file = file_name + '.tex'
    pdf_url = '%s/resume/pdf/latex%s' % (settings.MEDIA_URL, pdf_file,)
    build_pdf(file_name=tex_file, profile=profile, debug=True)
    return HttpResponseRedirect(pdf_url)
