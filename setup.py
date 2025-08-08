import setuptools

with open("README.md",'r',encoding='utf-8') as f:
    long_description=f.read()

__version__="0.0.0"

repo_name='chest_cancer_mlflow_DVC'
author_user_name='itsalok2'
src_repo='cnnClassifier'
author_email='harin3419@gmail.com'

setuptools.setup(
    name=repo_name,
    version=__version__,
    author=author_user_name,
    author_email=author_email,
    description='A small python package for CNN app',
    long_description=long_description,
    url=f"https://github.com/{author_user_name}/{repo_name}",
    project_url={
        "Bug Tracker": f"https://github.com/{author_user_name}/{repo_name}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)