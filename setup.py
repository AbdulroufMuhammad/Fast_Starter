from setuptools import setup, find_packages

setup(
    name='fast_starter',  
    version='0.1.0',  
    packages=find_packages(),  
    entry_points={
        'console_scripts': [
            'fast-starter=fast_starter.main:main',  
        ],
    },
    install_requires=[
        'fastapi',
        'sqlalchemy',
        'pydantic',
        'alembic',
    ],
    description='A simple package to quickly set up a FastAPI project structure.',
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/fast_starter',  
    author='Your Name',  # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: FastAPI',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  
)
