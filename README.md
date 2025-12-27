# LG-9: HD Wallet + Mempool Explorer

Bitcoin Testnet HD Wallet with Real-Time Mempool Analysis

[![Bitcoin](https://img.shields.io/badge/Bitcoin-Testnet-orange.svg)](https://testnet.blockchain.info/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29-red.svg)](https://streamlit.io/)

## 🌟 Features

### Wallet Management
- ✅ **HD Wallet Generation** (BIP39/BIP32/BIP44)
- ✅ **12/24-word Mnemonic** phrases
- ✅ **Multiple Address** derivation
- ✅ **Encrypted Backup** (AES-256-GCM)
- ✅ **Import/Export** functionality
- ✅ **QR Code** generation

### Transaction Handling
- ✅ **Create & Sign** transactions
- ✅ **Fee Estimation** (Fast/Standard/Economy)
- ✅ **UTXO Management**
- ✅ **Broadcast** to Bitcoin Testnet
- ✅ **Transaction Preview**

### Mempool Analysis
- ✅ **Real-time Statistics**
- ✅ **Fee Distribution**
- ✅ **Live Transaction Feed**
- ✅ **Confirmation Estimates**

## 🚀 Quick Start

### Option 1: Simple Batch Script (Recommended for Windows)

Just double-click the batch file:

```
run.bat
```

This will open two terminal windows:
- Backend server (FastAPI)
- Frontend dashboard (Streamlit)

### Option 2: Python Launcher Script

Run the unified launcher:

```bash
python run.py
```

This starts both servers in a single terminal with colored output and proper error handling.

### Option 3: Manual Start

**Terminal 1 - Backend:**
```bash
cd backend
python -m uvicorn app.main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
streamlit run app.py
```

## 📍 Access Points

Once started, access the application at:

- **Frontend Dashboard**: http://localhost:8501
- **Backend API Docs**: http://127.0.0.1:8000/docs
- **Backend Health**: http://127.0.0.1:8000/health

## 📦 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd lg9-wallet
```

### 2. Install Dependencies

**Backend:**
```bash
cd backend
pip install -r requirements.txt
```

**Frontend:**
```bash
cd frontend
pip install -r requirements.txt
```

### 3. Run the Application

Use any of the Quick Start methods above!

## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation
- **bitcoinlib** - Bitcoin operations
- **cryptography** - Encryption (AES-256-GCM)

### Frontend
- **Streamlit** - Interactive web UI
- **Plotly** - Data visualization
- **QRCode** - QR code generation
- **pandas** - Data manipulation

### Bitcoin Standards
- **BIP39** - Mnemonic code generation
- **BIP32** - Hierarchical deterministic wallets
- **BIP44** - Multi-account hierarchy (m/44'/1'/0'/0/index)

## 🔒 Security

### Testnet Only
- **⚠️ CRITICAL**: This application ONLY works with Bitcoin Testnet
- **coin_type = 1** (Testnet)
- Never use with real Bitcoin!

### Best Practices
- ✅ Private keys never exposed in UI
- ✅ Mnemonic shown only once
- ✅ AES-256-GCM encryption
- ✅ PBKDF2 password hashing (100k iterations)
- ✅ HTTPS ready for production

## 📱 Application Pages

### 1. Dashboard (Main)
- Wallet balance overview
- Mempool statistics
- Fee recommendations
- Quick access buttons

### 2. Wallet Generator
- Generate new HD wallet
- Save mnemonic phrase (with verification!)
- Download encrypted backup
- QR codes for all addresses

### 3. Balance Viewer
- View all addresses
- Check balances
- See UTXO counts
- Testnet faucet links

### 4. Send Transaction
- Enter recipient address
- Specify amount (BTC ↔ satoshi)
- Choose fee tier
- Preview before broadcast
- Track transaction status

### 5. Mempool Explorer
- Real-time mempool stats
- Fee distribution charts
- Live transaction feed
- Confirmation estimates

### 6. Settings
- Export/import wallet
- Security information
- Application info
- BIP standards reference

## 💰 Getting Testnet Bitcoins

To test transactions, get free testnet BTC from these faucets:

- https://testnet-faucet.mempool.co/
- https://bitcoinfaucet.uo1.net/
- https://coinfaucet.eu/en/btc-testnet/

## 🧪 Testing

Run the comprehensive test suite:

```bash
python test_comprehensive.py
```

This tests:
- ✅ All API endpoints
- ✅ Wallet creation
- ✅ Balance checking
- ✅ Mempool statistics
- ✅ Fee analysis

## 📚 Project Structure

```
lg9-wallet/
├── backend/                # FastAPI backend
│   ├── app/
│   │   ├── api/           # API routes
│   │   ├── core/          # Configuration
│   │   ├── mempool/       # Mempool analysis
│   │   ├── models/        # Pydantic models
│   │   ├── transaction/   # Transaction handling
│   │   ├── utils/         # Utilities
│   │   └── wallet/        # HD wallet logic
│   ├── main.py            # Entry point
│   └── requirements.txt
│
├── frontend/              # Streamlit frontend
│   ├── pages/            # Multi-page app
│   │   ├── 2_💼_Wallet_Generator.py
│   │   ├── 3_💰_Balance_Viewer.py
│   │   ├── 4_📤_Send_Transaction.py
│   │   ├── 5_📊_Mempool_Explorer.py
│   │   └── 6_⚙️_Settings.py
│   ├── utils/            # UI utilities
│   │   ├── api_client.py
│   │   ├── branding.py
│   │   └── styles.py
│   ├── app.py            # Main dashboard
│   └── requirements.txt
│
├── run.py                # Python launcher
├── run.bat              # Windows batch launcher
└── README.md            # This file
```

## 🎓 Academic Project

This project is developed for the **LG-9 Blockchain Technologies** course.

### Learning Objectives
- Understanding HD wallet architecture
- Bitcoin transaction structure
- Cryptographic key derivation
- Fee market dynamics
- Real-time blockchain data analysis

### Features Demonstrated
- Full BIP39/32/44 compliance
- ECDSA transaction signing
- UTXO management
- Mempool analysis
- Professional UI/UX design

## 🐛 Troubleshooting

### Backend won't start
- Check if port 8000 is available
- Verify Python version (3.8+ required)
- Install dependencies: `pip install -r backend/requirements.txt`

### Frontend won't start
- Check if port 8501 is available
- Verify Streamlit is installed: `pip install streamlit`
- Install dependencies: `pip install -r frontend/requirements.txt`

### Wallet creation fails
- Ensure backend is running
- Check backend logs for errors
- Verify network connectivity

### Transaction broadcast fails
- Confirm you're using testnet addresses (start with m, n, 2, or tb1)
- Check wallet has sufficient balance
- Verify testnet faucet has funded your address

## 📄 License

This is an academic project for educational purposes.

## 👏 Acknowledgments

- Bitcoin Core Team
- BIP authors (39, 32, 44)
- FastAPI & Streamlit communities

## ⚠️ Disclaimer

**TESTNET ONLY** - This application is exclusively for Bitcoin Testnet. Never use it with real Bitcoin or mainnet addresses. Test coins have no monetary value.

---

**Built with ₿ for LG-9 Course | Bitcoin Testnet**
