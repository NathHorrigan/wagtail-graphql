from setuptools import setup, find_packages

setup(
    name='wagtail-graphql',
    version='0.1.0',
    description='',
    author='Tiago Requeijo',
    author_email='tiago.requeijo.dev@gmail.com',
    url='https://github.com/tr11/wagtail-graphql',
    install_requires=[
        'graphene_django==2.2',
        'graphene_django_optimizer==0.3.5',
        'wagtail==2.3',
        'wagtailmenus==2.12'
    ],
    packages=find_packages(),
)
