from django.shortcuts import render

from state.models import District, State


# Create your views here.
def dropdown(request):
    state = State.objects.all()
    return render(request,'state/dropdown.html',{'state':state,})

def state_check(request):
    print('working')
    id=request.GET['id']
    print(id)
    district_data=District.objects.filter(state_id=id)
    print(district_data)
    
    return render(request,'state/district.html',{'dist_data':district_data})