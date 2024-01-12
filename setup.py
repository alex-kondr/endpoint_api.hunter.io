from setuptools import setup

setup(name='endpoint_hunter',
      version='1',
      description='endpoint_hunter',
      url='https://github.com/alex-kondr/endpoint_api.hunter.io',
      author='Alex Kondr',
      author_email='alex_kondr@outlook.com',
      license='MIT',
      install_requires=['fastapi', 'uvicorn', 'pydantic', 'pydantic-settings', 'requests'],
      entry_points={'console_scripts': ['api_hunter = endpoint_api_hunter_io.main:start']}
      )