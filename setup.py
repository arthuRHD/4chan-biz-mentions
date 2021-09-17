from setuptools import setup, find_packages

setup(
   name='4chan-biz-mentions',
   version='0.3.0',
   author='Arthur RICHARD',
   author_email='arthur.richard@protonmail.com',
   packages=find_packages(),
   url='https://boards.4channel.org/biz/catalog',
   description='Count the times a word is mentionned, can be used to track a shitcoin',
   long_description=open('README.md').read(),
   long_description_content_type='text/markdown'
)