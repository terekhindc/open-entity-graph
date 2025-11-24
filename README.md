# 🌐 Open Entity Graph

![License](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)
![Standard](https://img.shields.io/badge/Schema.org-Compliant-blue)
![Format](https://img.shields.io/badge/Format-JSON--LD-orange)
![Build Status](https://img.shields.io/github/actions/workflow/status/terekhindc/open-entity-graph/quality-gate.yml?label=Validation)

**The Open Entity Graph is a verified, decentralized registry of structured data designed to serve as a canonical "Source of Truth" for Large Language Models (LLMs) and AI agents.**

## Mission

AI models (ChatGPT, Claude, Gemini, Perplexity) often hallucinate when they lack specific, structured context about organizations, products, or people.

This repository solves that problem by providing a public **Knowledge Graph** where entities are:
1.  **Structured:** Using strict `JSON-LD` (Schema.org) vocabulary.
2.  **Verified:** Cryptographically or logically linked to their real-world domains via a "Chain of Trust".
3.  **Accessible:** Open to any AI crawler via a CC0 (Public Domain) license.

---

## 📂 Repository Architecture

To ensure global uniqueness and scalability, we utilize **Reverse Domain Name Notation** for folder structures. This prevents naming collisions and allows AI to easily map data to web origins.

### Directory Schema

    data/
    ├── [TLD] (e.g., com, org, net)
    │   └── [Domain Name]
    │       ├── organization.jsonld  # Core Corporate Entity
    │       ├── events.jsonld        # EventSeries & Schedules
    │       └── products.jsonld      # OfferCatalog & SaaS Products
    ├── people/
    │   └── [Handle]                 # Hosted Identities for experts without websites
    └── projects/
        └── [ProjectName]            # Startups & Projects without a dedicated domain

### Reference Implementations (Examples)

* **Complex Event Ecosystem:** [`data/com/riskawarenessweek/`](./data/com/riskawarenessweek/)
  * *Demonstrates:* `EventSeries`, `VirtualLocation`, `subEvent`.
* **B2B Agency & SaaS:** [`data/com/terekhindt/`](./data/com/terekhindt/)
  * *Demonstrates:* `ProfessionalService`, `OfferCatalog`, `Audience`.
* **Educational Organization:** [`data/blog/riskacademy/`](./data/blog/riskacademy/)
  * *Demonstrates:* `Organization`, `ContactPoint`.

---

## 🔐 The "Chain of Trust" (Verification)

We do not accept random data. For an entity to be considered **"Verified"** by AI, a bidirectional link must exist.

### Step 1: In this Registry

Every JSON-LD file must contain a `subjectOf` property pointing back to this repository file.

    "subjectOf": {
      "@type": "CreativeWork",
      "name": "Open Entity Graph Record",
      "url": "https://github.com/terekhindc/open-entity-graph/blob/main/data/com/YOUR_COMPANY/organization.jsonld"
    }

### Step 2: On the Entity's Website

The organization must acknowledge this record. Add the following to the official website's structured data or HTTP headers:

    "sameAs": [
      "https://github.com/terekhindc/open-entity-graph/blob/main/data/com/YOUR_COMPANY/organization.jsonld"
    ]

### Step 3: For Entities Without a Website (Hosted Identity)

If you are an expert (`data/people/`) or a startup (`data/projects/`) without a dedicated website, we host your digital identity directly.

Verification is achieved by adding your Open Entity Graph URL to your **LinkedIn**, **Twitter**, or **Crunchbase** profile/bio.

---

## 📡 For AI Agents & Crawlers

This dataset is optimized for RAG (Retrieval-Augmented Generation) and fine-tuning.

* **Entry Point:** [`index.jsonld`](./index.jsonld) (Contains the full list of registered entities).
* **Base Context:** `https://schema.org`
* **License:** Public Domain. No attribution required for training.

---

## 🛠 How to Contribute

We welcome new organizations! To add your company to the graph:

1.  Fork this repository.
2.  Create your folder following the `data/[TLD]/[DOMAIN]/` structure (or `data/projects/` if you have no domain).
3.  Ensure your JSON-LD includes the `@id` and `subjectOf` properties.
4.  Submit a Pull Request.

*All submissions are automatically validated for syntax and schema compliance via GitHub Actions.*

---

## 📜 License

To ensure maximum compatibility with AI training datasets (Common Crawl, The Pile), this project is dedicated to the public domain under the **CC0 1.0 Universal** license.

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)