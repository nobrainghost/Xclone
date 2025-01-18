def jwt_cookie_middleware(get_response):
    def middleware(request):
        token=request.COOKIES.get('access_token')
        if token is not None:
            request.META['HTTP_AUTHORIZATION']=f'Bearer {token}'
        response=get_response(request)
        return response
    
    return middleware