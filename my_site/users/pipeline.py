def get_avatar(backend, response, user=None, *args, **kwargs):
    if user is None:
        return

    if backend.name == 'vk-oauth2':
        url = response.get('photo_big', '')
    else:
        url = None

    if url:
        user.profile.avatar = url
        user.profile.save()
