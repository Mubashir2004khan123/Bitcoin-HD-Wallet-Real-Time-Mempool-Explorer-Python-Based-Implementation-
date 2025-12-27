"""
LG-9 Application Launcher
Starts both Backend (FastAPI) and Frontend (Streamlit) servers simultaneously

Usage: python run.py
"""

import subprocess
import sys
import time
import os
from pathlib import Path

# Colors for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_banner():
    """Print LG-9 startup banner"""
    print(f"\n{Colors.OKBLUE}{'='*70}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKGREEN}     ██╗      ██████╗       ██████╗ {Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKGREEN}     ██║     ██╔════╝      ██╔═══██╗{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKGREEN}     ██║     ██║  ███╗█████╗╚██████╔╝{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKGREEN}     ██║     ██║   ██║╚════╝██╔═══██╗{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKGREEN}     ███████╗╚██████╔╝      ╚██████╔╝{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKGREEN}     ╚══════╝ ╚═════╝        ╚═════╝ {Colors.ENDC}")
    print(f"\n{Colors.BOLD}  HD Wallet + Mempool Explorer | Bitcoin Testnet{Colors.ENDC}")
    print(f"{Colors.OKBLUE}{'='*70}{Colors.ENDC}\n")

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print(f"{Colors.FAIL}❌ Error: Python 3.8 or higher is required{Colors.ENDC}")
        print(f"   Current version: {sys.version}")
        sys.exit(1)
    print(f"{Colors.OKGREEN}✅ Python version: {sys.version.split()[0]}{Colors.ENDC}")

def check_ports():
    """Check if required ports are available"""
    import socket
    
    ports = {8000: "Backend", 8501: "Frontend"}
    
    for port, service in ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', port))
        sock.close()
        
        if result == 0:
            print(f"{Colors.WARNING}⚠️  Port {port} ({service}) is already in use{Colors.ENDC}")
            answer = input(f"   Continue anyway? (y/n): ")
            if answer.lower() != 'y':
                sys.exit(1)

def start_backend():
    """Start the FastAPI backend server"""
    print(f"\n{Colors.OKCYAN}🚀 Starting Backend Server...{Colors.ENDC}")
    
    backend_dir = Path(__file__).parent / "backend"
    
    if not backend_dir.exists():
        print(f"{Colors.FAIL}❌ Backend directory not found: {backend_dir}{Colors.ENDC}")
        sys.exit(1)
    
    # Start uvicorn
    backend_process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "app.main:app", "--reload", "--host", "127.0.0.1", "--port", "8000"],
        cwd=backend_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        bufsize=1
    )
    
    print(f"{Colors.OKGREEN}   Backend PID: {backend_process.pid}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}   Backend URL: http://127.0.0.1:8000{Colors.ENDC}")
    print(f"{Colors.OKGREEN}   API Docs: http://127.0.0.1:8000/docs{Colors.ENDC}")
    
    return backend_process

def start_frontend():
    """Start the Streamlit frontend server"""
    print(f"\n{Colors.OKCYAN}🚀 Starting Frontend Server...{Colors.ENDC}")
    
    frontend_dir = Path(__file__).parent / "frontend"
    
    if not frontend_dir.exists():
        print(f"{Colors.FAIL}❌ Frontend directory not found: {frontend_dir}{Colors.ENDC}")
        sys.exit(1)
    
    # Start streamlit
    frontend_process = subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "app.py", "--server.port", "8501", "--server.headless", "true"],
        cwd=frontend_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        bufsize=1
    )
    
    print(f"{Colors.OKGREEN}   Frontend PID: {frontend_process.pid}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}   Frontend URL: http://localhost:8501{Colors.ENDC}")
    
    return frontend_process

def main():
    """Main application launcher"""
    print_banner()
    
    # Pre-flight checks
    print(f"{Colors.HEADER}📋 Pre-flight Checks{Colors.ENDC}")
    check_python_version()
    check_ports()
    
    print(f"\n{Colors.OKGREEN}✅ All checks passed!{Colors.ENDC}\n")
    
    # Start servers
    backend_process = None
    frontend_process = None
    
    try:
        # Start backend first
        backend_process = start_backend()
        time.sleep(3)  # Give backend time to start
        
        # Then start frontend
        frontend_process = start_frontend()
        time.sleep(2)  # Give frontend time to start
        
        # Success message
        print(f"\n{Colors.OKBLUE}{'='*70}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.OKGREEN}🎉 LG-9 Application Started Successfully!{Colors.ENDC}")
        print(f"{Colors.OKBLUE}{'='*70}{Colors.ENDC}\n")
        
        print(f"{Colors.BOLD}📍 Access Points:{Colors.ENDC}")
        print(f"   • Frontend Dashboard: {Colors.OKCYAN}http://localhost:8501{Colors.ENDC}")
        print(f"   • Backend API Docs:   {Colors.OKCYAN}http://127.0.0.1:8000/docs{Colors.ENDC}")
        
        print(f"\n{Colors.WARNING}⚠️  Press Ctrl+C to stop both servers{Colors.ENDC}\n")
        
        # Keep running and show logs
        print(f"{Colors.HEADER}📜 Server Logs:{Colors.ENDC}")
        print(f"{Colors.OKBLUE}{'-'*70}{Colors.ENDC}\n")
        
        # Monitor both processes
        while True:
            # Check if processes are still running
            if backend_process.poll() is not None:
                print(f"\n{Colors.FAIL}❌ Backend process terminated unexpectedly{Colors.ENDC}")
                break
            
            if frontend_process.poll() is not None:
                print(f"\n{Colors.FAIL}❌ Frontend process terminated unexpectedly{Colors.ENDC}")
                break
            
            time.sleep(1)
    
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}🛑 Shutting down servers...{Colors.ENDC}")
    
    except Exception as e:
        print(f"\n{Colors.FAIL}❌ Error: {str(e)}{Colors.ENDC}")
    
    finally:
        # Clean up processes
        if backend_process:
            print(f"{Colors.OKCYAN}   Stopping backend...{Colors.ENDC}")
            backend_process.terminate()
            try:
                backend_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                backend_process.kill()
        
        if frontend_process:
            print(f"{Colors.OKCYAN}   Stopping frontend...{Colors.ENDC}")
            frontend_process.terminate()
            try:
                frontend_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                frontend_process.kill()
        
        print(f"\n{Colors.OKGREEN}✅ All servers stopped{Colors.ENDC}")
        print(f"{Colors.BOLD}Thank you for using LG-9! 👋{Colors.ENDC}\n")

if __name__ == "__main__":
    main()
