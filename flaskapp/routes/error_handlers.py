#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
This file is a part of heartvoices.org project.

The software embedded in or related to heartvoices.org
is provided under a some-rights-reserved license. This means
that Users are granted broad rights, including but not limited
to the rights to use, execute, copy or distribute the software,
to the extent determined by such license. The terms of such
license shall always prevail upon conflicting, divergent or
inconsistent provisions of these Terms. In particular, heartvoices.org
and/or the software thereto related are provided under a GNU GPLv3 license,
allowing Users to access and use the software’s source code.
Terms and conditions: https://www.goandtodo.org/terms-and-conditions

Created Date: Sunday October 17th 2021
Author: GO and to DO Inc
E-mail: heartvoices.org@gmail.com
-----
Last Modified: Sunday, October 17th 2021, 2:35:43 pm
Modified By: GO and to DO Inc
-----
Copyright (c) 2021
"""


def error_handler_factory(
    *,
    status_code=404,
    exit_code=1,
    error_template='',
    message='failed'
):
    """General error-handler factory for flaskapp
    """

    def error_handler(error):
        return {
            "status_code": status_code,
            "exit_code": exit_code,
            "error": error_template.format(error),
            "message": message
        }, status_code

    return error_handler
