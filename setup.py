from setuptools import setup, find_packages

setup(
    name='py-res',
    version='1.0',
    description='Python solution for room reservation',
    author='Ayesh Jayasekara',
    author_email='cim12137@ciom.edu.au',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'PyInquirer',
        'bcrypt',
        'setuptools',
        'rich',
        'importlib-metadata; python_version<"3.10"',
    ]
)

# ~=1.0.3
# bcrypt~=4.3.0
# setuptools~=68.2.0
# rich~=14.0.0
# )
