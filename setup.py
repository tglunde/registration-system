from setuptools import find_packages, setup

setup(
    name='registration',
    version='1.0.0',
    scripts=['registration'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask_mail',
        'flask_sqlalchemy',
        'validate_email',
        'py3DNS',
    ],
)
