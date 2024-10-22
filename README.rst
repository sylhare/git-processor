Git Processor
=============

A git log processor for better stats.
Made to be used on one or multiple Git repositories

View the demo `git processor demo <https://sylhare.github.io/git-processor/>`_.


Setup
-----

Install the library with:

.. code:: bash

    # From pypi
    python3 -m pip install git_processor


To use it, run the ``generate_git_logs.sh`` in where you have all your repository.
It will create a ``stats.txt`` file.

.. code:: python

    import os
    from git_processor.data import Projects

    p = Projects(os.path.abspath("stats.txt"))  # Process the git log stats
    p.clean_up_names()                          # Get all similar names as one
    p.df                                        # Get the created dataframe
    p.total()                                   # Total commits per user



Let's use jupyter to display the information.

.. code:: bash

    pyhton3 -m pip install jupyter
    cd jupyter/
    jupyter notebook

Once you are in the jupyter notebook, you can display the data and plot the stats.
Check in the ``jupyter/`` folder, you can reuse the demo and get your stats in one go.
Just click on ``Run All Cell``, or go along with [shift] + [enter] to run them individually.


Testing
-------

To find out more info about the testing configuration, check out the
``tox.ini`` file.

.. code:: bash

   # Run the test suite
   tox
   # Run the linter:
   tox -e lint


Local Installation
------------------

Using a virtual environment:

.. code:: bash

    # From pypi
    python3 -m pip install virtualenv

Then set it up and install the package locally

.. code:: bash

   # Create the virtual environment
   python3 -m venv `pwd`/env
   # Activate it
   source env/bin/activate
   # Install from local
   (env) python3 -m pip install .
   
   
Other Git Processors
--------------------

Here is a list of other python git processors. (Usually meant for one repository)

- `hercules <https://github.com/src-d/hercules>`_
- `git-of-theseus <https://github.com/erikbern/git-of-theseus>`_



