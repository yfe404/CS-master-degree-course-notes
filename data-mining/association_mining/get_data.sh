#!/bin/bash
#
# Copyright (C) 2017-2018  Yann Feunteun <yannfeunteun@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DATA="$ROOT/data"

# Download weather.nominal.arff dataset
wget -q http://storm.cis.fordham.edu/~gweiss/data-mining/weka-data/weather.nominal.arff  -O "$DATA/weather.nominal.arff"

# Download supermarket.arff dataset
wget -q http://storm.cis.fordham.edu/~gweiss/data-mining/weka-data/supermarket.arff  -O "$DATA/supermarket.arff"
