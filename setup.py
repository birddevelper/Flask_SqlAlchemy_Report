from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='flask_sqlalchemy_report',
    version='0.1.7',
    description='A useful simple to use tool to turn your sql query into a beautiful report html table',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='GNU',
    packages=find_packages(),
    author='M.Shaeri',
    
    keywords=['Flask', 'sqlAlchemy', 'Report', 'HTML', 'Table', 'SQL'],
    url='https://github.com/birddevelper/Flask_SqlAlchemy_Report',
    download_url='https://pypi.org/project/Flask_SqlAlchemy_Report/'
)

install_requires = [
    'flask', 'flask_sqlalchemy'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)