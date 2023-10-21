"""
Tests for `{{ cookiecutter.repo_name }}` module.
"""
import pytest
from {{ cookiecutter.package_name }} import {{ cookiecutter.package_name }}


class Test{{ cookiecutter.package_name|capitalize }}(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_something(self):
        pass

    @classmethod
    def teardown_class(cls):
        pass
