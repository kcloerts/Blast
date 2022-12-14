.. blast documentation master file, created by
   sphinx-quickstart on Thu Dec 23 12:02:23 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to blast's documentation!
=================================

.. image:: https://readthedocs.org/projects/blast/badge/?version=latest
.. image:: https://github.com/astrophpeter/blast/actions/workflows/continuous-integration.yml/badge.svg
.. image:: https://results.pre-commit.ci/badge/github/astrophpeter/blast/main.svg

Blast is a Django web app for the automatic characterization of supernova hosts.
Blast is developed on `github <https://github.com/astrophpeter/blast>`_.

Using the web interface
-----------------------

.. toctree::
   :maxdepth: 2
   :caption: Web interface

   web_pages
   web_api

Developer Guide
---------------

.. toctree::
   :maxdepth: 2
   :caption: Developer Guide

   dev_getting_started
   dev_running_blast
   dev_system_pages
   dev_workflow
   dev_overview_of_repo
   dev_github_issues
   dev_documentation
   dev_task_runner


Code API
--------

.. toctree::
   :maxdepth: 2
   :caption: Code API

   API/models
   API/transient_name_server
   API/base_tasks
