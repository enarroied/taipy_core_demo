# TAIPY Core demo app

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue.svg)

## What is this app?

This is a minimal app to test Taipy Core.

📚 I used this demo to write [a Medium article about how to use Taipy Core](https://medium.com/gitconnected/how-to-use-taipy-core-build-pipelines-for-better-applications-%EF%B8%8F-d40e5bc9aed3). 📚

I used Taipy 2.3 to build it.

File structure:

* mock_config_file: this is just a mock toml with no functionality
* src
  * config
  * data
  * page
  * main.py

## Data sources

You can find the dataset [in my Kaggle page](https://www.kaggle.com/datasets/ericnarro/volumes-wine-production-aoc-2009-2019).

The origincal source data is a [pdf file by France Agrimer](https://www.franceagrimer.fr/fam/content/download/62836/document/chiffres-fili%C3%A8re-viti-vinicole-2008-2018.pdf?version=).

You can find the process I followed to create the CSV file [in my blog's article about it](https://www.ericnarrodata.com/blog/2023/pdf_table_wine_production.html).
