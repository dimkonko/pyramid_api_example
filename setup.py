from setuptools import setup, find_packages

ENTRY_POINT = """
[paste.app_factory]
main=pyramid_api_example:main
"""

REQUIREMENTS = [
    'pyramid',
    # 'SQLAlchemy'
]

TESTS_REQUIRE = [
    'WebTest >= 1.3.1',  # py3 compat
]


def get_version():
    return "0.0"


setup(
    name="pyramid_api_example",
    version=get_version(),
    description="pyramid_api_example description",
    long_description="""'
    pyramid_api_example long description
    """,
    classifiers=[
        "Programming Language :: Python",
        'Framework :: Pylons',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application'],
    author="Dmytro Karacheban",
    author_email="d.karacheban@gmail.com",
    url="",
    license="asdf",
    keywords='web wsgi pylons pyramid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite="pyramid_api_example",
    install_requires=REQUIREMENTS,
    extras_require={
        'tests': TESTS_REQUIRE,
    },
    entry_points=ENTRY_POINT
)
