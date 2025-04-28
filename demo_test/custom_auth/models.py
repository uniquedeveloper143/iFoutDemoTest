import uuid
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from demo_test.custom_auth.managers import ApplicationUserManager

class ApplicationUser(
    AbstractBaseUser,
    PermissionsMixin,
):

    username_validator = UnicodeUsernameValidator()
    uuid = models.UUIDField(
        verbose_name=_('uuid'),
        unique=True,
        help_text=_('Required. A 32 hexadecimal digits number as specified in RFC 4122.'),
        error_messages={
            'unique': _('A user with that uuid already exists.'),
        },
        default=uuid.uuid4,
    )
    username = models.CharField(
        verbose_name=_('username'),
        max_length=150,
        unique=True,
        blank=True,
        null=True,
        help_text=_('Required. A 32 hexadecimal digits number as specified in RFC 4122.'),
        error_messages={
            'unique': _('A user with that username already exists.'),
        },
    )
    email = models.EmailField(_('email address'),null=True,blank=True,unique=True,
                              error_messages={
                                  'unique': _('A user with that email already exists.'),
                              },
                              )
    is_email_verified = models.BooleanField('email verified', default=True)
    first_name = models.CharField(_('first name'), max_length=150,blank=True)
    last_name = models.CharField(_('last name'), max_length=150,blank=True)
    full_name = models.CharField(_('full name'), max_length=150,blank=True,
                                 help_text=_('Full name as it was returned by social provider'))
    about = models.TextField(_('about me'),max_length=1000, blank=True)
    is_active = models.BooleanField(_('active'), default=True, help_text=_(
        'Designates whether the user can log into this admin site.'
        ),
                                   )
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_(
        'Designates whether this user should be treated as active. '
        'Unselect theis instead of deleting accounts.'),
                                   )
    is_delete = models.BooleanField(_('delete'), default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    last_modified = models.DateTimeField(_('last modified'),auto_now=True)
    last_user_activity = models.DateTimeField(_('last activity'), default=timezone.now)
    date_of_birth = models.DateField(_('data of birth'), null=True, blank=True)

    objects = ApplicationUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username or self.full_name or self.email or self.first_name or str(self.uuid)

    def save(self, *args, **kwargs):

        if self.email:
            self.email = self.__class__.objects.normalize_email(self.email)

        if not self.username:
            new_username = self.email.split('@')[0] if self.email else ''

            if self._meta.model._default_manager.filter(username=new_username).exists() or new_username == '':
                postfix = timezone.now().strftime('%Y%m%d%H%M%S')

                while self._meta.model._default_manager.filter(username=new_username + postfix).exists():
                    postfix = timezone.now().strftime('%Y%m%d%H%M%S')

                new_username += postfix
            self.username = new_username

        if not self.full_name.strip():
            if self.first_name and self.last_name:
                self.assign_full_name_to_the_object()
        if self.full_name:
            self.assign_first_last_name_to_the_object()

        return super(ApplicationUser, self).save(*args, **kwargs)

    def assign_full_name_to_the_object(self):
        self.full_name = f'{self.first_name} {self.last_name}'.strip()

    def assign_first_last_name_to_the_object(self):
        fullname = self.full_name.split(' ')
        self.first_name = fullname[0]
        if len(fullname) > 1:
            self.last_name = fullname[1]
        else:
            self.first_name = fullname[0]

    def update_last_activity(self):
        now = timezone.now()

        self.last_user_activity = now
        self.save(update_fields=('last_user_activity', 'last_modified'))


