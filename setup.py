from distutils.core import setup, Extension

# exec this file by command : python setup.py build
# then .c files will be compiled and located in ./build/

module1 = Extension('demo',
                    sources=['src/ccc.c'])

setup(name='PackageName',
      version='1.0',
      description='This is a demo package',
      ext_modules=[module1])
