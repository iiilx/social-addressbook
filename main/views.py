from urllib import urlencode

from django.views.generic.simple import direct_to_template
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect

import settings
from addressbook.models import *

request_variables = {
    'client_id': settings.FACEBOOK_APP_ID,
    'redirect_uri': 'http://%s/accounts/facebook_login/done/' % settings.DOMAIN,
}
# /accounts/facebook_login/done/
urlencoded_request_variables = urlencode(request_variables)
FB_LOGIN_URL = "https://graph.facebook.com/oauth/authorize?%s" % urlencoded_request_variables

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('addressbook_index'))
    else:
        return direct_to_template(request, 'base.html', {'FB_LOGIN_URL':FB_LOGIN_URL})

