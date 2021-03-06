# The Hazard Library
# Copyright (C) 2012 GEM Foundation
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from openquake.hazardlib.gsim.youngs_1997 import YoungsEtAl1997SInter
from openquake.hazardlib.gsim.youngs_1997 import YoungsEtAl1997SSlab

from tests.gsim.utils import BaseGSIMTestCase

# Test data generated from OpenSHA implementation.


class YoungsEtAl1997SInterTestCase(BaseGSIMTestCase):
    GSIM_CLASS = YoungsEtAl1997SInter

    def test_mean(self):
        self.check('YOUNGS97/Y97SInter_MEAN.csv',
                   max_discrep_percentage=0.1)

    def test_std_total(self):
        self.check('YOUNGS97/Y97SInter_STD_TOTAL.csv',
                   max_discrep_percentage=0.1)


class YoungsEtAl1997SSlabTestCase(BaseGSIMTestCase):
    GSIM_CLASS = YoungsEtAl1997SSlab

    def test_mean(self):
        self.check('YOUNGS97/Y97SSlab_MEAN.csv',
                   max_discrep_percentage=0.1)

    def test_std_total(self):
        self.check('YOUNGS97/Y97SSlab_STD_TOTAL.csv',
                   max_discrep_percentage=0.1)
