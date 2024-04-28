
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index , name='index'),
    path('accordion/',views.accordion, name='accordion'),
    path('breadcrumb/',views.breadcrumb, name='breadcrumb'),
    path('cards/',views.cards, name='cards'),
    path('carousel/',views.carousel, name='carousel'),
    path('collapse/',views.collapse, name='collapse'),
    path('list-grpup/',views.list_group, name='listGrpup'),
    path('navs-tabs/',views.navs_tabs, name='nav_tabs'),
    path('pagination/',views.pagination,name='pagination'),
    path('placeholders/',views.placeholders, name='placeholders'),
    path('popovers/',views.popovers, name='popovers'),
    path('progress/',views.progress, name='progress'),
    path('spinners/',views.spinners, name='spinners'),
    path('tables/',views.tables, name='tables'),
    path('tooltips/',views.tooltips,name='tooltips'),
    path('charts/',views.charts, name='charts'),
    path('widgets/',views.widgets, name='widgets'),
    path('colors/',views.colors, name='colors'),
    path('typography/',views.typography, name='typography'),
    path('checks-radios/',views.checks_radios, name='checks_radios'),
    path('floating-labels/',views.floating_labels, name='floating_labels'),
    path('form-control/',views.form_control,name="form_control"),
    path('input-group/',views.input_group, name='input_group'),
    path('layout/',views.layout, name='layout'),
    path('range/',views.range, name='range'),
    path('select/',views.select, name='select'),
    path('validation/',views.validation, name='validation'),
    path('button-group/',views.button_group, name='button_group'),
    path('buttons/',views.buttons, name='buttons'),
    path('dropdowns/',views.dropdowns, name='dropdowns'),
    path('coreui-icons-brand/',views.coreui_icons_brand, name='coreui_icons_brand'),
    path('coreui-icons-flag/',views.coreui_icons_flag, name='coreui_icons_flag'),
    path('coreui-icons-free/',views.coreui_icons_free, name='coreui_icons_free'),
    path('alerts/', views.alerts, name='alerts'),
    path('badge/', views.badge, name='badge'),
    path('modals/', views.modals, name='modals'),
    path('toasts/', views.toasts, name='toasts'),

    # Authentication
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/register/', views.UserRegistrationView.as_view(), name='register'),

    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password-change-done.html'
    ), name="password_change_done"),

    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/',
        views.UserPasswrodResetConfirmView.as_view(), name="password_reset_confirm"
    ),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password-reset-done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password-reset-complete.html'
    ), name='password_reset_complete'),
    
    path('logout/', views.logout_view, name='logout'),
]
