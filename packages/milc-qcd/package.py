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


class MilcQcd(Package):
    """The MIMD Lattice Collaboration (MILC) Code"""

    homepage = "http://www.physics.utah.edu/~detar/milc/"
    url      = "http://www.physics.utah.edu/%7Edetar/milc/milc_qcd-7.8.1.tar.gz"

    version('7.8.1', '7789ba82e93ac3e34395f13c6916d4d9')

    #variant('apps', values=('ks_spectrum', 'ext_src'), multi=True)

    depends_on('qmp+mpi')
    depends_on('qio+mpi')
    depends_on('qla')
    depends_on('qdp')
    depends_on('qopqdp')
    depends_on('fftw+double')
    depends_on('mpi')

    phases = ['edit', 'install']
    parallel = False

    def edit(self, spec, prefix):
        makefile = FileFilter('Makefile')
        if '%intel' in spec:
          makefile.filter('COMPILER = .*', 'COMPILER = intel')
        else:
          makefile.filter('COMPILER = .*', 'COMPILER = gnu')
        makefile.filter('MPP = .*', 'MPP = true')

        makefile.filter('QMPPAR = .*', 'QMPPAR = %s' % spec['qmp'].prefix)
        makefile.filter('QIOPAR = .*', 'QIOPAR = %s' % spec['qio'].prefix)
        makefile.filter('QLA = .*', 'QLA = %s' % spec['qla'].prefix)
        makefile.filter('QDP = .*', 'QDP = %s' % spec['qdp'].prefix)
        makefile.filter('QOPQDP = .*', 'QOPQDP = %s' % spec['qopqdp'].prefix)

        makefile.filter('PRECISION = .*', 'PRECISION = 2')

        makefile.filter('WANTFFTW = .*', 'WANTFFTW = true')
        makefile.filter('FFTW = .*', 'FFTW = %s' % spec['fftw'].prefix)

        makefile.filter('OPT = .*', 'OPT = -g -O3 -march=native')

    def install(self, spec, prefix):
        copy = which('cp')
        mkdirp(prefix.bin)

        with working_dir('ks_spectrum'):
          copy('../Makefile', '.')
          make('ks_spectrum_hisq')
          install('ks_spectrum_hisq', prefix.bin)
        with working_dir('ext_src'):
          copy('../Makefile', '.')
          make('ext_src')
          install('ext_src', prefix.bin)
