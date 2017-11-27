from django.conf.urls import url

from password_policies import views as pp_views

urlpatterns = [
   url(r'^change/done/$',
       pp_views.PasswordChangeDoneView.as_view(),
       name="password_change_done"),
   url(r'^change/$',
       pp_views.PasswordChangeFormView.as_view(),
       name="password_change"),
   url(r'^reset/$',
       pp_views.PasswordResetFormView.as_view(),
       name="password_reset"),
   url(r'^reset/complete/$',
       pp_views.PasswordResetCompleteView.as_view(),
       name="password_reset_complete"),
   url(r'^reset/confirm/([0-9A-Za-z_\-]+)/([0-9A-Za-z]{1,13})/([0-9A-Za-z-=_]{1,32})/$',
       pp_views.PasswordResetConfirmView.as_view(),
       name="password_reset_confirm"),
   url(r'^reset/done/$',
       pp_views.PasswordResetDoneView.as_view(),
       name="password_reset_done"),
]
