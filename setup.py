from setuptools import find_packages, setup


setup(name="cfxgb",
      version="1.0.0",
      description="The official implementation of CFXGB : Cascaded Forest and XGBoost Classifier",
      author="Surya Dheeshjith",
      author_email='Surya.Dheeshjith@gmail.com',
      platforms=["any"],
      url="https://github.com/suryadheeshjith/CFXGB",
      packages=["cfxgb", "cfxgb.lib","cfxgb.lib.cascade","cfxgb.lib.estimators","cfxgb.lib.utils"],
      package_dir={"": "src"},
      install_requires=[
            "numpy==1.22.0",
            "pandas==1.2.3",
            "joblib==1.0.1",
            "psutil==5.8.0",
            "scikit-learn==0.24.1",
            "imblearn==0.0",
            "scipy==1.6.1"
            ],
        extras_require={
            "testing": ["pytest-cov"]
      }

)
