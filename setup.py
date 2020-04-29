import setuptools

def readme():
	with open('README.md') as f:
		README = f.read()
	return README

setuptools.setup(
	name='hungarian_algorithm',
	version='0.1.9',
	author='Ben Chaplin',
	author_email='benchaplin@protonmail.ch',
	description='Python 3 implementation of the Hungarian Algorithm for the assignment problem.',
	long_description=readme(),
	long_description_content_type='text/markdown',
	url='https://github.com/benchaplin/hungarian-algorithm',
	packages=setuptools.find_packages(),
	classifiers=['Programming Language :: Python :: 3',
				 'License :: OSI Approved :: MIT License',
				 'Operating System :: OS Independent'
				 ]
) 
