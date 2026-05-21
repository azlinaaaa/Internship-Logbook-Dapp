# 🚀 Stellar LogTrust: Decentralized Internship Logbook dApp

[![Stellar](https://img.shields.io/badge/Blockchain-Stellar-black?style=for-the-badge&logo=stellar)](https://stellar.org)
[![Python](https://img.shields.io/badge/Backend-Python%203.11+-blue?style=for-the-badge&logo=python)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

An enterprise-grade, blockchain-anchored Decentralized Application (dApp) designed to transform traditional internship reporting. By combining **Python Flask** with the **Stellar Blockchain Network**, this platform enforces absolute cryptographic data integrity, prevents academic fraud, and establishes an immutable ledger of student industrial training records.

---

## 📌 Executive Summary & Problem Statement

### The Problem
Traditional internship logbooks rely heavily on central databases or physical signatures, making them vulnerable to:
* **Retroactive Modification:** Students altering past records at the end of their internship.
* **Lack of Transparency:** Industrial supervisors and university coordinators having no decentralized method to verify if a log was legitimately written on the specified date.
* **Data Vulnerability:** Single points of failure inherent in standard centralized storage systems.

### The Innovation: Stellar LogTrust
This dApp solves these challenges by treating every daily log submission as a unique state transaction. The system compiles input data, generates a cryptographic signature, and anchors it immutably onto the Stellar Testnet Layer-1 ledger via `manage_data` operations. This establishes a high-throughput, low-cost verifiable audit trail for academic institutions.

---

## 📸 System Interface & Visual Walkthrough

### 1. Main Landing Page
The entry point of the dApp featuring a high-impact corporate design that introduces the core values of decentralized trust in academic reporting.
![Main Website](https://raw.githubusercontent.com/azlinaaaa/Internship-Logbook-Dapp/572e8757dc5058bdcc8f797578091122bf546b82/Image/Main_Website.png)

### 2. Node Profile Registration
Secured portal access where users can provision a new account. The backend dynamically handles node registration and prepares session parameters.
![Create Account](https://raw.githubusercontent.com/azlinaaaa/Internship-Logbook-Dapp/572e8757dc5058bdcc8f797578091122bf546b82/Image/Create_Account.png)

### 3. User Authentication & Welcome Portal
A secure authentication gate enforcing stateful session management before granting access to the cryptographic ledger tools.
![Welcome User](https://raw.githubusercontent.com/azlinaaaa/Internship-Logbook-Dapp/572e8757dc5058bdcc8f797578091122bf546b82/Image/Welcome_User.png)

### 4. Interactive Analytics Dashboard
The enterprise UI dashboard that aggregates overall activities, showing cryptographic keys and anchored log statistics without workspace clutter.
![Dashboard](https://raw.githubusercontent.com/azlinaaaa/Internship-Logbook-Dapp/572e8757dc5058bdcc8f797578091122bf546b82/Image/Dashboard.png)

### 5. Cryptographic Log Submission Form
The core interface where students input their daily industrial tasks. Data entered here is automatically staged for SHA-256 hashing.
![Submit Internship Log Form](https://raw.githubusercontent.com/azlinaaaa/Internship-Logbook-Dapp/572e8757dc5058bdcc8f797578091122bf546b82/Image/Submit_Internship_Log.png)
*(Alternative view showing structured fields for secure data entry)*
![Submit Internship Log Fields](https://raw.githubusercontent.com/azlinaaaa/Internship-Logbook-Dapp/572e8757dc5058bdcc8f797578091122bf546b82/Image/Submit_Internship_Log%20(2).png)

### 6. Blockchain Immutable Confirmation
Once submitted, the system displays a verification screen showing the real-time SHA-256 State Hash and the globally verifiable Stellar Transaction Hash.
![After Submit Log](https://raw.githubusercontent.com/azlinaaaa/Internship-Logbook-Dapp/572e8757dc5058bdcc8f797578091122bf546b82/Image/After_Submit_Log.png)

---

## 🛠️ Advanced Architecture & Tech Stack


```

[User Interface (Bootstrap 5 Dark Tech)]
│ (Secure Session / Flask-Login)
▼
[Flask Backend Application Node]
│
├─► [Cryptographic Engine] ──► Generates SHA-256 State Hash
│
├─► [Stellar SDK Gateway] ───► Broadcasts & Anchors to Stellar Testnet Ledger
│
└─► [Persistence Layer] ─────► Stores Structured Data (SQLite / SQLAlchemy)

```

### Core Technologies
* **Core Backend:** Python 3.11+ with Flask Framework (Microservice-ready architecture).
* **Decentralized Ledger Technology (DLT):** `stellar-sdk` interfacing with the Stellar Horizon Testnet API.
* **Cryptographic Engine:** Built-in `hashlib` utilizing SHA-256 hashing standards.
* **Security & Authentication:** `Flask-Login` for stateful session management; `Werkzeug.security` executing secure salted PBKDF2 password hashing.
* **Database Management:** SQLite handled via Flask-SQLAlchemy Object-Relational Mapping (ORM).
* **Frontend Interface:** Glassmorphic Futuristic Dark-Mode UI powered by Bootstrap 5 & Bootstrap Icons.

---

## 🌟 Key Features

1. **Cryptographic Record Anchoring**
   When a student submits a logbook entry, the backend instantly concatenates the Title + Content + Username. This payload passes through a SHA-256 algorithm to output a unique 64-character digital fingerprint.
2. **Live Stellar Ledger Integration**
   The generated hash is injected into a live Stellar transaction as a key-value data attribute (`manage_data` operation). This transaction is signed programmatically via the user's secret key and broadcasted to the Horizon network, yielding a globally verifiable Stellar Transaction Hash.
3. **Fault-Tolerant Network Handshaking**
   The application contains native blockchain exception handling. If a new user profile tries to communicate with the ledger, the backend catches `NotFoundError` (404) codes and triggers an automatic asynchronous connection to the Stellar Friendbot API to bootstrap and fund the network node seamlessly.
4. **Enterprise UI/UX Dashboard**
   Features a high-fidelity, responsive analytics interface built with glassmorphism aesthetics, designed to present deep transaction hashes and cryptographic keys cleanly without cluttering user workspace.

---

## 📂 Project Structure


```

Internship-Logbook-DApp/
│
├── app.py                 # Core application controller & route handlers
├── stellar_utils.py       # Blockchain interface module (Keypair generation, Transaction construction)
├── requirements.txt       # Frozen project dependencies
├── .gitignore             # Strict directory masking (Excludes .env, instance, and venv)
├── README.md              # Software documentation
│
├── templates/             # UI Presentation Layer (Jinja2 Templates)
│   ├── index.html         # High-impact corporate landing page
│   ├── login.html         # Secure portal access page
│   ├── register.html      # Node profile registration
│   ├── dashboard.html     # Analytics and transaction history view
│   └── submit_log.html    # Cryptographic payload submission form
│
└── instance/
└── internship.db      # Local relational ledger state (SQLite)

```

---

## 🚀 Quick-Start Installation Guide

### Prerequisites
* Python 3.11 or higher installed.
* Stable internet connection (for Stellar Horizon Network syncing).

### 1. Clone & Navigate
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git)
cd Internship-Logbook-DApp

```

### 2. Isolate Environment

```bash
# Create Virtual Environment
python -m venv .venv

# Activate - Windows
.venv\Scripts\activate

# Activate - macOS/Linux
source .venv/bin/activate

```

### 3. System Provisioning

```bash
pip install -r requirements.txt

```

### 4. Configuration Layer (.env)

Create a `.env` file in the root directory to store system variables:

```env
SECRET_KEY=your_robust_flask_session_secret_key
STELLAR_SECRET_KEY=your_stellar_testnet_secret_seed_starting_with_S

```

*(Note: The public key is generated dynamically from the secret key inside the system utility to eliminate redundancy)*

### 5. Launch Node

```bash
python app.py

```

Open your browser and navigate to `http://127.0.0.1:5000` to interact with the application.

---

## 🔒 Security Architectures

* **Zero Trust Key Management:** Public keys are generated dynamically in-memory via `Keypair.from_secret()`. No sensitive data keys are hardcoded or pushed to repository streams.
* **CSRF Mitigation & Secure Sessions:** Session-based authentication handles endpoint routing restrictions through the `@login_required` decorator.
* **Input Data Isolation:** Prevention of basic SQL injection vectors by mapping inputs through parameterized SQLAlchemy queries.

---

## 🔮 Future Horizons & Scalability Roadmap

* **Soroban Smart Contracts:** Transitioning data verification parameters into compiled Rust-based smart contracts for automated multi-party approval workflows.
* **Non-Custodial Wallet Protocols:** Integrating Freighter Wallet to allow students to physically sign transactions using their own decentralized identities.
* **Supervisor Decentralized Consensus:** Implementing a multi-signature framework where an entry is only fully finalized when approved by both student and supervisor keys.
* **AI-Driven Analytics:** Injecting NLP sentiment and progress analyzers into the log submission interface to flag anomalies or burnout signals automatically.

---

## 🎯 Competition Value Proposition

* **Real-World Web3 Integration:** Moving past theoretical blockchain definitions into functional, everyday utility using the cost-effective Stellar rails.
* **Production-Ready UI:** Replaces monotonous default templates with an aesthetically superior dark mode design to appeal directly to modern digital workspaces.
* **Highly Reproducible:** Clear deployment pathways with robust sandbox automation handling account funding behind the scenes.

---

## 👩‍💻 Author & Technical Contribution

**Norazlina Shariff**

*Data Science Specialist & Blockchain Engineering Enthusiast*

Focusing on bridging the gap between standard enterprise web architecture and decentralized trust networks. Developed for educational innovation and competitive dApp evaluation benchmarks.

*Developed for educational innovation and competitive dApp evaluation benchmarks.*


