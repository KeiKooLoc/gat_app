.. quickstart:

Quickstart
==========

A Python app, which follows README description.
Application UI based on MDB Free and EBM Bootstrap Plugin, available under MIT License and provided by `MDBoostrap.com <https://mdbootstrap.com>`_.


Running Locally
---------------

It can be run locally. Make sure you have Python_ installed ::

    $ git clone https://github.com/mdyzma/gat_app.git
    $ cd gat_app
    $ pip install --no-cache-dir -r requirements.txt
    $ python manage.py runserver

Your app should now be running on `http://127.0.0.1:5000 <http://localhost:5000/>`_.

It can be also deployed to tone of the popular deployment services like HEROKU.

Testing
-------

To test app run `manage.py` with specific command. In case of testing it is::
    
    $ python manage.py test
    python manage.py test
    [2018-07-09 21:40:42,651] DEBUG in app: Debug toolbar activated
    ============================= test session starts =============================
    platform win32 -- Python 3.6.5, pytest-3.5.0, py-1.5.3, pluggy-0.6.0 -- C:\Users\Alicja\Anaconda3\python.exe
    cachedir: .pytest_cache
    rootdir: F:\praca2018\procesy_rekrutacyjne\05-06-2018-GAT-Dynaminds\gat_app, inifile:
    plugins: remotedata-0.2.0, openfiles-0.2.0, doctestplus-0.1.2, cov-2.5.1, arraydiff-0.2
    collected 15 items
    tests/webapp/test_app.py::test_base_panel_calculate_price PASSED         [  6%]
    tests/webapp/test_app.py::test_panel_one_url PASSED                      [ 13%]
    tests/webapp/test_app.py::test_panel_two_url PASSED                      [ 20%]
    tests/webapp/test_app.py::test_panel_three_url PASSED                    [ 26%]
    tests/webapp/test_app.py::test_panel_one_price PASSED                    [ 33%]
    tests/webapp/test_app.py::test_panel_three_price PASSED                  [ 40%]
    tests/webapp/test_config.py::test_production_config PASSED               [ 46%]
    tests/webapp/test_config.py::test_dev_config PASSED                      [ 53%]
    tests/webapp/test_config.py::test_testing_config PASSED                  [ 60%]
    tests/webapp/test_panels.py::test_base_panel_calculate_price PASSED      [ 66%]
    tests/webapp/test_panels.py::test_panel_one_url PASSED                   [ 73%]
    tests/webapp/test_panels.py::test_panel_two_url PASSED                   [ 80%]
    tests/webapp/test_panels.py::test_panel_three_url PASSED                 [ 86%]
    tests/webapp/test_panels.py::test_panel_one_price PASSED                 [ 93%]
    tests/webapp/test_panels.py::test_panel_three_price PASSED               [100%]
    ========================== 15 passed in 3.40 seconds ==========================



Sometimes it is necessary to remove temporary files. `manage.py` provides handy tool to clean temporary test files usin this command::
    
    $ python manage.py clean
    [2018-07-09 21:49:42,832] DEBUG in app: Debug toolbar activated
    Removing .\webapp\__pycache__\__init__.cpython-36.pyc   
    Removing .\webapp\__pycache__\app.cpython-36.pyc
    Removing .\webapp\__pycache__\settings.cpython-36.pyc
    Removing .\webapp\__pycache__\panels.cpython-36.pyc
    Removing .\tests\webapp\__pycache__\test_app.cpython-36-PYTEST.pyc
    Removing .\tests\webapp\__pycache__\test_config.cpython-36-PYTEST.pyc
    Removing .\tests\webapp\__pycache__\test_panels.cpython-36-PYTEST.pyc


Documentation
-------------


To create documentartion enter `.docs` folder and type ::
    
    $ make html
    Running Sphinx v1.7.5
    loading pickled environment... done
    building [mo]: targets for 0 po files that are out of date
    building [html]: targets for 1 source files that are out of date
    updating environment: 0 added, 1 changed, 0 removed
    reading sources... [100%] quickstart
    looking for now-outdated files... none found
    pickling environment... done
    checking consistency... done
    preparing documents... done
    writing output... [100%] quickstart
    generating indices... genindex
    writing additional pages... search
    copying static files... done
    copying extra files... done
    dumping search index in English (code: en) ... done
    dumping object inventory... done
    build succeeded.


The HTML pages are in build/html.

.. links

.. _Python: http://install.python-guide.org