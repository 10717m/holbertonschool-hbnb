# High-Level Package Diagram - HBnB Evolution

This document contains the high-level package diagram for the HBnB Evolution project.  
The system follows a **three-layered architecture** with clear responsibilities assigned to each package.

---

## 🎯 Purpose

The goal of this diagram is to visualize the main packages and their dependencies.  
It shows how each layer communicates with the others, following a clean and modular structure.

---

## 📦 Package Diagram (Mermaid)

```mermaid
graph TD
    A[Presentation Layer] --> B[Business Logic Layer]
    B --> C[Persistence Layer]

    subgraph A [Presentation Layer]
        A1(UserController)
        A2(PlaceController)
        A3(ReviewController)
        A4(AmenityController)
    end

    subgraph B [Business Logic Layer]
        B1(UserService)
        B2(PlaceService)
        B3(ReviewService)
        B4(AmenityService)
    end

    subgraph C [Persistence Layer]
        C1(UserRepository)
        C2(PlaceRepository)
        C3(ReviewRepository)
        C4(AmenityRepository)
    end

    A1 --> B1
    A2 --> B2
    A3 --> B3
    A4 --> B4

    B1 --> C1
    B2 --> C2
    B3 --> C3
    B4 --> C4

