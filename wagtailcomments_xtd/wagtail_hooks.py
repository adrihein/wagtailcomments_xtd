try:
    # urlresolvers removed in Django 2.0:
    from django.core.urlresolvers import reverse
except ImportError:
    # For Django 2.0+
    from django.urls import reverse 
from wagtailcomments_xtd import urls
from wagtail.wagtailcore import hooks
from django.conf.urls import include, url
from wagtail.wagtailadmin.menu import MenuItem
from django.utils.translation import ugettext_lazy as _


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^comments/', include(urls)),
    ]


@hooks.register('register_admin_menu_item')
def register_styleguide_menu_item():
    return MenuItem(
        _('Comments'),
        reverse('wagtailcomments_xtd_pages'),
        classnames='icon icon-fa-comments-o',
        order=1000
    )
