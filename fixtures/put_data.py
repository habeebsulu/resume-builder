import sys, os

sys.path.append('/Users/aconbere/Projects/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Personal.settings'

from django.core.serializers import serialize
from Personal.resume import models

model_names = ['Project', 'UserProfile', 'Education', 'Experience', 'Responsibility', 'Skill', 'SkillHeading']

for model_name in model_names:
    cls = getattr(models, model_name)
    if not cls:
        print "Could not find " + model_name

    filename = model_name.lower() + ".json"
    file = open(filename, "w")
    file.write(serialize("json", cls.objects.all()))

