from setuptools import setup


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    # name="housing_value_prediction",
    # version="0.2",
    # install_requires=["scikit-learn>=1.0.2", "pandas>=1.5",],
    # dependency_links=[],
    # description="Predict house value",
    # url="http://github.com/roshande-tiger/mle-training",
    # author="Roshan Hande",
    # author_email="roshan.hande@tigeranalytics.com",
    # license="MIT",
    # packages=["src"],
    zip_safe=False,
)
