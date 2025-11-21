# 🧩 Simple Full-Stack Application – Architecture Overview

## 1. Overview
This repository contains a **full-stack web application** built with:
- **Frontend:** React (Next.js)
- **Backend:** FastAPI
- **Database:** PostgreSQL
- **Environment:** Docker-based local development setup

The application provides a foundation for modern web app development using an **API-first architecture**, ensuring clean separation of concerns between the UI, backend services, and data layer.

---

## 2. Goals
- Provide a minimal but extensible full-stack example
- Enable local development with Docker Compose
- Serve as a reference for integrating React (Next.js) with FastAPI
- Offer a foundation for CI/CD automation and cloud deployment

---

## 3. High-Level Architecture

```plaintext
┌────────────────────────┐
│        Frontend         │
│  Next.js (React)        │
│  Static Pages + API Calls│
└───────────┬────────────┘
            │ REST API (HTTP)
┌───────────▼────────────┐
│        Backend          │
│   FastAPI (Python)      │
│   Business Logic & CRUD  │
└───────────┬────────────┘
            │ SQLAlchemy ORM
┌───────────▼────────────┐
│       Database          │
│   PostgreSQL            │
│   Persistent Storage     │
└────────────────────────┘
```
