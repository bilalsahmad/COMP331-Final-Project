{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOHN8dYqKIT3vIW3zP/k2de"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-S9dV6JFJe2C",
        "outputId": "2973e51e-e494-4a48-8e1a-84e00cb31a4e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: ucimlrepo in /usr/local/lib/python3.12/dist-packages (0.0.7)\n",
            "Requirement already satisfied: pandas>=1.0.0 in /usr/local/lib/python3.12/dist-packages (from ucimlrepo) (2.2.2)\n",
            "Requirement already satisfied: certifi>=2020.12.5 in /usr/local/lib/python3.12/dist-packages (from ucimlrepo) (2025.11.12)\n",
            "Requirement already satisfied: numpy>=1.26.0 in /usr/local/lib/python3.12/dist-packages (from pandas>=1.0.0->ucimlrepo) (2.0.2)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas>=1.0.0->ucimlrepo) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas>=1.0.0->ucimlrepo) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas>=1.0.0->ucimlrepo) (2025.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas>=1.0.0->ucimlrepo) (1.17.0)\n",
            "Null values per column:\n",
            "age                 0\n",
            "workclass         963\n",
            "fnlwgt              0\n",
            "education           0\n",
            "education-num       0\n",
            "marital-status      0\n",
            "occupation        966\n",
            "relationship        0\n",
            "race                0\n",
            "sex                 0\n",
            "capital-gain        0\n",
            "capital-loss        0\n",
            "hours-per-week      0\n",
            "native-country    274\n",
            "dtype: int64\n",
            "\n",
            "Percentage of nulls per column:\n",
            "age               0.00\n",
            "workclass         2.96\n",
            "fnlwgt            0.00\n",
            "education         0.00\n",
            "education-num     0.00\n",
            "marital-status    0.00\n",
            "occupation        2.97\n",
            "relationship      0.00\n",
            "race              0.00\n",
            "sex               0.00\n",
            "capital-gain      0.00\n",
            "capital-loss      0.00\n",
            "hours-per-week    0.00\n",
            "native-country    0.84\n",
            "dtype: float64\n"
          ]
        }
      ],
      "source": [
        "!pip install ucimlrepo\n",
        "import pandas as pd\n",
        "from ucimlrepo import fetch_ucirepo\n",
        "\n",
        "# Fetch dataset\n",
        "adult = fetch_ucirepo(id=2)\n",
        "X = adult.data.features\n",
        "\n",
        "# Count null values per column\n",
        "null_counts = X.isna().sum()\n",
        "\n",
        "# Print results\n",
        "print(\"Null values per column:\")\n",
        "print(null_counts)\n",
        "\n",
        "# Hard coded because of duplicated values.\n",
        "null_percent = (null_counts / 32509) * 100\n",
        "print(\"\\nPercentage of nulls per column:\")\n",
        "print(null_percent.round(2))\n"
      ]
    }
  ]
}