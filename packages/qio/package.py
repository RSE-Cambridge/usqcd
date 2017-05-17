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


class Qio(AutotoolsPackage):
    """QIO provides as suite of input/output routines for lattice data."""

    homepage = "http://usqcd.jlab.org/usqcd-docs/qio"
    url      = "https://github.com/usqcd-software/qio/archive/qio2-4-2.tar.gz"

    version('2-4-2', '6ba561e774fe79789c838f5a78827883')
    version('2-4-0', '46858fe11400ee5c3b7b7706370b38b5')
    version('2-3-9', '072026b7ae4e93c0fee29568fb18abad')
    version('master', git='git@github.com:usqcd-software/qio.git', branch='master')
    submodules=True

    variant('mpi', default=True)

    depends_on('qmp')
    depends_on('qmp+mpi', when='+mpi')
    depends_on('mpi', when='+mpi')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    def autoreconf(self, spec, prefix):
        which('git')('submodule', 'update', '--init', '--recursive')
        autoreconf('--install', '--verbose', '--force')

    def configure_args(self):
        args = [
            '--with-qmp=%s' % self.spec['qmp'].prefix,
            ]
        if '+mpi' in self.spec:
          args += [
              'CC=%s' % self.spec['mpi'].mpicc,
              'CFLAGS=-std=c99',
              '--with-qio-comms-type=MPI',
              '--enable-parallel-io',
              ]
        return args
