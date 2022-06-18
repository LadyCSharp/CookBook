from userapp.models import Profile
import random
def get_joke(request):
    jokes=['Жизнь слишком коротка, для того, чтобы есть невкусную еду!', 'Большие девочки не плачут, они едят.',
           'Затупил - заточи!','Пожрать и поржать!']
    return {"joke": random.choice(jokes)}

def get_profile(request):
    print(request)
    if request.user.is_authenticated:
        return {"profile_id": Profile.objects.get(user=request.user).id}
    else:
        return {"profile_id":-1}