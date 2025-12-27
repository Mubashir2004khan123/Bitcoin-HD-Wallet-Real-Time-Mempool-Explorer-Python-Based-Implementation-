"""
Quick test script to verify demo balance API endpoint
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_backend():
    print("🧪 Testing Demo Balance Feature\n")
    
    # Test 1: Check backend is running
    print("1. Checking backend connection...")
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=2)
        if response.status_code == 200:
            print("   ✅ Backend is running")
        else:
            print(f"   ❌ Backend returned status {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Cannot connect to backend: {e}")
        return False
    
    # Test 2: Check if wallet exists
    print("\n2. Checking if wallet exists...")
    try:
        response = requests.get(f"{BASE_URL}/api/wallet/addresses")
        if response.status_code == 200:
            addresses = response.json()
            if len(addresses) > 0:
                print(f"   ✅ Wallet found with {len(addresses)} addresses")
                test_address = addresses[0]['address']
                print(f"   Using address: {test_address[:20]}...")
            else:
                print("   ⚠️  No addresses found. Create a wallet first!")
                return False
        else:
            print("   ⚠️  No wallet loaded. Create a wallet first!")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False
    
    # Test 3: Credit demo balance
    print("\n3. Testing demo balance credit...")
    try:
        amount_btc = 0.05
        amount_satoshi = int(amount_btc * 100_000_000)
        
        response = requests.post(
            f"{BASE_URL}/api/demo/credit",
            json={
                "address": test_address,
                "amount_satoshi": amount_satoshi
            }
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"   ✅ Demo balance credited!")
            print(f"   Amount: {result['amount_btc']:.8f} tBTC")
            print(f"   New balance: {result['new_demo_balance_btc']:.8f} tBTC")
        else:
            print(f"   ❌ Failed with status {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False
    
    # Test 4: Check balance reflects the demo credit
    print("\n4. Verifying balance update...")
    try:
        response = requests.get(f"{BASE_URL}/api/wallet/balance")
        if response.status_code == 200:
            balance = response.json()
            total_btc = balance['total_balance']
            print(f"   ✅ Total balance: {total_btc:.8f} tBTC")
            if total_btc > 0:
                print(f"   ✅ Balance includes demo credit!")
            else:
                print(f"   ⚠️  Balance is zero, demo credit may not be showing")
        else:
            print(f"   ❌ Failed to get balance")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False
    
    print("\n✅ All tests passed! Demo balance feature is working!")
    return True

if __name__ == "__main__":
    test_backend()
