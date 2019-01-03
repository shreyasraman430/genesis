from django.conf.urls import include, url
from . import views
import django.contrib.auth.views

urlpatterns = [
    url(r'^pubg$', views.pubgRegistration, name='pubgRegistration'),
    url(r'^pubg/$', views.pubgRegistration, name='pubgRegistration'),
    url(r'^pisRound2$', views.pisRound2Registration, name='pisRound2Registration'),
    url(r'^pisRound2/$', views.pisRound2Registration, name='pisRound2Registration'),
    url(r'^vignettoraregistered$', views.vignettoraregisteredRegistration, name='vignettoraregisteredRegistration'),
    url(r'^vignettoraregistered/$', views.vignettoraregisteredRegistration, name='vignettoraregisteredRegistration'),
    url(r'^etcregistered$', views.etcregisteredRegistration, name='etcregisteredRegistration'),
    url(r'^etcregistered/$', views.etcregisteredRegistration, name='etcregisteredRegistration'),
    url(r'^ibmhackathon$', views.ibmhackathonRegistration, name='ibmhackathonRegistration'),
    url(r'^ibmhackathon/$', views.ibmhackathonRegistration, name='ibmhackathonRegistration'),
    url(r'^interschool$', views.iscRegistration, name='iscRegistration'),
    url(r'^interschool/$', views.iscRegistration, name='iscRegistration'),
	url(r'^closed$', views.closed, name='closed'),
	url(r'^closed/$', views.closed, name='closed'),
	url(r'^registered$', views.registered, name='registered'),
	url(r'^registered/$', views.registered, name='registered'),
	url(r'^campusambassadors$', views.campusambassadors, name='campusambassadors'),
	url(r'^campusambassadors/$', views.campusambassadors, name='campusambassadors'),
	url(r'^lasya$', views.lasyaRegistrationRedirect, name='lasyaRegistration'),
	url(r'^lasya/$', views.lasyaRegistrationRedirect, name='lasyaRegistration'),
	url(r'^lasyasolo$', views.lasyaSoloRegistration, name='lasyaSoloRegistration'),
	url(r'^lasyasolo/$', views.lasyaSoloRegistration, name='lasyaSoloRegistration'),
	url(r'^lasyagroup$', views.lasyaGroupRegistration, name='lasyaGroupRegistration'),
	url(r'^lasyagroup/$', views.lasyaGroupRegistration, name='lasyaGroupRegistration'),
	url(r'^proscenium$', views.prosceniumRegistration, name='prosceniumRegistration'),
	url(r'^proscenium/$', views.prosceniumRegistration, name='prosceniumRegistration'),
	url(r'^footprints$', views.footprintsRegistration, name='footprintsRegistration'),
	url(r'^footprints/$', views.footprintsRegistration, name='footprintsRegistration'),
	url(r'^decoherence$', views.decoherenceRegistration, name='decoherenceRegistration'),
	url(r'^decoherence/$', views.decoherenceRegistration, name='decoherenceRegistration'),
	url(r'^battleofbands$', views.battleofbandsRegistration, name='battleofbandsRegistration'),
	url(r'^battleofbands/$', views.battleofbandsRegistration, name='battleofbandsRegistration'),
	url(r'^vignettora$', views.vignettoraRegistration, name='vignettoraRegistration'),
	url(r'^vignettora/$', views.vignettoraRegistration, name='vignettoraRegistration'),
	url(r'^explain_the_concept$', views.etcRegistration, name='etcRegistration'),
	url(r'^explain_the_concept/$', views.etcRegistration, name='etcRegistration'),
    url(r'^chemisticon$', views.chemisticonRegistration, name='chemisticonRegistration'),
	url(r'^chemisticon/$',views.chemisticonRegistration, name='chemisticonRegistration'),
	url(r'^sciencejournalism/$',views.sciencejournalismRegistration, name='sciencejournalismRegistration'),
	url(r'^sciencejournalism$',views.sciencejournalismRegistration, name='sciencejournalismRegistration'),
    url(r'^sciencejournalism/submission/$', views.sciencejournalismsubmission , name="sciencejournalismsubmission"),
	url(r'^sciencejournalism/submission$', views.sciencejournalismsubmission , name="sciencejournalismsubmission"),
    url(r'^debubulary$', views.debubularyRegistration, name='debubularyRegistration'),
	url(r'^debubulary/$', views.debubularyRegistration, name='debubularyRegistration'),
	url(r'^cryptothlon$', views.cryptothlonRegistration, name='cryptothlonRegistration'),
	url(r'^cryptothlon/$', views.cryptothlonRegistration, name='cryptothlonRegistration'),
	url(r'^time$', views.time, name='time'),
	url(r'^time/$', views.time, name='time'),
	url(r'^servertime$', views.getServerTime, name='servertime'),
	url(r'^servertime/$', views.getServerTime, name='servertime'),
	url(r'^wikimediaphotography$', views.wikimediaphotographyRegistration, name='wikimediaphotographyRegistration'),
	url(r'^wikimediaphotography/$', views.wikimediaphotographyRegistration, name='wikimediaphotographyRegistration'),
	url(r'^pravega_innovation_summit$', views.pisRegistration, name='pisRegistration'),
	url(r'^pravega_innovation_summit/$', views.pisRegistration, name='pisRegistration'),
	url(r'^signup$', views.signup, name='signup'),	url(r'^signup$', views.signup, name='signup'),
	url(r'^signup/$', views.signup, name='signup'),	url(r'^signup$', views.signup, name='signup'),
	url(r'^activate/account/$', views.activateAccount),
	url(r'^$', views.registration_index, name="registration"),
	url('^password_reset/$', django.contrib.auth.views.PasswordResetView.as_view(
		email_template_name='registration/email_templates/password_reset.txt',
		html_email_template_name='registration/email_templates/reset_password_email.html',
		subject_template_name='registration/email_templates/password_reset_subject.txt'
	),name='password_reset'),
	url(r'^', include('django.contrib.auth.urls')),
	url(r'^decoherence/prelims$', views.decoherencePrelims, name='decoherencePrelims'),
	url(r'^decoherence/prelims/$', views.decoherencePrelims, name='decoherencePrelims'),
	#url(r'^time$', views.time, name='time'),
	#url(r'^time/$', views.time, name='time'),
	url(r'^servertime$', views.getServerTime, name='servertime'),
	url(r'^servertime/$', views.getServerTime, name='servertime'),
]
