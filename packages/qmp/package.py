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


class Qmp(AutotoolsPackage):
    """QMP provides a standard communications layer for Lattice QCD."""

    homepage = "http://usqcd.jlab.org/usqcd-docs/qmp"
    url      = "https://github.com/usqcd-software/qmp/archive/qmp2-5-0.tar.gz"

    version('2-5-0', '2070a9c6c46e9aa2fce6b4a4f3df280d')
    version('2-4-1', 'a6dd17b18e9413d55e0ab958689f659d')

    variant('mpi', default=True)

    depends_on('mpi', when='+mpi')

    def configure_args(self):
        args = []
        if '+mpi' in self.spec:
          args += [
              '--with-qmp-comms-type=MPI',
              'CC=%s'  % self.spec['mpi'].mpicc,
              'CXX=%s' % self.spec['mpi'].mpicxx,
              'CFLAGS=-std=c99',
              ]
        else:
          args+= [
              '--with-qmp-comms-type=SINGLE',
              ]
        return args
