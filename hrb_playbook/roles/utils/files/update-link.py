#!/usr/bin/python

import sys, os
import argparse
import subprocess
from distutils.version import LooseVersion
import re

def main():
    kwargs = parse_argv(sys.argv[1:])
    module = kwargs.module[0]
    version = None if kwargs.version ==None else kwargs.version[0]
    product_dir = '/opt/repo/env/'+module if kwargs.product_dir ==None \
                    else os.path.join(kwargs.product_dir[0], module)
    if not os.path.isdir(product_dir):
        raise Exception('Not a valid product directory: ' + product_dir)

    target = get_path(product_dir, version)
    if not os.path.isdir(target):
        raise Exception('Can not find target directory: ' +target)

    link_name = '/opt/'+module
    if os.path.isdir(os.path.dirname(link_name)) != True:
        os.makedirs(os.path.dirname(link_name), 0755)
    if os.path.exists(link_name):
        if os.path.islink(link_name):
            os.remove(link_name)
        else:
            raise Exception("Remove old link error, not a link: "+link_name)

    cmd = ['ln', '-s', target, link_name]
    returncode = subprocess.call(cmd)
    if returncode != 0:
        raise Exception('Cmd false: ' + ' '.join(cmd))

def get_path(product_dir, version):
    if version == None:
        if len(os.listdir(product_dir)) == 0:
            raise Exception('Empty directory: ' + product_dir)
        version = LooseVersion('0.0.0.0')
        dir_names = [f for f in os.listdir(product_dir) if
                     re.match('^(\d+\.){3}\d+', f)]
        for f in dir_names:
            tmp = LooseVersion(f)
            if version < tmp:
                version = tmp
        version = version.__str__()
    return os.path.join(product_dir, version)

def parse_argv(argv):
    parser = argparse.ArgumentParser(
                    description='''update link for module.''')
    parser.add_argument('--module', nargs=1, required=True,
                    help='''module to unpack.''')
    parser.add_argument('--product-dir', nargs=1,
                    help='''directory that contain all versions of product.''')
    parser.add_argument('--version', nargs=1)


    return parser.parse_args(argv)



if __name__ == '__main__':
    main()
