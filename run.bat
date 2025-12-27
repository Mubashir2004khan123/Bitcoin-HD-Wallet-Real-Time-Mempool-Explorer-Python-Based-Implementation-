
@echo off
REM LG-9 Application Launcher (Windows Batch Script)
REM Starts both Backend and Frontend servers

echo ======================================================================
echo      ██╗      ██████╗       ██████╗ 
echo      ██║     ██╔════╝      ██╔═══██╗
echo      ██║     ██║  ███╗█████╗╚██████╔╝
echo      ██║     ██║   ██║╚════╝██╔═══██╗
echo      ███████╗╚██████╔╝      ╚██████╔╝
echo      ╚══════╝ ╚═════╝        ╚═════╝ 
echo.
echo   HD Wallet + Mempool Explorer ^| Bitcoin Testnet
echo ======================================================================
echo.

echo [1/3] Starting Backend Server...
start "LG-9 Backend" cmd /k "cd backend && python -m uvicorn app.main:app --reload"
timeout /t 3 /nobreak > nul

echo [2/3] Starting Frontend Server...
start "LG-9 Frontend" cmd /k "cd frontend && streamlit run app.py"
timeout /t 2 /nobreak > nul

echo.
echo ======================================================================
echo   🎉 LG-9 Application Started Successfully!
echo ======================================================================
echo.
echo   📍 Access Points:
echo      • Frontend Dashboard: http://localhost:8501
echo      • Backend API Docs:   http://127.0.0.1:8000/docs
echo.
echo   ⚠️  Close the terminal windows to stop the servers
echo.
echo ======================================================================
echo.

pause
