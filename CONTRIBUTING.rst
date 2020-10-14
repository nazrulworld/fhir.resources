.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/nazrulworld/fhir.resources/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

fhir.resources could always use more documentation, whether as part of the
official fhir.resources docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/nazrulworld/fhir.resources/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `fhir.resources` for local development.

1. Fork the `fhir.resources` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/fhir.resources.git

3. Install your local copy into a virtualenv. Assuming you have pipenv installed
   (but don't worry you could use simply virtualenv and install from ``requirements_dev.txt ),
   this is how you set up your fork for local development::

    $ cd fhir.resources/
    $ pipenv install --dev

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox::

    $ flake8 fhir.resources tests
    $ python setup.py test or py.test
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 2.7, 3.4, 3.5 and 3.6, and for PyPy. Check
   https://travis-ci.org/nazrulworld/fhir.resources/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

$ py.test tests.test_fhir.resources


Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

$ bumpversion patch # possible: major / minor / patch
$ git push
$ git push --tags

Travis will then deploy to PyPI if tests pass.


Adding a new resource
---------------------

Adding a new resource should be done under the relevant directory.
For R4, the directory is `fhir/resources/` and for DSTU2 and STU3 the
directories are `fhir/resources/DSTU2/` and `fhir/resources/STU3/`.

After adding you resource, you need to add it to couple of additional places:
1. `fhirtypes.py` in the FHIR version your resource belongs to. This includes
   both the reource and the inner elements you created for it.
2. Add relevant entries inside the list `MODEL_CLASSES` at
   `fhirtypesvalidators.py`. Probably you will need to add
   `(None, .your_resource_module_name)`.
3. Add validator functions in `fhirtypesvalidators.py` for both your resource
   and the inner resources you created.
4. Add the validator methods you created to the list at the bottom of the file.

Lastly, add your tests into the `tests` directory inside the relevant directory
where you created your resource.
