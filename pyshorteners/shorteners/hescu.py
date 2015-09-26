# encoding: utf-8
"""
hes.cu shortener implementation
No config params needed
"""
from .base import BaseShortener
from ..exceptions import ShorteningErrorException


class HescuShortener(BaseShortener):
    api_url = 'https://hec.su/api'

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
            return data['short']
        raise ShorteningErrorException('There was an error shortening this '
                                       'url - {0}'.format(response.content))
