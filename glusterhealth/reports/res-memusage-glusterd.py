#
# Copyright (c) 2017 Red Hat, Inc.
#
# This file is part of gluster-health-report project which is a
# subproject of GlusterFS ( www.gluster.org)
#
# This file is licensed to you under your choice of the GNU Lesser
# General Public License, version 3 or any later version (LGPLv3 or
# later), or the GNU General Public License, version 2 (GPLv2), in all
# cases as published by the Free Software Foundation.

import logging

from utils import command_output, CommandError

#TODO:We need to extend this to glusterfsd and glusterfs.
procs = ['glusterd']

def report_resmemusagegluster(ctx):
    try:

        for i in procs:
            cmd = "cat /proc/`pgrep %s`/status | grep -i vmrss | awk '{print $2}'" % (i)
            out = command_output(cmd)
            ctx.ok("Glusterd ResMem in kB", memory=out.strip())



    except CommandError as e:
        ctx.notok("Glusterd is not running")
        logging.warn(ctx.lf("Glusterd is not running",
                            error_code=e[0],
                            error=e[1]))
