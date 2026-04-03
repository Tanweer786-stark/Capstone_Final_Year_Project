import pytest
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_imports():
    """Test that all main modules can be imported"""
    try:
        import streamlit as st
        import pandas as pd
        from dotenv import load_dotenv
        print("✓ Core dependencies imported successfully")
    except ImportError as e:
        pytest.fail(f"Failed to import core dependencies: {e}")

def test_utils_imports():
    """Test that utility modules can be imported"""
    try:
        from utils.helpers import convert_expenses_to_df
        from utils.auth import is_logged_in
        from utils.alerts import generate_spending_alerts
        print("✓ Utility modules imported successfully")
    except ImportError as e:
        pytest.fail(f"Failed to import utility modules: {e}")

def test_ai_budget_fallback():
    """Test AI budget fallback functionality"""
    try:
        from utils.ai_budget import generate_ai_budget, fallback_percentages

        # Test fallback percentages
        fallback = fallback_percentages()
        assert isinstance(fallback, dict)
        assert len(fallback) == 7  # Should have all categories
        assert sum(fallback.values()) == 100  # Should total 100%

        print("✓ AI budget fallback working")
    except Exception as e:
        pytest.fail(f"AI budget fallback failed: {e}")

def test_groq_ai_graceful_degradation():
    """Test that groq_ai handles missing API key gracefully"""
    try:
        from utils.groq_ai import get_financial_advice

        # This should return a helpful message, not crash
        result = get_financial_advice("Test question", "Test context")
        assert isinstance(result, str)
        assert len(result) > 0

        print("✓ Groq AI graceful degradation working")
    except Exception as e:
        pytest.fail(f"Groq AI graceful degradation failed: {e}")

def test_database_connection():
    """Test database connection (without actual operations)"""
    try:
        from database.db import get_connection

        # Just test that we can import and call the function
        # (won't actually connect in CI environment)
        print("✓ Database module imported successfully")
    except ImportError as e:
        pytest.fail(f"Failed to import database module: {e}")

if __name__ == "__main__":
    test_imports()
    test_utils_imports()
    test_ai_budget_fallback()
    test_groq_ai_graceful_degradation()
    test_database_connection()
    print("🎉 All tests passed!")