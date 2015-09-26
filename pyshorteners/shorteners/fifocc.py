# encoding: utf-8
"""
fifo.cc shortener implementation
No config params needed
"""
from .base import BaseShortener
from ..exceptions import ShorteningErrorException


class FifoccShortener(BaseShortener):
    api_url = 'http://api.fifo.cc/'

    def short(self, url):
        params = {
            'url': url,
        }
        response = self._get(self.api_url, params=params)
        if response.ok:
            try:
                data = response.json()
            except ValueError:
                raise ShorteningErrorException('There was an error shortening'
                                               ' this url - {0}'.format(
                                                   response.content))
            return data['short_url']
        raise ShorteningErrorException('There was an error shortening this '
                                       'url - {0}'.format(response.content))
