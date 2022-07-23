from ecom.models import Product

class EcomAdapter(object):
    def __init__(self):
        pass
    def add_product(self, title, description, image_url):
        print(image_url)
