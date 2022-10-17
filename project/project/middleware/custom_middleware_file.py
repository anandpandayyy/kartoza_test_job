from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class ExampleMiddleware(MiddlewareMixin, object):
    """
    this middleware will redirect user bases on thier role
    (normal user or superuser)
    """

    def _init_(self, get_response):
        self.get_response = get_response

    def _call_(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        if request.user.is_anonymous or request.user.is_superuser:
            return
        if request.user.is_staff:
            if "admin" in request.path:
                if request.path in [
                    "/admin/app/user/" + str(request.user.pk) + "/change/",
                    "/admin/logout/",
                    "/admin/password_change/",
                ]:
                    return
                return redirect(
                    "/admin/app/user/" + str(request.user.pk) + "/change/"
                )
