import os

def populate():
    for i in range(1,13):
        import random
        x=random.randint(10,1000)
        x=x*100
        y=random.randint(1,6)
        z="upload/"
        z=z+ str(i) + ".jpeg"
        a = add_apparel(price=x, merchant_id=y, image=z)


def add_apparel(price,merchant_id,image):
    c = Apparel.objects.get_or_create(price=price, merchant_id=merchant_id, image=image)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Apparel population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dressy.settings')
    from home.models import Apparel
    populate()
