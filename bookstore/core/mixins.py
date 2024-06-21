from rest_framework.serializers import BaseSerializer


class SerializerClassByActionMixin(object):

    def get_serializer_class(self):
        try:
            match = self.serializer_action_classes[self.action]
            if issubclass(match, BaseSerializer):
                return match
            return match[self.request.method]
        except (KeyError, AttributeError):
            return super().get_serializer_class()


class PermissionsByActionMixin(object):

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]