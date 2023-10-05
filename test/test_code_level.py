# UPDATE https://www.anaconda.com/blog/8-levels-of-reproducibility

import os
import datetime
import subprocess


def main():
    """
    Drawn from the research of Dr. Bednar holds a Ph.D. in Computer Science
    from the University of Texas, along with degrees in Electrical Engineering and Philosophy.

    All code should be able to be tested and give off a level to enable
    efficent running and optimal user experience
    :return:
    """
    # TODO test for /data exist
    # TODO test for /test exist
    # TODO test for /src or /source exist
    # TODO test for /data exist
    # TODO test for README.md exist
    # TODO test for .gitignore exist
    # TODO test for .env exist
    # TODO test for main exist
    # TODO test for requirements.txt exist
    # TODO test for setup.py exist
    # TODO test for setup.cfg exist
    # TODO test for __init__.py exist in how many folders
    # TODO test for *docker exist in folder
    # TODO test for mention of csv or flat files in data exist
    # TODO test for mentiom or links to database exist
    # TODO test for AWS, Oracle, Azure, or GoogleCloud exist


# Level 0: Your code ran and worked properly once.
def test_level_zero():
    """test cases that may fail when code is not reproducible.
    :return:
    """

    # TODO Check if a .pyc file exists.
    # TODO how to iterate through file_names to {file_name} as f script below

    script_name = "script_name.pyc"
    pyc_file_exists = os.path.isfile(f"{script_name}")

    # Check if the .pyc file was last modified before today.
    if pyc_file_exists:
        pyc_file_modified_time = datetime.datetime.fromtimestamp(
            os.path.getmtime(f"{script_name}")
        )
        today = datetime.datetime.today()
        modified_before_today = pyc_file_modified_time < today

    # Assert that both conditions are met.
    assert pyc_file_exists and modified_before_today
        elif:
            print("it looks like there is no .pyc file so chances are low")
    assert your_function() == expected_result


# Level 1: Your code currently runs, repeatably, in your initial environment.
def test_level_one():
    """Add test cases to ensure code runs in the same environment
        :return:
    """
    assert your_function() == expected_result


# Level 2: Reproducible by others with guidance (requirements.txt or
# environment.yml).
def test_level_two():
    """
    Ensure code can be reproduced by others using requirements.txt or environment.yml
    :return:
    """
    # TODO test that requirement file specified in requirements.txt or
    #  setup.py is installed
    assert your_function() == expected_result


# Level 3: Reproducible today, by anyone with internet access (
# anaconda-project or equivalent).
def test_level_three():
    """
    Ensure code can be reproduced by anyone with internet access
    :return:
    """
    # TODO test pip is installed
    # TODO test anaconda is installed or available
    assert your_function() == expected_result


# Level 4: Reproducible indefinitely, by anyone with internet access (fully
# locked project).
def test_level_four():
    """Ensure code can be reproduced indefinitely with a fully locked project
        :return:
    """
    assert your_function() == expected_result


# Level 5: Reproducible indefinitely, without depending on the internet (
# fully locked anaconda project).
def test_level_five():
    """Ensure code can be reproduced indefinitely without internet access
    :return:
    """
    assert your_function() == expected_result


# Level 6: Reproducible with Docker (Docker image).
def test_level_six():
    """Ensure code can be reproduced with Docker
        :return:
    """
    assert your_function() == expected_result


# Level 6: Reproducible with a virtual machine (VM image).
def test_level_seven():
    """Ensure code can be reproduced with a virtual machine
    :return:
    """
    assert your_function() == expected_result


# Level 8: Reproducible on untouched hardware (air-gapped physical hardware).
def test_level_eight():
    """Ensure code can be reproduced on untouched hardware
        :return:
    """
    assert your_function() == expected_result


# Example function to be tested.
def your_function():
    """Replace this with your actual code
        :return:
    """
    return result


# Example expected result.
expected_result = "Some expected result"

# Run the tests.
if __name__ == "__main__":
    test_level_zero()
    test_level_one()
    test_level_two()
    test_level_three()
    test_level_four()
    test_level_five()
    test_level_six()
    test_level_seven()
    test_level_eight()
