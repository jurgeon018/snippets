# -*- coding: utf-8 -*-
"""Cisco Spark Webhook-Event data model."""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *

from .sparkdata import SparkData


__author__ = "Chris Lunsford"
__author_email__ = "chrlunsf@cisco.com"
__copyright__ = "Copyright (c) 2016-2018 Cisco and/or its affiliates."
__license__ = "MIT"


class WebhookEventBasicPropertiesMixin(object):
    """A mixin for :class:`SparkData` classes."""

    @property
    def id(self):
        """Webhook ID."""
        return self._json_data.get('id')

    @property
    def name(self):
        """A user-friendly name for this webhook."""
        return self._json_data.get('name')

    @property
    def resource(self):
        """The resource type for the webhook."""
        return self._json_data.get('resource')

    @property
    def event(self):
        """The event type for the webhook."""
        return self._json_data.get('event')

    @property
    def filter(self):
        """The filter that defines the webhook scope."""
        return self._json_data.get('filter')

    @property
    def orgId(self):
        """The ID of the organization that owns the webhook."""
        return self._json_data.get('orgId')

    @property
    def createdBy(self):
        """The ID of the person that added the webhook."""
        return self._json_data.get('createdBy')

    @property
    def appId(self):
        """Identifies the application that added the webhook."""
        return self._json_data.get('appId')

    @property
    def ownedBy(self):
        """Indicates if the webhook is owned by the `org` or the `creator`.

        Webhooks owned by the creator can only receive events that are
        accessible to the creator of the webhook. Those owned by the
        organization will receive events that are visible to anyone in the
        organization.

        """
        return self._json_data.get('ownedBy')

    @property
    def status(self):
        """Indicates if the webhook is active.

        A webhook that cannot reach your URL is disabled.

        """
        return self._json_data.get('status')

    @property
    def actorId(self):
        """The ID of the person that caused the webhook to be sent."""
        return self._json_data.get('actorId')

    @property
    def data(self):
        """The data for the resource that triggered the webhook."""
        return SparkData(self._json_data.get('data'))
