# pypackages

Script specific packages similar to PEP 582 using a `__pypackages__` directory.
The `__pypackages__` directory is created in the same directory as the script being executed.
A requirements.txt file must exist in the same folder to activate package installation.

## Intent

Avoid dependency conflicts when installing python command line utilities.

## Automatic requirements install

Place requirements.txt in the folder to install or upgrade on startup using pip.

This saves the need for distributing python version specific packages explicitly.

This also avoids the package having explicit dependencies that are installed along side
the package therefore creating the potential for package version conflicts.

## Activating

    import pypackages
    pypackages.packages()

Execute pypackages.packages() to perform a local installation of requirements.txt

## Pre-requisites

pip must already exist in the python environment if requirements.txt is used.

## Example setup.cfg

    [metadata]
    name = demo
    version = 1.0

    [options]
    packages =
        demo
    install_requires =
        pypackages

    [options.package_data]
    demo =
        *.txt

    [options.entry_points]
    console_scripts =
        demo = demo.app:cli


## Structure of deployment for scripts

    myapp.py
    pypackages/
        __init__.py
    requirements.txt

## Example (requirements.txt)

    sanic==22.12.0

## Example (myapp.py)

    #!/usr/bin/python
    import pypackages
    pypackages.packages()

    from sanic import Sanic
    from sanic.response import text

    app = Sanic('myapp')


    @app.route('/')
    async def hello(request):
        return text('Hello, world')


    if __name__ == '__main__':
        app.run(port=9999)

## References

https://peps.python.org/pep-0582/
