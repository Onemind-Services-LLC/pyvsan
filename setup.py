import re
import ast

from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('src/vmware/vsan/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1))
    )

setup(
    name='pyvsan',
    version=version,
    description='VMware vSAN SDK for Python',
    long_description=open('README.md').read(),
    author='VMware, Inc.',
    author_email='unknown@vmware.com',
    maintainer='Abhimanyu Saharan',
    maintainer_email='asaharan@onemindservices.com',
    license='BSD',
    url='https://code.vmware.com/apis/1188/vsan',
    download_url='https://code.vmware.com/apis/1188/vsan',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    project_urls={
        'Documentation': 'https://code.vmware.com/apis/1188/vsan',
        'Download': 'https://developer.vmware.com/web/sdk/7.0%20U3/vsan-python',
    },
    scripts=[
        'src/vsanapisamples',
        'src/vsaniscsisamples',
    ],
    install_requires=[
        'pyvmomi >= 7.0.3',
    ]
)
