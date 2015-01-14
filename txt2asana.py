#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Simple script to read a text file with one task per line and add everty task to
asana.

Copyright (C) 2012 Corp B2C S.A.C.

This program is free software; you can redistribute it and/or
modify it under the terms of version 2 of the GNU General Public
License published by the Free Software Foundation.

Needs asana from: https://github.com/pandemicsyn/asana

Author:
    Nicolas Valcárcel Scerpella <nvalcarcel@corpb2c.com>
"""

import sys

import asana

FILENAME = 'tasks.txt'
API_KEY = ''
PROJECT_ID = ''


def read_tasks():
    """
    Reads the file, returns list with tasks
    """
    try:
        f = open(FILENAME)
    except IOError:
        print 'Error: Could not read %s' % FILENAME
        sys.exit(1)
    else:
        ret = f.readlines()
    finally:
        f.close()

    return ret


def file_tasks(tasks, api, ws):
    """
    File tasks to asana.
    """
    res = []
    for task in tasks:
        res.append(api.create_task(task, ws))

    return res


def assign_to_project(tasks, api):
    """
    Assign tasks to project.
    """
    for task in tasks:
        api.add_project_to_task(PROJECT_ID, task[u'id'])


def main():
    """
    Main function.
    """
    api = asana.AsanaAPI(API_KEY)

    myspaces = api.list_workspaces()

    tasks = read_tasks()
    a_tasks = file_tasks(tasks, api, myspaces[0][u'id'])
    if PROJECT_ID:
        assign_to_project(a_tasks, api)


if __name__ == '__main__':
    main()
