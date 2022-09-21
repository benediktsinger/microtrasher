import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='micro_trasher',
    version='0.0.3',
    author='Benedikt Singer',
    author_email='benedikt.singer@ist.ac.at',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://git.ist.ac.at/bsinger/microprev',
    project_urls = {
        "Bug Tracker": "https://git.ist.ac.at/bsinger/microprev/-/issues"
    },
    license='MIT',
    packages=['micro_trasher'],
    install_requires=[
        "mrcfile >= 1.3.0",
        "numpy >= 1.23.1",
        "Pillow >= 9.2.0"
    ],
)