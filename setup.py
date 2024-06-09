from setuptools import setup, find_packages

setup(
   name='MobileDogs_API',
   version='1.0',
   description='Provides an API service for managing homeless dogs',
   license='MIT',
   author='Tetsushiro, Dasha Sisimirova',
   author_email='AlhemyD@mail.ru',
   url='https://github.com/Deppkepa/MobileDogs_API.git',
   packages=find_packages(), 
   install_requires=['fastapi','uvicorn'],
   extras_require={'test': [
            'pytest'
        ],
   },
   python_requires='>=3',
)
