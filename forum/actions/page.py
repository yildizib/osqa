#!/usr/bin/env python
# -*- coding: utf8 -*- 

from django.utils.translation import ugettext as _
from forum.models.action import ActionProxy
from forum.models import Page

class NewPageAction(ActionProxy):
    verb = _("created")

    def process_data(self, **data):
        title = data.pop('title')
        body = data.pop('content')

        page = Page(author=self.user, title=title, body=body, extra=data)
        page.save()
        self.node = page

    def describe(self, viewer=None):
        if viewer==self.user:
            s =u"%(user)s, %(page)s ba�l�kl� yeni bir sayfa olu�turdunuz"
        else:
            s =u"%(user)s kullan�c�s�, %(page)s ba�l�kl� yeni bir sayfa olu�turdu"     
        return s % {         
        'user': self.hyperlink(self.user.get_profile_url(), self.friendly_username(viewer, self.user)),
        'page': self.hyperlink(self.node.get_absolute_url(), self.node.title)
        }

class EditPageAction(ActionProxy):
    verb = _("edited")

    def process_data(self, **data):
        title = data.pop('title')
        body = data.pop('content')

        if (title != self.node.title) or (body != self.node.body):
            self.node.create_revision(self.user, title=title, body=body)

        self.node.extra = data
        self.node.save()

    def describe(self, viewer=None):
        if viewer==self.user:
            s =u"%(user)s, %(page)s ba�l�kl� sayfay� g�ncellediniz"
        else:
            s =u"%(user)s kullan�c�s�, %(page)s ba�l�kl� sayfay� g�ncelledi"     
        return s % {         
        'user': self.hyperlink(self.user.get_profile_url(), self.friendly_username(viewer, self.user)),
        'page': self.hyperlink(self.node.get_absolute_url(), self.node.title)
        }

class PublishAction(ActionProxy):
    verb = _("published")

    def process_action(self):
        self.node.marked = True
        self.node.nstate.published = self
        self.node.save()

    def cancel_action(self):
        self.node.marked = False
        self.node.nstate.published = None
        self.node.save()

    def describe(self, viewer=None):
        if viewer==self.user:
            s =u"%(user)s, %(page)s ba�l�kl� yeni bir sayfa yay�mlad�n�z"
        else:
            s =u"%(user)s kullan�c�s�, %(page)s ba�l�kl� yeni bir sayfa yay�mlad�"     
        return s % {          
        'user': self.hyperlink(self.user.get_profile_url(), self.friendly_username(viewer, self.user)),
        'page': self.hyperlink(self.node.get_absolute_url(), self.node.title)
        }
