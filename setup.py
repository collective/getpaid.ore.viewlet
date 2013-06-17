from setuptools import setup, find_packages

setup(
    name="getpaid.ore.viewlet",
    version="0.2.3-getpaid",
    install_requires=[
        'setuptools',
        'zc.table >= 0.5'
    ],
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['getpaid'],
    package_data={
    '': ['*.txt', '*.zcml', '*.gif', '*.js', '*.pt'],
    },

    zip_safe=False,
    author='Kapil Thangavelu',
    author_email='info@objectrealms.net',
    description="""\
    These are some extensions of the base zope.viewlet model, preconstructed
    viewlets for container management, and new primitives like a private event
    channel, and private annotation storage on the viewlet manager,
    multipage/wizard viewlets, and formlib viewlets.
    """,
    long_description=open('CHANGES.txt').read(),
    license='GPL',
    keywords="zope zope3",
    )
