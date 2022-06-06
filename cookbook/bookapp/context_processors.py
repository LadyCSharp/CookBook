from userapp.models import Profile

def get_joke(request):
    return {"joke": 'Жизнь слишком коротка, для того, чтобы есть невкусную еду!'}

def get_profile(request):
    print(request)
    if request.user.is_authenticated:
        return {"profile_id": Profile.objects.get(user=request.user).id}
    else:
        return {"profile_id":-1}