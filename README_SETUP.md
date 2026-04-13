# Setup Guide

This guide explains how to configure and run the examples in this repository.

## Prerequisites

- Python 3.11+ installed
- Conda installed (Anaconda or Miniconda)
- Access to OCI Generative AI OpenAI-compatible endpoint
- A valid OCI API key and project ID

## 1. Create and activate a Conda environment

```bash
conda create -n oci_deep_agents python=3.11 -y
conda activate oci_deep_agents
```

## 2. Install Python libraries

```bash
pip install --upgrade pip
pip install langchain-openai python-dotenv
```

## 3. Configure environment variables

Create a `.env` file in the project root with the following variables:

```dotenv
OCI_API_KEY=your_api_key_here
OCI_BASE_URL=https://inference.generativeai.<region>.oci.oraclecloud.com/20231130/openai/v1
OCI_MODEL_NAME=openai.gpt-5.4
OCI_PROJECT_ID=your_project_ocid_here
```

Variable details:

- `OCI_API_KEY`: API key used to authenticate requests
- `OCI_BASE_URL`: OCI OpenAI-compatible endpoint base URL
- `OCI_MODEL_NAME`: model identifier to use for inference
- `OCI_PROJECT_ID`: OCI Generative AI project OCID

## 4. Run the first example

```bash
python test01.py
```

If the configuration is correct, the script prints a model response in the terminal.

## Notes

- `.env` is already ignored by Git in this repository.
- Keep credentials private and never commit real secrets.
