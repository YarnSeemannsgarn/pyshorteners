# encoding: utf-8
"""
bn.gy shortener implementation
No config params needed
"""
from .base import BaseShortener
from ..exceptions import ShorteningErrorException
import xml.etree.ElementTree as ET

class BngyShortener(BaseShortener):
    api_url = 'http://bn.gy/API.asmx/CreateUrl'

    def short(self, url):
        params = {
            'real_url': url,
        }
        response = self._get(self.api_url, params=params)
        if response.ok:
            try:
                data = ET.fromstring(response.text)
            except ValueError:
                raise ShorteningErrorException('There was an error shortening'
                                               ' this url - {0}'.format(
                                                   response.content))
            return data[1].text
        raise ShorteningErrorException('There was an error shortening this '
                                       'url - {0}'.format(response.content))
