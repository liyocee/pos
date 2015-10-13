from rest_framework import serializers
from common.serializers import AbstractFieldsMixin
from rest_framework.exceptions import ValidationError
from django.db import transaction
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer
from .models import(
    Organization, SalesAgent,
    ProductTypes, Sales)


class BaseMemberSerializer(
    AbstractFieldsMixin, serializers.ModelSerializer
):
    profile = UserSerializer()

    @transaction.atomic
    def create(self, validated_data):
        user = get_user_model().objects.create(
            **validated_data['profile'])
        validated_data['profile'] = user
        return self.Meta.model.objects.create(**validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        profile = self.initial_data.get('profile', None)
        if profile:
            try:
                user = get_user_model().objects.get(pk=profile.pop('id'))
                for attr, value in profile.items():
                    setattr(user, attr, value)
                user.save()
                validated_data['profile'] = user
            except KeyError:
                raise ValidationError({'profile': "id for user not provided"})
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class OrganizationSerializer(BaseMemberSerializer):

    class Meta:
        model = Organization


class SalesAgentSerializer(BaseMemberSerializer):

    class Meta:
        model = SalesAgent


class ProductTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductTypes


class SalesSerializer(serializers.ModelSerializer):
    agent_details = SalesAgentSerializer(
        source="agent", read_only=True)
    product_details = ProductTypesSerializer(
        source="product", read_only=True)

    class Meta:
        model = Sales
