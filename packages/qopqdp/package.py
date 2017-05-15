##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Qopqdp(AutotoolsPackage):
    """QOPQDP is an implementation of the QOP level-three interface using QDP."""

    homepage = "http://usqcd.jlab.org/usqcd-docs/qopqdp"
    url      = "https://github.com/usqcd-software/qopqdp/archive/qopqdp0-20-1.tar.gz"

    version('0-20-1', '26b35b18963f7a83da0e7ba0ed94ef51')
    version('0-20-0', 'f2083898304892184f499f6b52a82d55')
    version('0-19-4', '62b364e420cb5cf3ccb7bfaa9e5c16cf')
    version('0-19-3', '5bf110387595c59bd299148263cae5c2')
    version('0-19-1', '492d8782732f4a57284758ba3f05c583')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    depends_on('qmp')
    depends_on('qio')
    depends_on('qla')
    depends_on('qdp')

    def autoreconf(self, spec, prefix):
        autoreconf('--install', '--verbose', '--force')

    def configure_args(self):
        args = [
            'CFLAGS=-std=c99',
            '--with-qmp=%s' % self.spec['qmp'].prefix,
            '--with-qio=%s' % self.spec['qio'].prefix,
            '--with-qla=%s' % self.spec['qla'].prefix,
            '--with-qdp=%s' % self.spec['qdp'].prefix,
            ]
        return args
