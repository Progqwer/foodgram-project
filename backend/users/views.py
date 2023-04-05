from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import exceptions, status
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response

from .models import CustomUser, Follow


class CustomUserViewSet(UserViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def followers(self, request):
        user = self.request.user
        user_follows = user.follower.all()
        authors = [item.author.id for item in user_follows]
        queryset = CustomUser.objects.filter(pk__in=authors)
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = self.get_serializer(paginated_queryset, many=True)

        return self.get_paginated_response(serializer.data)

    def follow(self, request, id=None):
        user = self.request.user
        author = get_object_or_404(CustomUser, pk=id)

        if self.request.method == 'POST':
            if user == author:
                raise exceptions.ValidationError(
                    'Вы не можете подписаться на самого себя.'
                )
            if Follow.objects.filter(
                user=user,
                author=author
            ).exists():
                raise exceptions.ValidationError('Вы уже подписанны на данного пользователя.')

            Follow.objects.create(user=user, author=author)
            serializer = self.get_serializer(author)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if self.request.method == 'DELETE':
            if not Follow.objects.filter(
                user=user,
                author=author
            ).exists():
                raise exceptions.ValidationError(
                    'Вы и так не подписанны на данного пользователя.'
                )

            following = get_object_or_404(
                Follow,
                user=user,
                author=author
            )
            following.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)