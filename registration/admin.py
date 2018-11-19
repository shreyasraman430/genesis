from django.contrib import admin
from .models import *
from . import adminResources
from import_export.admin import ExportMixin
from django.utils.html import format_html
from django.conf import settings



class UserDataResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','institution','city',)
    list_filter = ('email_validated','city',)
    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    class Meta:
        model = UserData

class AdminEventResource(ExportMixin,admin.ModelAdmin):
    fields = ('title','displayTitle','registrationStatus','description','priority','registrationLink')    #for showing the fields in this order
    list_display = ('title','registrationStatus')
    list_filter = ('registrationStatus',)
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_staff:
            if request.user.is_superuser:
                return []
            else:
                return ['title','registrationLink']
    class Meta:
        model = AdminEvent


class CampusAmbassadorResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','institution','city','submit_date',)
    list_filter = ('submit_date','city',)
    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj,)
    class Meta:
        model = CampusAmbassador



class LasyaRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','category','teamName','teamLeader','email','institution','city','submit_date','seeVideoFile','seeVideoLink',)
    list_filter = ('submit_date','city',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj,)
    def seeVideoFile(self, obj):                        #shows uploaded video link in the list of model instances`
        return adminResources.seeVideoFile(self, obj)
    def seeVideoLink(self, obj):                         #shows external video link in the list of model instances
        return adminResources.seeVideoLink(self, obj)

    class Meta:
        model = LasyaRegistration

class ProsceniumRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','teamName','teamLeader','email','institution','city','submit_date','seeVideoFile','seeVideoLink')
    list_filter = ('submit_date','city',)
    readonly_fields = ('videoFile','videoFileLink',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    def seeVideoFile(self, obj):                        #shows uploaded video link in the list of model instances`
        return adminResources.seeVideoFile(self, obj)
    def seeVideoLink(self, obj):                         #shows external video link in the list of model instances
        return adminResources.seeVideoLink(self, obj)

    class Meta:
        model = ProsceniumRegistration


class BattleOfBandsRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','teamName','teamLeader','email','institution','city','regionalfinalscity','submit_date','seeAudioVideoFile','seeAudioVideoLink')
    list_filter = ('submit_date','regionalfinalscity',)
    readonly_fields = ('audioVideoFile','audioVideoFileLink',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    def seeAudioVideoFile(self, obj):                        #shows uploaded video link in the list of model instances`
        return adminResources.seeAudioVideoFile(self, obj)
    def seeAudioVideoLink(self, obj):                         #shows external video link in the list of model instances
        return adminResources.seeAudioVideoLink(self, obj)

    class Meta:
        model = BattleOfBandsRegistration


class FootprintsRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','teamName','teamLeader','email','institution','city','submit_date')
    list_filter = ('submit_date','city',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)

    class Meta:
        model = FootprintsRegistration


class DecoherenceRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('teamName','institution','city','submit_date')
    list_filter = ('submit_date','city',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)

    class Meta:
        model = DecoherenceRegistration


class WikimediaPhotographyRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','wikimediaUsername','institution','city','submit_date')
    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    class Meta:
        model = WikimediaPhotographyRegistration

class VignettoraRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user', 'email','institution','city','submit_date')
    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    class Meta:
        model = VignettoraRegistration

class PPPRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user', 'email','institution','city','submit_date')
    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    class Meta:
        model = PPPRegistration

class ImpromptooRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user', 'email','institution','city','submit_date')
    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    class Meta:
        model = ImpromptooRegistration

class PISRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','teamName','institution','city','submit_date')
    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    class Meta:
        model = PISRegistration

admin.site.register(UserData,UserDataResource)
admin.site.register(AdminEvent,AdminEventResource)
admin.site.register(CampusAmbassador,CampusAmbassadorResource)
admin.site.register(LasyaRegistration,LasyaRegistrationResource)
admin.site.register(ProsceniumRegistration,ProsceniumRegistrationResource)
admin.site.register(BattleOfBandsRegistration,BattleOfBandsRegistrationResource)
admin.site.register(FootprintsRegistration,FootprintsRegistrationResource)
admin.site.register(DecoherenceRegistration,DecoherenceRegistrationResource)
admin.site.register(WikimediaPhotographyRegistration,WikimediaPhotographyRegistrationResource)
admin.site.register(PPPRegistration,PPPRegistrationResource)
admin.site.register(VignettoraRegistration,VignettoraRegistrationResource)
admin.site.register(PISRegistration,PISRegistrationResource)
admin.site.register(ImpromptooRegistration,ImpromptooRegistrationResource)
