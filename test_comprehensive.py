"""
LG-9 Comprehensive UI and Feature Test Report

This script tests all major features and checks for any issues.
"""

import requests
import json
from typing import Dict, Any, List

BASE_URL = "http://127.0.0.1:8000"

class TestResults:
    def __init__(self):
        self.passed = []
        self.failed = []
        self.warnings = []
    
    def add_pass(self, test: str):
        self.passed.append(test)
        print(f"✅ PASS: {test}")
    
    def add_fail(self, test: str, reason: str):
        self.failed.append((test, reason))
        print(f"❌ FAIL: {test} - {reason}")
    
    def add_warning(self, test: str, reason: str):
        self.warnings.append((test, reason))
        print(f"⚠️  WARN: {test} - {reason}")
    
    def print_summary(self):
        print("\n" + "="*70)
        print("TEST SUMMARY")
        print("="*70)
        print(f"✅ Passed: {len(self.passed)}")
        print(f"❌ Failed: {len(self.failed)}")
        print(f"⚠️  Warnings: {len(self.warnings)}")
        
        if self.failed:
            print("\nFailed Tests:")
            for test, reason in self.failed:
                print(f"  - {test}: {reason}")
        
        if self.warnings:
            print("\nWarnings:")
            for test, reason in self.warnings:
                print(f"  - {test}: {reason}")
        
        print("="*70)

results = TestResults()

def test_wallet_creation():
    """Test wallet creation with different configurations"""
    print("\n" + "▶ "*35)
    print("TESTING: Wallet Creation")
    print("▶ "*35)
    
    # Test 12-word wallet
    resp = requests.post(f"{BASE_URL}/api/wallet/create", json={
        "word_count": 12,
        "password": "test123456",
        "num_addresses": 3
    }, timeout=10)
    
    if resp.status_code == 200:
        data = resp.json()
        if 'mnemonic' in data and len(data['mnemonic'].split()) == 12:
            results.add_pass("12-word wallet creation")
        else:
            results.add_fail("12-word wallet creation", "Invalid mnemonic format")
        
        if 'addresses' in data and len(data['addresses']) == 3:
            results.add_pass("Correct number of addresses generated")
        else:
            results.add_fail("Address generation", f"Expected 3, got {len(data.get('addresses', []))}")
        
        if 'encrypted_export' in data:
            results.add_pass("Encrypted export included")
        else:
            results.add_fail("Encrypted export", "Missing encrypted export")
    else:
        results.add_fail("Wallet creation API", f"HTTP {resp.status_code}")

def test_wallet_endpoints():
    """Test all wallet-related endpoints"""
    print("\n" + "▶ "*35)
    print("TESTING: Wallet Endpoints")
    print("▶ "*35)
    
    # Get addresses
    resp = requests.get(f"{BASE_URL}/api/wallet/addresses", timeout=10)
    if resp.status_code == 200:
        results.add_pass("Get addresses endpoint")
        addresses = resp.json()
        if addresses:
            # Check address format
            addr = addresses[0]
            if 'address' in addr and 'path' in addr and 'index' in addr:
                results.add_pass("Address format validation")
            else:
                results.add_warning("Address format", "Missing expected fields")
    else:
        results.add_fail("Get addresses endpoint", f"HTTP {resp.status_code}")
    
    # Get balance
    resp = requests.get(f"{BASE_URL}/api/wallet/balance", timeout=10)
    if resp.status_code == 200:
        results.add_pass("Get balance endpoint")
        balance = resp.json()
        if 'total_balance' in balance and 'total_balance_satoshi' in balance:
            results.add_pass("Balance format validation")
        else:
            results.add_warning("Balance format", "Missing expected fields")
    else:
        results.add_fail("Get balance endpoint", f"HTTP {resp.status_code}")

def test_mempool_endpoints():
    """Test mempool-related endpoints"""
    print("\n" + "▶ "*35)
    print("TESTING: Mempool Endpoints")
    print("▶ "*35)
    
    # Mempool stats
    resp = requests.get(f"{BASE_URL}/api/mempool/stats", timeout=10)
    if resp.status_code == 200:
        results.add_pass("Mempool stats endpoint")
        stats = resp.json()
        expected_fields = ['tx_count', 'avg_fee_rate', 'mempool_size_mb']
        missing = [f for f in expected_fields if f not in stats]
        if not missing:
            results.add_pass("Mempool stats format")
        else:
            results.add_warning("Mempool stats format", f"Missing: {missing}")
    else:
        results.add_fail("Mempool stats endpoint", f"HTTP {resp.status_code}")
    
    # Fee analysis
    resp = requests.get(f"{BASE_URL}/api/mempool/fees", timeout=10)
    if resp.status_code == 200:
        results.add_pass("Fee analysis endpoint")
        fees = resp.json()
        if 'estimates' in fees and len(fees['estimates']) > 0:
            results.add_pass("Fee estimates included")
            # Check for fast/standard/economy tiers
            tiers = [e.get('fee_tier') for e in fees['estimates']]
            expected_tiers = ['fast', 'standard', 'economy']
            if all(t in tiers for t in expected_tiers):
                results.add_pass("All fee tiers present")
            else:
                results.add_warning("Fee tiers", f"Expected {expected_tiers}, got {tiers}")
        else:
            results.add_warning("Fee estimates", "No estimates returned")
    else:
        results.add_fail("Fee analysis endpoint", f"HTTP {resp.status_code}")

def test_api_info():
    """Test API information endpoints"""
    print("\n" + "▶ "*35)
    print("TESTING: API Information")
    print("▶ "*35)
    
    # Health check
    resp = requests.get(f"{BASE_URL}/health", timeout=10)
    if resp.status_code == 200:
        results.add_pass("Health check endpoint")
    else:
        results.add_fail("Health check endpoint", f"HTTP {resp.status_code}")
    
    # API info
    resp = requests.get(f"{BASE_URL}/api/info", timeout=10)
    if resp.status_code == 200:
        results.add_pass("API info endpoint")
        data = resp.json()
        if data.get('network') == "Bitcoin Testnet":
            results.add_pass("Network verification (Testnet)")
        else:
            results.add_fail("Network verification", f"Expected Testnet, got {data.get('network')}")
    else:
        results.add_fail("API info endpoint", f"HTTP {resp.status_code}")

def check_ui_completeness():
    """Check if all UI pages are accessible"""
    print("\n" + "▶ "*35)
    print("CHECKING: Frontend Pages")
    print("▶ "*35)
    
    # Check if Streamlit is running
    try:
        resp = requests.get("http://localhost:8501", timeout=5)
        if resp.status_code == 200:
            results.add_pass("Frontend Streamlit server")
        else:
            results.add_fail("Frontend Streamlit server", f"HTTP {resp.status_code}")
    except Exception as e:
        results.add_fail("Frontend Streamlit server", str(e))

def main():
    print("\n" + "🔍"*35)
    print("LG-9 COMPREHENSIVE FEATURE TEST")
    print("🔍"*35)
    
    try:
        test_api_info()
        test_wallet_creation()
        test_wallet_endpoints()
        test_mempool_endpoints()
        check_ui_completeness()
        
        results.print_summary()
        
        # Final verdict
        print("\n" + "="*70)
        if not results.failed:
            print("🎉 ALL TESTS PASSED! The application is fully functional.")
        else:
            print(f"⚠️  {len(results.failed)} tests failed. Review the issues above.")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"\n❌ Testing failed with exception: {str(e)}")
        results.add_fail("Test Suite", str(e))

if __name__ == "__main__":
    main()
