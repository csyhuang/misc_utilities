import re
import urllib.request


class ImageURLExtractor(object):
    def __init__(self, url, prefix, suffix):
        self._url = url
        self._prefix = prefix
        self._suffix = suffix
        self._htmlstr = None
        self._list_of_image_urls = None

    def _return_html(self):
        fp = urllib.request.urlopen(self._url)
        mybytes = fp.read()
        self._htmlstr = mybytes.decode("utf8")
        fp.close()
        return self._htmlstr

    def _get_list_of_image_urls(self):
        ans = re.findall(r'{prefix}.*?\{suffix}'.format(prefix=self._prefix, suffix=self._suffix), self.htmlstr)
        self._list_of_image_urls = list(set(ans))
        print("Number of image urls: {}".format(len(self._list_of_image_urls)))

    @property
    def htmlstr(self):
        if self._htmlstr is None:
            self._htmlstr = self._return_html()
        return self._htmlstr

    @property
    def list_of_image_urls(self):
        if self._list_of_image_urls is None:
            self._get_list_of_image_urls()
        return self._list_of_image_urls

    @staticmethod
    def filter_out_str_that_contains_substrings(list_of_image_urls, exclude_substrings):
        return [x for x in list_of_image_urls if not any([y in x for y in exclude_substrings])]

