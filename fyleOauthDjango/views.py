import json
import os

import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .connectors import fyle

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
BASE_URL = os.environ.get("BASE_URL")
TOKEN_URL = '{0}/api/oauth/token'.format(BASE_URL)


class HomeView(TemplateView):
    def get(self, request):
        return render(request, 'welcome.html')

    def post(self, request):
        return redirect('profile/')


class ProfileView(TemplateView):
    def get(self, request):
        code = request.GET.get('code')
        error = request.GET.get('error')
        if code:
            return self.get_profile_details(self.request)
        elif error == "access_denied":
            return redirect('/login')
        return self.authorize(self.request)

    def authorize(self, request):
        global BASE_URL
        global CLIENT_ID
        redirect_uri = "{0}{1}/profile".format("http://", request.get_host())
        authorize_url = "{0}/app/main/#/oauth/authorize?client_id={1}&redirect_uri={" \
                        "2}&response_type=code&state=ajsfbjak".format(
            BASE_URL, CLIENT_ID, redirect_uri)
        return HttpResponseRedirect(authorize_url)

    def get_profile_details(self, request):
        global CLIENT_SECRET
        global CLIENT_ID
        code = request.GET.get('code')
        error = request.GET.get('error')
        if code and error is None:
            json_response = requests.post(TOKEN_URL, data={"grant_type": "authorization_code",
                                                           "client_id": CLIENT_ID,
                                                           "client_secret": CLIENT_SECRET,
                                                           "code": code})
            data = json.loads(json_response.text)
            refresh_token = data.get("refresh_token")
            fyle_connection = fyle.FyleConnector(refresh_token)
            emp_details = fyle_connection.get_employee_details()
            return render(self.request, 'profile.html', context={'emp_data': emp_details})
        return redirect('/login')
