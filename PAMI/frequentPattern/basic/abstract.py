#  Copyright (C)  2021 Rage Uday Kiran
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.


import abc


class _frequentPatterns(abc.ABC):
    def __init__(self, iFile, minSup, sep="\t"):
        self._iFile = iFile
        self._sep = sep
        self._minSup = minSup
        self._finalPatterns = {}
        self._oFile = str()
        self._memoryUSS = float()
        self._memoryRSS = float()
        self._startTime = float()
        self._endTime = float()

    '''@abstractmethod
    def iFile(self):
        """Variable to store the input file path/file name"""

        pass

    @abstractmethod
    def minSup(self):
        """Variable to store the user-specified minimum support value"""

        pass

    @abstractmethod
    def sep(self):
        """Variable to store the user-specified minimum support value"""

        pass

    @abstractmethod
    def startTime(self):
        """Variable to store the start time of the mining process"""

        pass

    @abstractmethod
    def endTime(self):
        """Variable to store the end time of the complete program"""

        pass

    @abstractmethod
    def memoryUSS(self):
        """Variable to store USS memory consumed by the program"""

        pass

    @abstractmethod
    def memoryRSS(self):
        """Variable to store RSS memory consumed by the program"""

        pass

    @abstractmethod
    def finalPatterns(self):
        """Variable to store the complete set of patterns in a dictionary"""

        pass

    @abstractmethod
    def oFile(self):
        """Variable to store the name of the output file to store the complete set of frequent patterns"""

        pass'''

    @abc.abstractmethod
    def startMine(self):
        pass

    @abc.abstractmethod
    def getPatterns(self):
        pass

    @abc.abstractmethod
    def save(self, oFile):
        pass

    @abc.abstractmethod
    def getPatternsAsDataFrame(self):
        pass

    @abc.abstractmethod
    def getMemoryUSS(self):
        pass

    @abc.abstractmethod
    def getMemoryRSS(self):
        pass

    @abc.abstractmethod
    def getRuntime(self):
        pass

    @abc.abstractmethod
    def printResults(self):
        pass
