from django.core.mail import send_mail
from Isure.models import EmailContact
from datetime import date

def mailit(source,content):
    print "******* Enter Mail it *****"
    send_mail(
    content.subj,
    "The following email is from "+content.name+"("+content.sender+")\n"+content.msg,
    "director@v2.intersure.com",
    content.to,
    fail_silently=False,
)
    this_contact = EmailContact()
    this_contact.pagesource = source
    this_contact.receivedfrom = content.sender 
    this_contact.sendto = content.to
    this_contact.content = content.msg
    this_contact.date=date.today()
    this_contact.save()
    return True
