# TradeJournal8

A modular, self-contained trading journal platform for tracking, masking, and analyzing financial statements.

---

## Overview

TradeJournal8 is a personal hobby project designed to securely manage trading data.  
It is built with modularity in mind, allowing independent development of components such as:

- CLI tools for masking sensitive information
- Processors for parsing statements and confirmations
- Storage services for organizing PDFs and parsed data
- Front-end dashboards (Angular default; React optional)
- Dockerized components for isolated development and deployment

The platform emphasizes **privacy, modularity, and flexibility**, making it easy to experiment with new components or features.

---

## Components

- **financialstatementsmaskercli** – CLI tool to mask sensitive info in statements.  
- **financialstatementsprocessor** – Parses statements and confirmations into structured JSON.  
- **tradestorage** – Stores PDFs and links parsed data.  
- **uiangular / uireact** – Front-end dashboards for visualizing and interacting with the data.  
- **docker** – Containerization of components for development or deployment.

> For a detailed overview of architecture, data flows, tech stack, and design decisions, see [ARCHITECTURE.md](ARCHITECTURE.md).

---

## Getting Started

Instructions for building, running, and contributing will be added here as the project evolves.  
Currently, the focus is on designing the architecture and core components.

---

## License

[Add license info here, if desired]
