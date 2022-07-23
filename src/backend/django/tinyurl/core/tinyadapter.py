from tinyurl.models import Tinyurl

from django.db import connection
import redis
import hashlib
import datetime
import redis

rd = redis.Redis(host = '0.0.0.0', port = 6379, db = 0)


class TinyAdapter(object):
    def __init__(self):
        pass
    def generate_domain(self, alias):
        long_url = rd.get(alias)
        if long_url is None:
            res = Tinyurl.objects.filter(alias = alias)
            if not res.exists():
                return None
            print("res :" , res[0].long_url)
            long_url = res[0].long_url
            rd.set(alias, long_url)
        else:
            long_url = long_url.decode()
            print('From Redis', long_url)
        return long_url



    def update_tinydb(self, alias, long_url, domain):
        if alias != '':
            als = self.val_update_tinyurl(alias, long_url, domain)
            if als is None:
                return "alias not available"
            return f"{domain}/{als}"
        short_url = hashlib.shake_256(long_url.encode()).hexdigest(5)
        als = Tinyurl.objects.filter(alias = short_url)
        if als.exists():
            timestamp = datetime.datetime.now().timestamp()
            short_url = short_url + str(int(timestamp))

        self.add_tiny(short_url, long_url, domain)
        print("short: ", short_url)
        return f"{domain}/{short_url}"

    def add_tiny(self, alias, long_url, domain):
        Tinyurl.objects.update_or_create(alias = alias, long_url = long_url, domain = domain)
    def val_update_tinyurl(self, alias, long_url, domain = None):
        url = Tinyurl.objects.filter(alias=alias)
        print(url.exists())
        if not url.exists():
            self.add_tiny(alias, long_url, domain)
            return alias
        if url[0].long_url == long_url:
            return alias

        return None



