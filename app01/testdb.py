from django.http import HttpResponse
from app01.models import Test,Test2

def testdb(request):
    response=""
    response1=""

    list1=Test.objects.all()
    list2=Test2.objects.all()

    response3=Test2.objects.get(id=1)

    return HttpResponse(list1)







