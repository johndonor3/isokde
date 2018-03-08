# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2017-12-05 12:01:21
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2017-12-05 12:19:32

from __future__ import print_function, division, absolute_import


class IsokdeError(Exception):
    """A custom core Isokde exception"""

    def __init__(self, message=None):

        message = 'There has been an error' \
            if not message else message

        super(IsokdeError, self).__init__(message)


class IsokdeNotImplemented(IsokdeError):
    """A custom exception for not yet implemented features."""

    def __init__(self, message=None):

        message = 'This feature is not implemented yet.' \
            if not message else message

        super(IsokdeNotImplemented, self).__init__(message)


class IsokdeApiError(IsokdeError):
    """A custom exception for API errors"""

    def __init__(self, message=None):
        if not message:
            message = 'Error with Http Response from Isokde API'
        else:
            message = 'Http response error from Isokde API. {0}'.format(message)

        super(IsokdeAPIError, self).__init__(message)


class IsokdeApiAuthError(IsokdeAPIError):
    """A custom exception for API authentication errors"""
    pass


class IsokdeMissingDependency(IsokdeError):
    """A custom exception for missing dependencies."""
    pass


class IsokdeWarning(Warning):
    """Base warning for Isokde."""
    pass


class IsokdeUserWarning(UserWarning, IsokdeWarning):
    """The primary warning class."""
    pass


class IsokdeSkippedTestWarning(IsokdeUserWarning):
    """A warning for when a test is skipped."""
    pass


class IsokdeDeprecationWarning(IsokdeUserWarning):
    """A warning for deprecated features."""
    pass

