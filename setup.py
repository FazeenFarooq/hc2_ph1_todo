from setuptools import setup, find_packages

setup(
    name="todo_app",
    version="0.1.0",
    description="A simple CLI Todo application",
    author="Developer",
    author_email="developer@example.com",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'todo_app=src.todo_app:main',
        ],
    },
    python_requires='>=3.13',
    install_requires=[],
)