from setuptools import setup

def readme():
	with open('README.md') as f:
		README = f.read()
	return README

setup(
	name='hungarian-algorithm',
	version='0.1',
	description='Python 3 implementation of the Hungarian Algorithm (a.k.a. the Kuhn-Munkres algorithm), an O(n^3) solution for the assignment problem, or maximum-weighted bipartite matching problem.',
	long_description=readme(),
	long_description_content_type='text/markdown',
	url='https://github.com/benchaplin/hungarian-algorithm',
	classifiers=['Programming Language :: Python :: 3',
				'Programming Language :: Python :: 3.7'],
	pymodules=['graph'],
	include_package_data=True,
	package_dir={'': 'src'}
) 
