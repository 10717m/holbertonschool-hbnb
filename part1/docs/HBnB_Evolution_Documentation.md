# 🏠 HBnB Evolution - Technical Documentation

## 📌 Introduction

This document presents a complete technical overview of the **HBnB Evolution** project. It includes three core elements:

- High-Level Package Diagram
- Detailed Class Diagram for the Business Logic Layer
- Sequence Diagrams for API Calls

The objective is to provide a clear, professional blueprint that guides the implementation process and serves as a reference for system architecture.

---

## 📦 1. High-Level Architecture

```mermaid
graph TD
    A[Presentation Layer] --> B[Business Logic Layer]
    B --> C[Persistence Layer]
    B -->|Uses| D[Facade]

