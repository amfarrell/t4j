To set up environment:

Install miniconda:
download http://repo.continuum.io/miniconda/Miniconda-3.8.3-MacOSX-x86_64.sh
and run it to install miniconda.

Run `conda env create --name t4j --file ./local-environment.yml`
to install all the needed files into a virtual environment.
Run `source activate t4j` to activate that environment.

Run python manage.py runserver to run the local server.

