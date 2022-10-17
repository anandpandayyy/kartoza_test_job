from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import User
from django.contrib import admin
from django.utils.html import escape
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib.admin.models import ADDITION, CHANGE, DELETION, LogEntry
from django.utils.translation import pgettext_lazy
from django.contrib.contenttypes.models import ContentType
from django.urls import NoReverseMatch, reverse
from django.utils.encoding import force_str


class UserAdmin(admin.ModelAdmin):

    def get_fieldsets(self, request, obj):
        if obj is None:
            return [
                (
                    None,
                    {'fields': ('type', 'description',)}
                )
            ]
        elif request.user.is_superuser:
            return [
                (
                    None,
                    {'fields': ('password', 'username', 'email',
                                'address', 'phone_number')}
                )
            ]
        else:
            return [
                (
                    None,
                    {'fields': ('password', 'username', 'email',
                                'address', 'phone_number')}
                )
            ]


action_names = {
    ADDITION: pgettext_lazy("logentry_admin:action_type", "Logged In"),
    DELETION: pgettext_lazy("logentry_admin:action_type", "Logged Out"),
    CHANGE: pgettext_lazy("logentry_admin:action_type", "Change"),
}


class LogEntryAdmin(admin.ModelAdmin):
    """
    Log-in log-out entry's
    """

    list_display_links = ["action_time", "action_description"]

    list_display = [
        "user_details",
        "content_type",
        "action_description",
        "action_time",
    ]

    def get_actions(self, request):
        actions = super(LogEntryAdmin, self).get_actions(request)
        actions.pop("delete_selected", None)
        return actions

    def action_description(self, obj):
        return action_names[obj.action_flag]
    action_description.short_description = _("action")

    def user_details(self, obj):
        content_type = ContentType.objects.get_for_model(type(obj.user))
        user_link = escape(force_str(obj.user))
        try:
            url = reverse(
                "admin:{}_{}_change".format(
                    content_type.app_label, content_type.model),
                args=[obj.user.pk],
            )
            user_link = '<a href="{}">{}</a>'.format(url, user_link)
        except NoReverseMatch:
            pass
        return mark_safe(user_link)

    user_details.admin_order_field = "user"
    user_details.short_description = _("user")


admin.site.register(LogEntry, LogEntryAdmin)
admin.site.register(User, UserAdmin)
