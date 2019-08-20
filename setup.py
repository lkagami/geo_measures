import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='geo_measures',  

     version='0.1',

     author="Luciano Porto Kagami",

     author_email="lucianopkagami@hotmail.com",

     description="The 'Geometric Measures' script that was developed to carry out geometric analysis on protein structures.",

     long_description=long_description,

     long_description_content_type="text/markdown",

     url="https://github.com/lkagami/geo_measures",

     packages=setuptools.find_packages(),

     entry_points={'console_scripts': ['geo_measures = geo_main:call_main']},

     classifiers=[

         "Programming Language :: Python :: 3.7",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],
    install_requires=['biopandas==0.2.5','biopython==1.74','numpy==1.17.0','pandas==0.25.0','Pillow==6.1.0','PyQt5==5.13.0','PyQt5-sip==4.19.18','scipy==1.3.1',
      ],
    zip_safe=False

 )