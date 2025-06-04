# HBnB Evolution - High-Level Architecture Documentation

## Overview

This document outlines the high-level architecture of the HBnB Evolution application.  
The system is built using a **three-layered architecture** pattern, promoting separation of concerns, maintainability, and scalability.

---

## 🧱 Architecture Layers

### 1. Presentation Layer (API / Services)
- Exposes HTTP APIs to end users.
- Responsible for input validation, request parsing, and response formatting.
- Forwards requests to the Business Logic Layer via **facade interfaces**.

**Components:**
- UserController
- PlaceController
- ReviewController
- AmenityController

---

### 2. Business Logic Layer (Models / Services)
- Contains the core domain logic and business rules.
- Encapsulates application-specific rules and data flow.
- Implements the **Facade Pattern** to serve as the single point of communication with the Presentation Layer.

**Entities:**
- UserService
- PlaceService
- ReviewService
- AmenityService

**Models:**
- User
- Place
- Review
- Amenity

---

### 3. Persistence Layer (Repositories / Database Access)
- Handles storage and retrieval of data from the database.
- Implements data access logic in the form of Repositories (DAOs).
- Each service from the Business Logic Layer communicates with its related repository.

**Components:**
- UserRepository
- PlaceRepository
- ReviewRepository
- AmenityRepository

---

## 🔁 Layered Communication (Facade Pattern)

The application uses the **Facade Pattern** between the Presentation Layer and Business Logic Layer.  
This pattern simplifies the interface and ensures loose coupling between layers.

```mermaid
classDiagram
class PresentationLayer {
    <<interface>>
    +UserController
    +PlaceController
    +ReviewController
    +AmenityController
}
class BusinessLogicLayer {
    +UserService
    +PlaceService
    +ReviewService
    +AmenityService
}
class PersistenceLayer {
    +UserRepository
    +PlaceRepository
    +ReviewRepository
    +AmenityRepository
}

PresentationLayer --> BusinessLogicLayer : Uses (via Facade Pattern)
BusinessLogicLayer --> PersistenceLayer : Database Access

