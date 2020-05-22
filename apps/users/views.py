# from .models import UserProfile
# from .serializer import UserProfileSerializers
#
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.reverse import reverse
# from rest_framework import viewsets
#
#
# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format)
#     })
#
#
# class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializers