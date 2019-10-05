from distutils.core import setup

setup(
    name='backup',
    version='1.0',
    packages=[''],
    url='',
    license='',
    author='alexandr',
    author_email='',
    description='Бекап файлов и каталогов',
    entry_points={
        'console_scripts': [
            'backup-python-script = backup:main'
        ]
    }
)
