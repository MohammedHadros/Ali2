
def room_name(request):
    return {'room_name' :request.user.username}