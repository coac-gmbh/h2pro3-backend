from django.db import transaction
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from openbook_common.responses import ApiMessageResponse
from openbook_moderation.permissions import IsNotSuspended
from openbook_common.utils.helpers import normalise_request_data, normalize_list_value_in_request_data
from openbook_communities.views.community.serializers import GetCommunityCommunitySerializer, DeleteCommunitySerializer, \
    UpdateCommunitySerializer, UpdateCommunityAvatarSerializer, UpdateCommunityCoverSerializer, GetCommunitySerializer, \
    FavoriteCommunitySerializer, CommunityAvatarCommunitySerializer, CommunityCoverCommunitySerializer, \
    FavoriteCommunityCommunitySerializer, TopPostCommunityExclusionSerializer, \
    SubscribeToCommunityNotificationsSerializer, GroupSerializer, \
    SubscribeToCommunityNotificationsCommunitySerializer, LegacyGetCommunityCommunitySerializer
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseBadRequest


class CommunityItem(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)

    def get(self, request, community_name):
        serializer = GetCommunitySerializer(data={'community_name': community_name})
        serializer.is_valid(raise_exception=True)

        user = request.user
        community = user.get_community_with_name(community_name)

        community_serializer = self._get_community_serializer()
        response_serializer = community_serializer(community, context={"request": request})

        return Response(response_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, community_name):
        serializer = DeleteCommunitySerializer(data={'community_name': community_name})
        serializer.is_valid(raise_exception=True)

        user = request.user

        with transaction.atomic():
            user.delete_community_with_name(community_name)

        return Response(status=status.HTTP_200_OK)

    def patch(self, request, community_name):
        request_data = normalise_request_data(request.data)
        normalize_list_value_in_request_data(list_name='categories', request_data=request_data)
        from openbook_communities.models import Community
        community = Community.objects.get(name=community_name)
        serializer = GroupSerializer(community, data=request_data, partial=True)

        if serializer.is_valid(raise_exception=True):
            community = serializer.save()
            community.set_categories_with_names(categories_names=request_data.get('categories', []))
            community_serializer = self._get_community_serializer()
            response_serializer = community_serializer(community, context={"request": request})
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        return HttpResponseBadRequest()

    def _get_community_serializer(self):
        if self.request.version == '1.0':
            return GetCommunityCommunitySerializer
        return LegacyGetCommunityCommunitySerializer


class CommunityAvatar(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)

    def put(self, request, community_name):
        request_data = normalise_request_data(request.data)
        request_data['community_name'] = community_name

        serializer = UpdateCommunityAvatarSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)

        user = request.user

        data = serializer.validated_data
        avatar = data.get('avatar')

        with transaction.atomic():
            community = user.update_community_with_name_avatar(community_name, avatar=avatar)

        response_serializer = CommunityAvatarCommunitySerializer(community, context={"request": request})

        return Response(response_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, community_name):
        user = request.user

        with transaction.atomic():
            community = user.delete_community_with_name_avatar(community_name)

        response_serializer = CommunityAvatarCommunitySerializer(community, context={"request": request})

        return Response(response_serializer.data, status=status.HTTP_200_OK)


class CommunityCover(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)

    def put(self, request, community_name):
        request_data = normalise_request_data(request.data)
        request_data['community_name'] = community_name

        serializer = UpdateCommunityCoverSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)

        user = request.user

        data = serializer.validated_data
        cover = data.get('cover')

        with transaction.atomic():
            community = user.update_community_with_name_cover(community_name, cover=cover)

        response_serializer = CommunityCoverCommunitySerializer(community, context={"request": request})

        return Response(response_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, community_name):
        user = request.user

        with transaction.atomic():
            community = user.delete_community_with_name_cover(community_name)

        response_serializer = CommunityCoverCommunitySerializer(community, context={"request": request})

        return Response(response_serializer.data, status=status.HTTP_200_OK)


class FavoriteCommunity(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)

    def put(self, request, community_name):
        request_data = normalise_request_data(request.data)
        request_data['community_name'] = community_name

        serializer = FavoriteCommunitySerializer(data=request_data)
        serializer.is_valid(raise_exception=True)

        user = request.user

        with transaction.atomic():
            community = user.favorite_community_with_name(community_name)

        response_serializer = FavoriteCommunityCommunitySerializer(community, context={"request": request})

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, community_name):
        request_data = normalise_request_data(request.data)
        request_data['community_name'] = community_name

        serializer = FavoriteCommunitySerializer(data=request_data)
        serializer.is_valid(raise_exception=True)

        user = request.user

        with transaction.atomic():
            community = user.unfavorite_community_with_name(community_name)

        response_serializer = FavoriteCommunityCommunitySerializer(community, context={"request": request})

        return Response(response_serializer.data, status=status.HTTP_200_OK)


# LEGACY, Remove after 0.0.63
class LegacyExcludeTopPostsCommunity(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)

    def put(self, request, community_name):
        request_data = normalise_request_data(request.data)
        request_data['community_name'] = community_name

        serializer = TopPostCommunityExclusionSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)

        user = request.user

        with transaction.atomic():
            user.exclude_community_with_name_from_top_posts(community_name)

        return ApiMessageResponse(_('Community excluded from this feed'), status=status.HTTP_202_ACCEPTED)

    def delete(self, request, community_name):
        request_data = normalise_request_data(request.data)
        request_data['community_name'] = community_name

        serializer = TopPostCommunityExclusionSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)

        user = request.user

        with transaction.atomic():
            user.remove_exclusion_for_community_with_name_from_top_posts(community_name)

        return ApiMessageResponse(_('Community exclusion removed'), status=status.HTTP_202_ACCEPTED)


class SubscribeToCommunityNewPostNotifications(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)

    def put(self, request, community_name):
        request_data = normalise_request_data(request.data)
        request_data['community_name'] = community_name

        serializer = SubscribeToCommunityNotificationsSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        community_name = data.get('community_name')
        user = request.user

        with transaction.atomic():
            community = user.enable_new_post_notifications_for_community_with_name(community_name=community_name)

        response_serializer = SubscribeToCommunityNotificationsCommunitySerializer(community,
                                                                                   context={"request": request})

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, community_name):
        request_data = normalise_request_data(request.data)
        request_data['community_name'] = community_name

        serializer = SubscribeToCommunityNotificationsSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        community_name = data.get('community_name')
        user = request.user

        with transaction.atomic():
            community = user.disable_new_post_notifications_for_community_with_name(community_name=community_name)

        response_serializer = SubscribeToCommunityNotificationsCommunitySerializer(community,
                                                                                   context={"request": request})

        return Response(response_serializer.data, status=status.HTTP_200_OK)
