from setuptools import setup

setup(
    name='test_plaid_webapp',
    version='1.0.0',
    install_requires=[
        'requests',
        'falcon',
        'httpie',
        'pytest',
        'plaid-python'
    ]
)
