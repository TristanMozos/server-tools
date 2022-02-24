# Copyright https://github.com/jayluxferro/megatools-python
# !/usr/bin/env python3

"""
Author: Jay Lux Ferro
Email:  jayluxferro@sperixlabs.org, jay@ovond.com
Date:   23rd August, 2019
"""

from . import helper as hp
import os


class Mega:
    # Default path on Linux
    megaPath = '/usr/bin/'
    dir_path = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, megaPath=None, mega_username=None, mega_pass=None):
        if megaPath != None:
            self.megaPath = megaPath if megaPath[-1] == '/' else megaPath + '/'
        self.mega_username = mega_username
        self.mega_pass = mega_pass

    def df(self, f='g'):
        f = '--mb' if f.lower() == 'm' else '--gb'
        return hp.formatDf([self.megaPath + 'megadf', f, '--username', self.mega_username, '--password', self.mega_pass])

    def ls(self, path='/'):
        return hp.ls([self.megaPath + 'megals', '--username', self.mega_username, '--password', self.mega_pass, path if path[0] == '/' else '/' + path])

    def put(self, fileName, serverPath='/Root'):
        return hp.put([self.megaPath + 'megaput', '--username', self.mega_username, '--password', self.mega_pass, '--path', serverPath, fileName])

    def rm(self, filePath):
        return hp.rm([self.megaPath + 'megarm', '--username', self.mega_username, '--password', self.mega_pass, filePath])

    def md(self, directoryPath):
        return hp.md([self.megaPath + 'megamkdir', '--username', self.mega_username, '--password', self.mega_pass, directoryPath])

    def copy(self, localDirectoryPath, remoteDirectoryPath, download=False):
        download = '' if not download else '--download'
        return hp.copy([self.megaPath + 'megacopy', '--username', self.mega_username, '--password', self.mega_pass, '--local', localDirectoryPath, '--remote',
                        remoteDirectoryPath, download])

    def get(self, remoteFile):
        return hp.get([self.megaPath + 'megaget', '--username', self.mega_username, '--password', self.mega_pass, remoteFile])

    def url(self, remoteFile):
        return hp.url([self.megaPath + 'megals', '--username', self.mega_username, '--password', self.mega_pass, remoteFile, '--export'])

    def dl(self, url):
        return hp.dl([self.megaPath + 'megadl', '--username', self.mega_username, '--password', self.mega_pass, url])
