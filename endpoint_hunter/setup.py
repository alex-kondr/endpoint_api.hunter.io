from setuptools import setup, find_namespace_packages

setup(name='endpoint_hunter',
      version='1',
      description='endpoint_hunter',
      url='https://github.com/alex-kondr/endpoint_api.hunter.io',
      author='Alex Kondr',
      author_email='alex_kondr@outlook.com',
      license='MIT',
      packages=find_namespace_packages(),
      install_requires=['fastapi', 'uvicorn', 'pydantic', 'pydantic-settings', 'requests'],
      entry_points={'console_scripts': ['api_hunter = endpoint_hunter:main']}
      )