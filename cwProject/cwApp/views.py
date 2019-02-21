from django.http import HttpResponse
from .models import Mom
from .models import Child

# default
def index(request):
    return HttpResponse('index')

# lists kids by moms in the terminal
def moms(request):
    allMoms = Mom.objects.all()
    for mothers in allMoms:
        print(f'{mothers.mom_fn} {mothers.mom_ln}')
        for kiddos in Child.objects.filter(child_mom__mom_fn=mothers.mom_fn):
            print(kiddos.child_fn)

    return HttpResponse('check the terminal')
# lists kids by moms in the terminal
def kiddos(request):
    allMoms = Mom.objects.all()
    for mothers in allMoms:
        for kiddos in Child.objects.filter(child_mom__mom_fn=mothers.mom_fn):
            print(kiddos.child_fn)
        print(f'{mothers.mom_fn} {mothers.mom_ln}')

    return HttpResponse('check the terminal')


# add one kid to each mom
def addchild(request):
    allMoms = Mom.objects.all()
    for mothers in allMoms:
        addChildDove = Child(child_fn='Nelly', child_ln='Grave', child_mom=mothers)
        addChildDove.save()

    return HttpResponse('check the admin')


# delete moms
def deltemom(request):
    allMoms = Mom.objects.all()
    allMoms[0].delete()
    return HttpResponse('check the admin')

