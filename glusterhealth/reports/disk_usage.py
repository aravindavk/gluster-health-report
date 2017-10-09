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
from utils import get_disk_usage_details
	
def check_disk_usage_percetage(ctx, path, percentage=0):
	out = get_disk_usage_details(path)
	if out is None:
		return
	if out.percentage:
		used_percent = int(out.percentage.split('%')[0])
		if used_percent >= percentage:
			ctx.notok("Disk used percentage for \'"+ path +"\' is exceeding "+ str(percentage) +"%, consider deleting unneccesary data")
		else:
			ctx.ok("Disk used percentage for \'"+ path +"\' is " + str(used_percent) +"%")
		
def report_system_mounts_disk_usage(ctx):
	check_disk_usage_percetage(ctx, "/", 90)
	check_disk_usage_percetage(ctx, "/var", 90)
	check_disk_usage_percetage(ctx, "/tmp", 90)

def report_brick_disk_usage(ctx):
	# ToDo : Add brick disk usage report
	pass
