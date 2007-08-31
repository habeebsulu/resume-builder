from django.contrib.auth.models import User
from django.template import Context, Template, loader
from django.conf import settings
from models import Education, WorkExperience, SkillHeading, UserProfile, Project

import os
import sys
import commands
import resume_settings

                
def build_pdf(profile=None, file_name=None, debug=False):
    tex_dir = os.path.abspath('./latex/')
    output_dir = settings.MEDIA_ROOT + '/resume/pdf'
    
    if not file_name:
        file_name = 'resume.tex'

    if profile:
        project_list = Project.objects.filter(profile__name = profile).order_by('-start_date')
        education_list = Education.objects.filter(profile__name = profile).order_by('-start_date')
        experience_list = WorkExperience.objects.filter(profile__name = profile).order_by('-start_date')
        skillheading_list = SkillHeading.objects.filter(profile__name = profile).order_by('name')
    else:   
        project_list = Project.objects.order_by('-start_date')
        education_list = Education.objects.order_by('-start_date')
        experience_list = WorkExperience.objects.order_by('-start_date')
        skillheading_list = SkillHeading.objects.order_by('name')
        
    user = User.objects.get(username=resume_settings.ResumeUser)

    latex_context = Context({'project_list': project_list,
               'education_list': education_list,
               'experience_list': experience_list,
               'skillheading_list': skillheading_list,
               'user': user,
               'user_profile': user.get_profile(),
               'profile': profile,
               })

    latex_template = loader.get_template('resume/latex/resume.tex')
    resume_tex = latex_template.render(latex_context)
    
    tex_file = tex_dir + file_name
    latex_output = open(tex_file, 'w')
    latex_output.write(resume_tex)
    latex_output.close()
    
    command = "pdflatex -output-directory %s %s" % (output_dir, tex_file,)
    if debug:
        status = os.system(command)
    else:
        status = commands.getstatusoutput(command)
