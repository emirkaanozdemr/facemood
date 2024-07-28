from setuptools import setup, find_packages

setup(
    name='facemood',
    version='1.0.0',
    author='Emir Kaan Özdemir',
    author_email='emirkaanbulut08@gmail.com',
    description='A library for emotion prediction from camera input.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/emirkaanozdemr/facemood',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'opencv-python',
        'Pillow',
        'numpy',
        'tensorflow',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='Apache License 2.0'
)
