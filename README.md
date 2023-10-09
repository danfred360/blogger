# Enriched Logging Agent

> **Documentation**: For more detailed information, please refer to the [docs](./docs/index.md).

### Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)

## Overview

This project aims to build a Logstash ingestion agent that sends log events to a Graylog server. The logs are enriched with extra data generated using a Language Model (LLM) and context data gathered using available performance and reliability metrics. The project uses Python and is managed with Poetry. It also includes unit test coverage with pytest.

## Technologies Used

Below is a summary of the major technologies that are being leveraged in this project:

### [Python](https://www.python.org/doc/)

Python is the primary programming language used for this project. It offers a wide range of libraries and frameworks that make it easier to develop the agent.

### [Poetry](https://python-poetry.org/docs/)

Poetry is used for dependency management. It allows us to manage project dependencies in an isolated environment, making the project easier to maintain and share.

### [Langchain](#) 

Langchain is used for generating extra data using a Language Model (LLM). It helps in enriching the log data to provide more context and potentially diagnose issues. (Note: Replace with the actual documentation link for Langchain when available)

### [Graylog](https://docs.graylog.org/)

Graylog is an open-source log management platform. This project sends enriched log events to a Graylog server for further analysis and visualization.

### [pytest](https://docs.pytest.org/en/latest/)

pytest is used for writing unit tests for the project. It helps in maintaining the code quality and making sure that the functionalities work as expected.


