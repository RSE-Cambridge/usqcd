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


class Qla(AutotoolsPackage):
    """QLA provides a standard interface for linear algebra routines that can
    act on a site or a array of sites with several indexing options."""

    homepage = "http://usqcd.jlab.org/usqcd-docs/qla"
    url      = "https://github.com/usqcd-software/qla/archive/qla1-9-0.tar.gz"

    version('1-9-0', '730f3aabfa98c69b83aba7be114aeaee')
    version('1-8-0', 'bc0e4ca89ebabc386ee2d84ca6aeff38')
    version('1-7-2', 'c37a03aaf11537555c5c21c79966506c')
    version('1-7-1', 'da68b0b22068b4e1c379dc8553b154c8')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    def autoreconf(self, spec, prefix):
        autoreconf('--install', '--verbose', '--force')

    def configure_args(self):
        args = []
        return args
