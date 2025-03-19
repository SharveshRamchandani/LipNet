from setuptools import setup

setup(name='lipnet',
    version='0.1.6',
    description='End-to-end sentence-level lipreading',
    url='http://github.com/rizkiarm/LipNet',
    author='Muhammad Rizki A.R.M',
    author_email='rizki@rizkiarm.com',
    license='MIT',
    packages=['lipnet'],
    zip_safe=False,
    install_requires=[
        'tensorflow>=2.0.0',
        'numpy>=1.19.2',
        'opencv-python>=4.5.1',
        'scipy>=1.6.0',
        'dlib>=19.21.0',
        'h5py>=3.1.0',
        'keras>=2.4.3',
        'editdistance>=0.3.1',
        'matplotlib>=2.0.0',
        'python-dateutil>=2.6.0',
        'Pillow>=4.1.0',
        'nltk>=3.2.2',
        'sk-video>=1.1.7'
    ])
