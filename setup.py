from setuptools import setup

setup(
    name='Data_Bench',
    version='0.0.2',
    packages=['requests', 'ipython', 'beautifulsoup4',
              'google.cloud', 'sqlalchemy', 'pandas',
              'numpy', 'numba', 'tqdm',
              'scipy', 'numba', 'scipy',
              'matplotlib', 'streamlit', 'mysqlclient',
              'mysql', 'plotly'],
    url='',
    license='MIT',
    author='Andrew Schell',
    author_email='paintstone@gmail.com',
    description='a workbench for data science tools and databases'
)

if __name__ == "__main__":
    setup()