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


class Qdp(AutotoolsPackage):
    """QDP/C is the C implementation of the QDP (QCD Data Parallel) interface."""

    homepage = "http://usqcd.jlab.org/usqcd-docs/qdp/"
    url      = "https://github.com/usqcd-software/qdp/archive/qdp1-11-1.tar.gz"

    version('1-11-1', '722d56a47f996f987a9a2efd00c38eb0')
    version('1-11-0', 'b3a0dfba20a5ab34218c765adb86d5d5')
    version('1-10-2', '506ca3e76ce827df8897f48c6214d29d')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    depends_on('qmp')
    depends_on('qio')
    depends_on('qla')

    def autoreconf(self, spec, prefix):
        autoreconf('--install', '--verbose', '--force')

    def configure_args(self):
        args = [
            '--with-qmp=%s' % self.spec['qmp'].prefix,
            '--with-qio=%s' % self.spec['qio'].prefix,
            '--with-qla=%s' % self.spec['qla'].prefix,
            ]
        return args
