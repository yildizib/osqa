from base import *
from django.utils.translation import ugettext as _

class Answer(Node):
    friendly_name = _("answer")
    friendly_name_i_hali            = _(u"cevab�")
    friendly_name_e_hali            = _(u"cevaba")
    friendly_name_de_hali           = _(u"cevapta")
    friendly_name_den_hali          = _(u"cevaptan")
    friendly_name_adindaki_hali     = _(u"cevab�")
    friendly_name_adindaki_i_hali   = _(u"cevab�n�")
    friendly_name_adindaki_e_hali   = _(u"cevab�na")
    friendly_name_adindaki_de_hali  = _(u"cevab�nda")
    friendly_name_adindaki_den_hali = _(u"cevab�ndan")    


    class Meta(Node.Meta):
        proxy = True

    @property
    def accepted(self):
        return self.nis.accepted

    @property
    def headline(self):
        return self.question.headline

    def get_absolute_url(self):
        return '%s/%s' % (self.question.get_absolute_url(), self.id)


class AnswerRevision(NodeRevision):
    class Meta:
        proxy = True