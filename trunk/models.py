from django.db import models
from django.contrib.auth.models import User

class SkillHeading(models.Model):
    name = models.CharField(maxlength=100)
    slug = models.SlugField(prepopulate_from=('name',))
    description = models.TextField(blank=True)
    profile = models.ManyToManyField('ResumeProfile', blank=True)

    def __str__(self):
        return self.name

    def get_skills(self):
        if self.profile:
            return self.skill_set.filter(profile__name = self.profile)
        else:
            return self.skill_set.all()

    class Admin:
        pass

class Skill(models.Model):
    name = models.CharField(maxlength=100)
    slug = models.SlugField(prepopulate_from=('name',))
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)
    skill_heading = models.ForeignKey(SkillHeading)
    projects = models.ManyToManyField('Project', null=True, blank=True)
    experience = models.CharField(maxlength=200)
    profile = models.ManyToManyField('ResumeProfile', blank=True)
    
    added = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.skill_heading.name + ": " + self.name
    
    def save(self):
        if not self.added:
            self.added = datetime.datetime.now()
        self.updated = datetime.datetime.now()
        
        super(Skill, self).save()

    class Admin:
        pass

class Project(models.Model):
    name = models.CharField(maxlength=100)
    slug = models.SlugField(prepopulate_from=('name',))
    link = models.URLField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    profile = models.ManyToManyField('ResumeProfile', blank=True)
    
    added = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self):
        if not self.added:
            self.added = datetime.datetime.now()
        self.updated = datetime.datetime.now()

        super(Skill, self).save()

    class Admin:
        pass

class WorkExperience(models.Model):
    name = models.CharField(maxlength=100)
    slug = models.SlugField(prepopulate_from=('name',))
    title = models.CharField(maxlength=100)
    company_link = models.URLField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    description = models.TextField(blank=True)
    location = models.ForeignKey('ContactInfo')
    profile = models.ManyToManyField('ResumeProfile', blank=True)
    
    added = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    
    def get_responsibilities(self):
        if self.profile:
            return self.responsibility_set.filter(profile__name = self.profile)
        else:
            return self.responsibility_set.all()

    def __str__(self):
        return self.name

    def save(self):
        if not self.added:
            self.added = datetime.datetime.now()
        self.updated = datetime.datetime.now()

        super(Skill, self).save()

    class Admin:
        pass

class Responsibility(models.Model):
    description = models.TextField()
    work_experience = models.ForeignKey(WorkExperience)
    order = models.IntegerField(blank=True, null=True)
    profile = models.ManyToManyField('ResumeProfile', blank=True)
    
    added = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.work_experience.name + ": " + self.description[:50] + "..."

    def save(self):
        if not self.added:
            self.added = datetime.datetime.now()
        self.updated = datetime.datetime.now()

        super(Skill, self).save()

    class Admin:
        pass

class Education(models.Model):
    name = models.CharField(maxlength=100)
    slug = models.SlugField(prepopulate_from=('name',))
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)
    degree = models.CharField(maxlength=200, blank=True)
    minor = models.CharField(maxlength=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    location = models.ForeignKey('ContactInfo')
    profile = models.ManyToManyField('ResumeProfile', blank=True)
    
    added = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.name
        
    def save(self):
        if not self.added:
            self.added = datetime.datetime.now()
        self.updated = datetime.datetime.now()

        super(Skill, self).save()

    class Admin:
        pass

class CourseWork(models.Model):
    name = models.CharField(maxlength=100)
    slug = models.SlugField(prepopulate_from=('name',))
    description = models.TextField(blank=True)
    education = models.ForeignKey(Education)
    profile = models.ManyToManyField('ResumeProfile', blank=True)
        
    added = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.name

    def save(self):
        if not self.added:
            self.added = datetime.datetime.now()
        self.updated = datetime.datetime.now()

        super(Skill, self).save()

    class Admin:
        pass

class ContactInfo(models.Model):
    street = models.CharField(maxlength=30, blank=True)
    city = models.CharField(maxlength=30, blank=True)
    province = models.CharField(maxlength=30, blank=True)
    zipcode = models.IntegerField(maxlength=5, blank=True, null=True)
    country = models.CharField(maxlength=30, blank=True)
    phone = models.CharField(maxlength=30, blank=True)
    profile = models.ManyToManyField('ResumeProfile', blank=True)

    def __str__(self):
        return self.city
    
    class Admin:
        pass

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    address = models.ForeignKey(ContactInfo)
    current_activities = models.TextField()
    bio = models.TextField(blank=True)
    profile = models.ManyToManyField('ResumeProfile', blank=True)

    def __str__(self):
        return "profile: " + self.user.username

    class Admin:
        pass

class ResumeProfile(models.Model):
    name = models.CharField(maxlength=200)

    def __str__(self):
        return "resume: " + self.name

    class Admin:
        pass
