import os
from datetime import datetime

def populate():
    for i in range(1,13):
        import random
        apparel_id=i
        merchant_id=random.randint(1,6)
        if(i==1 or i==2 or i==3 or i==4):
            device="laptop"
            os="Linux"
            browser="Chrome"
            country="India"
        if(i==5 or i==6 or i==7 or i==8):
            device="mobile"
            os="Windows"
            browser="Firefox"
            country="China"
        if(i==9 or i==10 or i==11 or i==12):
            device="laptop"
            os="MAC"
            browser="Safari"
            country="Dubai"
        IP="117.220.181.81"
        user_id=i
        date=datetime(2014, random.randint(1, 12), random.randint(1, 30), random.randint(1, 12), 44, 56, 350892)
        a = add_apparel(apparel_id,merchant_id,device,browser,os,date,IP,country,user_id)
    for i in range(1,13):
        import random
        apparel_id=i
        merchant_id=random.randint(1,6)
        if(i==1 or i==2 or i==3 or i==4):
            device="laptop"
            os="Linux"
            browser="Chrome"
        if(i==5 or i==6 or i==7 or i==8):
            device="mobile"
            os="Windows"
            browser="Firefox"
        if(i==9 or i==10 or i==11 or i==12):
            device="laptop"
            os="MAC"
            browser="Safari"
        IP="117.220.181.81"
        country="india"
        user_shared_id=i
        user_followed_id=i-1
        followed_on=random.randint(1,2)
        date=datetime(2014, random.randint(1, 12), random.randint(1, 30), random.randint(1, 12), 44, 56, 350892)
        a = add_follow(apparel_id,merchant_id,device,browser,os,date,IP,country,user_shared_id,user_followed_id,followed_on)
    for i in range(1,13):
        import random
        apparel_id=i
        merchant_id=random.randint(1,6)
        if(i==1 or i==2 or i==3 or i==4):
            device="laptop"
            os="Linux"
            browser="Chrome"
            country="America"
        if(i==5 or i==6 or i==7 or i==8):
            device="mobile"
            os="Windows"
            browser="Firefox"
            country="China"
        if(i==9 or i==10 or i==11 or i==12):
            device="laptop"
            os="MAC"
            browser="Canada"
        IP="117.220.181.81"
        user_id=i
        shared_on=random.randint(1,2)
        date=datetime(2014, random.randint(1, 12), random.randint(1, 30), random.randint(1, 12), 44, 56, 350892)
        a = add_share(apparel_id,merchant_id,device,browser,os,date,IP,country,user_id,shared_on)


def add_apparel(apparel_id,merchant_id,device,browser,os,date,IP,country,user_id):
    c = ApparelTry.objects.get_or_create(apparel_id=apparel_id,merchant_id=merchant_id,device=device,browser=browser,os=os,date=date,IP=IP,country=country,user_id=user_id)[0]
    return c

def add_follow(apparel_id,merchant_id,device,browser,os,date,IP,country,user_shared_id,user_followed_id,followed_on):
    c = ApparelFollow.objects.get_or_create(apparel_id=apparel_id,merchant_id=merchant_id,device=device,browser=browser,os=os,date=date,IP=IP,country=country,user_shared_id=user_shared_id,user_followed_id=user_followed_id,followed_on=followed_on)[0]
    return c

def add_share(apparel_id,merchant_id,device,browser,os,date,IP,country,user_id,shared_on):
    c = ApparelShare.objects.get_or_create(apparel_id=apparel_id,merchant_id=merchant_id,device=device,browser=browser,os=os,date=date,IP=IP,country=country,user_id=user_id,shared_on=shared_on)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Apparel population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dressy.settings')
    from Analytics.models import ApparelTry
    from Analytics.models import ApparelFollow
    from Analytics.models import ApparelShare
    populate()
