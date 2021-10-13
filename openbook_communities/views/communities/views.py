# Create your views here.
from django.db import transaction
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import gettext as _

from openbook_common.serializers import CommonSearchCommunitiesSerializer, CommonSearchCommunitiesCommunitySerializer
from openbook_moderation.permissions import IsNotSuspended
from openbook_common.responses import ApiMessageResponse
from openbook_common.utils.helpers import normalize_list_value_in_request_data, normalise_request_data
from openbook_communities.views.communities.serializers import CreateCommunitySerializer, \
    CommunitiesCommunitySerializer, CommunityNameCheckSerializer, \
    GetFavoriteCommunitiesSerializer, GetJoinedCommunitiesSerializer, TrendingCommunitiesSerializer, \
    GetModeratedCommunitiesSerializer, GetAdministratedCommunitiesSerializer, SuggestedCommunitiesCommunitySerializer
from openbook_communities.views.community.serializers import GroupSerializer
from openbook_communities.models import CommunityMembership
from django.http import HttpResponseBadRequest


class Communities(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)

    def put(self, request):
        request_data = normalise_request_data(request.data)
        normalize_list_value_in_request_data(list_name='categories', request_data=request_data)
        serializer = GroupSerializer(data=request_data)
        if serializer.is_valid(raise_exception=True):
            community = serializer.save(creator=request.user)
            CommunityMembership.create_membership(user=request.user, is_administrator=True, is_moderator=False,
                                                  community=community)
            response_serializer = CommunitiesCommunitySerializer(community, context={"request": request})
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return HttpResponseBadRequest()

    def get(self, request):
        query_params = request.query_params.dict()
        serializer = GetJoinedCommunitiesSerializer(data=query_params)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        count = data.get('count', 10)
        offset = data.get('offset', 0)

        user = request.user

        communities = user.get_joined_communities()[offset:offset + count]

        response_serializer = CommonSearchCommunitiesCommunitySerializer(communities, many=True,
                                                                         context={"request": request})

        return Response(response_serializer.data, status=status.HTTP_200_OK)


class CommunityNameCheck(APIView):
    """
    The API to check if a communityName is both valid and not taken.
    """
    serializer_class = CommunityNameCheckSerializer
    permission_classes = (IsAuthenticated, IsNotSuspended)

    def post(self, request):
        # Serializer contains validators
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return ApiMessageResponse(_('Community name available'), status=status.HTTP_202_ACCEPTED)


class JoinedCommunities(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)

    def get(self, request):
        query_params = request.query_params.dict()
        serializer = GetJoinedCommunitiesSerializer(data=query_params)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        count = data.get('count', 10)
        offset = data.get('offset', 0)
        excluded_from_profile_posts = data.get('excluded_from_profile_posts')

        user = request.user

        communities = user.get_joined_communities(excluded_from_profile_posts=excluded_from_profile_posts)[
                      offset:offset + count]

        response_serializer = CommonSearchCommunitiesCommunitySerializer(communities, many=True,
                                                                         context={"request": request})

        return Response(response_serializer.data, status=status.HTTP_200_OK)


class SearchJoinedCommunities(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)

    def get(self, request):
        query_params = request.query_params.dict()
        serializer = CommonSearchCommunitiesSerializer(data=query_params)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        count = data.get('count', 10)
        query = data.get('query')
        excluded_from_profile_posts = data.get('excluded_from_profile_posts')

        user = request.user

        communities = user.search_joined_communities_with_query(query=query,
                                                                excluded_from_profile_posts=excluded_from_profile_posts)[
                      :count]

        response_serializer = CommonSearchCommunitiesCommunitySerializer(communities, many=True,
                                                                         context={"request": request})

        return Response(response_serializer.data, status=status.HTTP_200_OK)


class ModeratedCommunities(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)

    def get(self, request):
        query_params = request.query_params.dict()
        serializer = GetModeratedCommunitiesSerializer(data=query_params)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        count = data.get('count', 10)
        offset = data.get('offset', 0)

        user = request.user

        communities = user.get_moderated_communities()[offset:offset + count]

        response_serializer = CommonSearchCommunitiesCommunitySerializer(communities, many=True,
                                                                         context={"request": request})

        return Response(response_serializer.data, status=status.HTTP_200_OK)


class SearchModeratedCommunities(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)

    def get(self, request):
        query_params = request.query_params.dict()
        serializer = CommonSearchCommunitiesSerializer(data=query_params)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        count = data.get('count', 10)
        query = data.get('query')

        user = request.user

        communities = user.search_moderated_communities_with_query(query=query)[:count]

        response_serializer = CommonSearchCommunitiesCommunitySerializer(communities, many=True,
                                                                         context={"request": request})

        return Response(response_serializer.data, status=status.HTTP_200_OK)


class AdministratedCommunities(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)

    def get(self, request):
        query_params = request.query_params.dict()
        serializer = GetAdministratedCommunitiesSerializer(data=query_params)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        count = data.get('count', 10)
        offset = data.get('offset', 0)

        user = request.user

        communities = user.get_administrated_communities()[offset:offset + count]

        response_serializer = CommonSearchCommunitiesCommunitySerializer(communities, many=True,
                                                                         context={"request": request})

        return Response(response_serializer.data, status=status.HTTP_200_OK)


class SearchAdministratedCommunities(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)

    def get(self, request):
        query_params = request.query_params.dict()
        serializer = CommonSearchCommunitiesSerializer(data=query_params)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        count = data.get('count', 10)
        query = data.get('query')

        user = request.user

        communities = user.search_administrated_communities_with_query(query=query)[:count]

        response_serializer = CommonSearchCommunitiesCommunitySerializer(communities, many=True,
                                                                         context={"request": request})

        return Response(response_serializer.data, status=status.HTTP_200_OK)


class TrendingCommunities(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)
    serializer_class = TrendingCommunitiesSerializer

    def get(self, request):
        query_params = request.query_params.dict()
        serializer = self.serializer_class(data=query_params)
        serializer.is_valid(raise_exception=True)

        data = serializer.data
        category_name = data.get('category')

        user = request.user

        communities = user.get_trending_communities(category_name=category_name)[:30]

        posts_serializer = CommonSearchCommunitiesCommunitySerializer(communities, many=True,
                                                                      context={"request": request})
        return Response(posts_serializer.data, status=status.HTTP_200_OK)


class FavoriteCommunities(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)

    def get(self, request):
        query_params = request.query_params.dict()
        serializer = GetFavoriteCommunitiesSerializer(data=query_params)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        count = data.get('count', 10)
        offset = data.get('offset', 0)

        user = request.user

        communities = user.get_favorite_communities()[offset:offset + count]

        posts_serializer = CommonSearchCommunitiesCommunitySerializer(communities, many=True,
                                                                      context={"request": request})
        return Response(posts_serializer.data, status=status.HTTP_200_OK)


class SuggestedCommunities(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)

    def get(self, request):
        user = request.user

        communities = user.get_suggested_communities()

        communities_serializer = SuggestedCommunitiesCommunitySerializer(communities, many=True,
                                                                         context={"request": request})
        return Response(communities_serializer.data, status=status.HTTP_200_OK)


class SearchFavoriteCommunities(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)

    def get(self, request):
        query_params = request.query_params.dict()
        serializer = CommonSearchCommunitiesSerializer(data=query_params)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        count = data.get('count', 10)
        query = data.get('query')

        user = request.user

        communities = user.search_favorite_communities_with_query(query=query)[:count]

        response_serializer = CommonSearchCommunitiesCommunitySerializer(communities, many=True,
                                                                         context={"request": request})

        return Response(response_serializer.data, status=status.HTTP_200_OK)


class SearchCommunities(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)

    def get(self, request):
        query_params = request.query_params.dict()
        serializer = CommonSearchCommunitiesSerializer(data=query_params)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        count = data.get('count', 20)
        query = data.get('query')
        excluded_from_profile_posts = data.get('excluded_from_profile_posts')

        user = request.user

        communities = user.search_communities_with_query(query=query,
                                                         excluded_from_profile_posts=excluded_from_profile_posts)[
                      :count]

        response_serializer = CommonSearchCommunitiesCommunitySerializer(communities, many=True,
                                                                         context={"request": request})

        return Response(response_serializer.data, status=status.HTTP_200_OK)
