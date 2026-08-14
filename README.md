# VaultX AI Internship

## Week 01 – AI Foundations & Environment

This repository contains my work for **Week 01 of the VaultX CyberTech AI Internship**, focused on building a foundation in Python environments, Large Language Models, API integration, and practical LLM application development.

### Topics Covered

- Python virtual environments and project setup
- LLM fundamentals and terminology
- API integration with Gemini
- Tokens and context windows
- Generation parameters and temperature experiments
- Git and GitHub workflow
- Reusable LLM API wrapper
- Error handling, retries, and timeouts
- CLI-based text summarization and sentiment analysis

### Week 01 Work

#### 1. AI Terminology Glossary
Created a glossary covering key LLM concepts including:

- Tokens
- Context windows
- Temperature
- Top-p
- System prompts
- Embeddings
- Hallucinations
- Fine-tuning
- Inference
- Base models vs. instruction-tuned models

#### 2. API Integration
Implemented a first API call using Gemini and recorded token usage for the generated response.

#### 3. Generation Parameter Experiment
Experimented with temperatures **0, 0.7, and 1.0**, running each setting multiple times to observe how temperature affects output variation.

#### 4. Reusable LLM API Wrapper
Built a reusable Python API wrapper supporting:

- Message generation
- Retry handling
- Request timeouts
- Token usage tracking
- API error handling
- Invalid input handling
- Invalid API key handling

#### 5. CLI Summarization Tool
Built a command-line tool that accepts text through:

- Direct command-line input
- Text files
- Interactive file-path input

The tool generates:

- A summary
- Key points
- Sentiment

### Project Structure

```text
week-01/
├── experiments/
├── glossary/
├── samples/
│   ├── input1.txt
│   ├── input2.txt
│   └── input3.txt
├── src/
│   ├── api_wrapper.py
│   ├── cli_summarizer.py
│   ├── first_api_call.py
│   ├── test_api_wrapper.py
│   └── test_error_handling.py
└── README.md