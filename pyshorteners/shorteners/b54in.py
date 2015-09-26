# encoding: utf-8
"""
b54.in shortener implementation
No config params needed
"""
from .base import BaseShortener
from ..exceptions import ShorteningErrorException


class B54inShortener(BaseShortener):
    api_url = 'http://b54.in/api/'

    def short(self, url):
        params = {
            'action': 'shorturl',
            'format': 'simple',
            'url': url,
        }
        response = self._get(self.api_url, params=params)
        if response.ok:
            return response.text.strip()
        raise ShorteningErrorException('There was an error shortening this '
                                       'url - {0}'.format(response.content))
