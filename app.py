"""
Disney Trip Planning Agent - Streamlit Web Application
A beautiful, user-friendly interface for planning your magical Disney vacation
"""
import streamlit as st
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
import time
import pytz
import pickle
from pathlib import Path

from src.agents.trip_planner_agent import TripPlannerAgent
from src.models.trip_data import TripDetails, ChecklistItem, IdeaSuggestion
from src.utils.helpers import calculate_countdown, format_countdown, get_trip_phase
from src.utils.firebase_config import get_firebase_manager

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Disney Trip Planner",
    page_icon="🏰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for 90's Disney Glassmorphism Theme - Baby Blue & Soft Pink
st.markdown("""
<style>
    /* Import playful 90's Disney-inspired fonts */
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@300;400;500;600;700&family=Quicksand:wght@300;400;500;600;700&display=swap');

    /* Base font - Playful and rounded */
    * {
        font-family: 'Quicksand', sans-serif !important;
    }

    /* Headers - Fun and bouncy */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Fredoka', sans-serif !important;
        font-weight: 600 !important;
    }

    /* ========== COLOR VARIABLES - 90's DISNEY PALETTE ========== */
    :root {
        --baby-blue: #89CFF0;
        --soft-pink: #FFB6C1;
        --light-pink: #F4C2C2;
        --powder-pink: #FADADD;
        --lavender: #E6E6FA;
        --cream: #FFF8F0;
        --mint: #E0F7F4;
        --peach: #FFE5D9;
        --sunshine: #FFF44F;
        --white: #FFFFFF;
    }

    /* ========== LAYOUT - CLEAN & CENTERED ========== */

    /* Main container - centered and contained */
    .block-container {
        max-width: 1400px !important;
        padding: 3rem 4rem !important;
        margin: 0 auto !important;
    }

    /* Sidebar toggle button - Glassmorphism bubble */
    [data-testid="collapsedControl"] {
        color: var(--baby-blue) !important;
        background: rgba(255, 255, 255, 0.25) !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;
        border-radius: 50% !important;
        padding: 12px !important;
        margin: 15px !important;
        border: 2px solid rgba(137, 207, 240, 0.3) !important;
        box-shadow: 0 8px 32px rgba(137, 207, 240, 0.3),
                    inset 0 2px 10px rgba(255, 255, 255, 0.5) !important;
        transition: all 0.4s cubic-bezier(0.68, -0.55, 0.27, 1.55) !important;
    }

    [data-testid="collapsedControl"]:hover {
        background: rgba(255, 182, 193, 0.35) !important;
        transform: scale(1.15) rotate(5deg) !important;
        box-shadow: 0 12px 48px rgba(255, 182, 193, 0.5),
                    inset 0 2px 15px rgba(255, 255, 255, 0.7) !important;
    }

    /* Icon sizing */
    [data-testid="collapsedControl"] svg {
        width: 24px !important;
        height: 24px !important;
        display: block !important;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1)) !important;
    }

    /* Hide any text in sidebar toggle */
    [data-testid="collapsedControl"] span,
    [data-testid="collapsedControl"] p,
    [data-testid="collapsedControl"] div:not([data-testid]),
    [data-testid="collapsedControl"] *:not(svg):not(path) {
        display: none !important;
        font-size: 0 !important;
        opacity: 0 !important;
    }

    /* Force only SVG icon to show */
    [data-testid="collapsedControl"] svg,
    [data-testid="collapsedControl"] svg * {
        display: block !important;
        opacity: 1 !important;
    }

    /* Prevent text wrapping in input fields */
    .stTextInput input,
    .stNumberInput input,
    .stDateInput input,
    .stSelectbox select,
    .stSelectbox div[data-baseweb="select"] > div,
    .stMultiSelect div {
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
    }

    /* Text areas can wrap */
    .stTextArea textarea {
        overflow-x: hidden !important;
        overflow-y: auto !important;
        word-wrap: break-word !important;
    }

    /* Element spacing - no overlap */
    .element-container {
        margin-bottom: 1.5rem !important;
        clear: both !important;
    }

    .stMarkdown,
    .stButton,
    .stCheckbox,
    .stTextInput,
    .stSelectbox {
        margin-bottom: 1rem !important;
        position: relative !important;
        z-index: 2 !important;
    }

    /* Center content */
    .main .block-container > div {
        width: 100% !important;
    }

    /* Column spacing */
    [data-testid="column"] {
        padding: 0 1rem !important;
        min-width: 0 !important;
        flex: 1 1 0 !important;
    }

    [data-testid="stHorizontalBlock"] {
        gap: 1rem !important;
        margin-bottom: 1.5rem !important;
    }

    [data-testid="stVerticalBlock"] > div {
        margin-bottom: 1rem !important;
    }

    /* Center all major elements */
    .stTabs,
    .countdown-box,
    .idea-card,
    .checklist-card,
    .main-header,
    .trip-code-diamond {
        margin-left: auto !important;
        margin-right: auto !important;
    }

    .stButton {
        display: block !important;
        margin: 0 auto 1rem auto !important;
        text-align: center !important;
    }

    /* Prevent sidebar overlap */
    .main {
        padding-left: 0 !important;
    }

    /* Prevent text overflow */
    .stButton>button {
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        white-space: nowrap !important;
    }

    /* ========== RESPONSIVE DESIGN ========== */

    @media (max-width: 1200px) {
        .block-container {
            max-width: 100% !important;
            padding: 2rem 2rem !important;
        }
    }

    @media (max-width: 768px) {
        .block-container {
            padding: 1.5rem 1rem !important;
        }

        .main-header {
            font-size: 2.5em !important;
            padding: 40px 20px 30px 20px !important;
        }

        .stButton>button {
            padding: 12px 24px !important;
            font-size: 15px !important;
        }
    }

    /* Overlap prevention */
    .stApp {
        position: relative !important;
        overflow-x: hidden !important;
    }

    .block-container::after {
        content: "" !important;
        display: table !important;
        clear: both !important;
    }

    /* ========== 90's DISNEY ANIMATIONS ========== */

    /* Sparkle trail animation */
    @keyframes sparkleTrail {
        0% {
            opacity: 0;
            transform: translate(0, 0) scale(0) rotate(0deg);
        }
        50% {
            opacity: 1;
            transform: translate(var(--x, 0), var(--y, 0)) scale(1) rotate(180deg);
        }
        100% {
            opacity: 0;
            transform: translate(calc(var(--x, 0) * 2), calc(var(--y, 0) * 2)) scale(0) rotate(360deg);
        }
    }

    /* Bubble float animation */
    @keyframes bubbleFloat {
        0%, 100% {
            transform: translateY(0) translateX(0) scale(1);
            opacity: 0.6;
        }
        25% {
            transform: translateY(-15px) translateX(10px) scale(1.1);
            opacity: 0.8;
        }
        50% {
            transform: translateY(-30px) translateX(-5px) scale(1);
            opacity: 1;
        }
        75% {
            transform: translateY(-15px) translateX(-15px) scale(1.1);
            opacity: 0.8;
        }
    }

    /* Shimmer/shine effect (like Disney logo) */
    @keyframes disneyShine {
        0% {
            left: -100%;
        }
        100% {
            left: 200%;
        }
    }

    /* Bounce in animation */
    @keyframes bounceIn {
        0% {
            transform: scale(0.3) translateY(-100px);
            opacity: 0;
        }
        50% {
            transform: scale(1.05);
        }
        70% {
            transform: scale(0.9);
        }
        100% {
            transform: scale(1) translateY(0);
            opacity: 1;
        }
    }

    /* Gentle pulse */
    @keyframes gentlePulse {
        0%, 100% {
            transform: scale(1);
            box-shadow: 0 8px 32px rgba(137, 207, 240, 0.25);
        }
        50% {
            transform: scale(1.02);
            box-shadow: 0 12px 48px rgba(255, 182, 193, 0.35);
        }
    }

    /* Gradient animation */
    @keyframes gradientShift {
        0%, 100% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
    }

    /* ========== MAIN BACKGROUND - 90's GRADIENT MESH ========== */
    .main {
        background: linear-gradient(135deg,
            var(--baby-blue) 0%,
            var(--mint) 20%,
            var(--lavender) 40%,
            var(--powder-pink) 60%,
            var(--soft-pink) 80%,
            var(--peach) 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        position: relative;
        overflow: hidden;
    }

    /* VHS film grain texture overlay */
    .main::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' /%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.03'/%3E%3C/svg%3E");
        pointer-events: none;
        z-index: 1;
        opacity: 0.5;
    }

    /* Floating bubbles decoration */
    .main::after {
        content: '○';
        position: fixed;
        font-size: 80px;
        color: rgba(255, 255, 255, 0.15);
        top: 20%;
        left: 15%;
        animation: bubbleFloat 8s infinite ease-in-out;
        pointer-events: none;
        z-index: 0;
        text-shadow: 0 0 20px rgba(137, 207, 240, 0.3);
    }

    /* ========== SIDEBAR - GLASSMORPHISM ========== */
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.15) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-right: 2px solid rgba(255, 255, 255, 0.3) !important;
        box-shadow: 4px 0 24px rgba(137, 207, 240, 0.2),
                    inset -1px 0 10px rgba(255, 255, 255, 0.3) !important;
    }

    /* Gradient overlay on sidebar */
    [data-testid="stSidebar"]::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(180deg,
            rgba(137, 207, 240, 0.1) 0%,
            rgba(255, 182, 193, 0.05) 50%,
            rgba(230, 230, 250, 0.1) 100%);
        pointer-events: none;
        z-index: 0;
    }

    /* Floating sparkle in sidebar */
    [data-testid="stSidebar"]::after {
        content: '✨';
        position: absolute;
        top: 15%;
        right: 15%;
        font-size: 24px;
        animation: sparkleTrail 4s infinite ease-in-out;
        --x: -20px;
        --y: -30px;
        pointer-events: none;
        z-index: 1;
    }

    /* ========== MAIN HEADER - PLAYFUL 90's STYLE ========== */
    .main-header {
        text-align: center;
        font-size: 4em;
        font-weight: 700;
        padding: 50px 40px 40px 40px;
        background: linear-gradient(135deg,
            var(--baby-blue) 0%,
            var(--lavender) 30%,
            var(--soft-pink) 70%,
            var(--sunshine) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        position: relative;
        letter-spacing: 2px;
        margin-bottom: 30px;
        filter: drop-shadow(0 4px 8px rgba(137, 207, 240, 0.3));
        animation: bounceIn 1s ease-out;
    }

    /* Sparkle trail decorations */
    .main-header::before {
        content: '✨';
        position: absolute;
        top: 15px;
        left: 10%;
        font-size: 0.4em;
        animation: sparkleTrail 5s infinite ease-in-out;
        --x: 30px;
        --y: -20px;
        filter: drop-shadow(0 2px 8px rgba(255, 244, 79, 0.6));
    }

    .main-header::after {
        content: '💫';
        position: absolute;
        top: 15px;
        right: 10%;
        font-size: 0.4em;
        animation: sparkleTrail 5s infinite ease-in-out 1.5s;
        --x: -30px;
        --y: -20px;
        filter: drop-shadow(0 2px 8px rgba(255, 182, 193, 0.6));
    }

    /* ========== COUNTDOWN BOX - GLASSMORPHISM BUBBLE ========== */
    .countdown-box {
        background: rgba(255, 255, 255, 0.25) !important;
        backdrop-filter: blur(15px) !important;
        -webkit-backdrop-filter: blur(15px) !important;
        padding: 45px 50px !important;
        border-radius: 40px !important;
        width: 550px !important;
        max-width: 90% !important;
        margin: 30px auto !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        color: var(--baby-blue) !important;
        text-align: center !important;
        font-size: 2.2em !important;
        font-weight: 700 !important;
        box-shadow: 0 8px 32px rgba(137, 207, 240, 0.25),
                    inset 0 2px 15px rgba(255, 255, 255, 0.4),
                    0 0 50px rgba(255, 182, 193, 0.15) !important;
        border: 3px solid rgba(255, 255, 255, 0.3) !important;
        position: relative !important;
        overflow: visible !important;
        text-shadow: 0 2px 10px rgba(255, 255, 255, 0.5) !important;
        animation: gentlePulse 4s infinite ease-in-out;
    }

    /* Shine effect on countdown */
    .countdown-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 50%;
        height: 100%;
        background: linear-gradient(
            90deg,
            transparent,
            rgba(255, 255, 255, 0.5),
            transparent
        );
        animation: disneyShine 6s infinite;
        border-radius: 40px;
        z-index: 1;
    }

    /* Sparkle decoration */
    .countdown-box::after {
        content: '⭐';
        position: absolute;
        top: -15px;
        right: 30px;
        font-size: 1.5em;
        animation: sparkleTrail 4s infinite ease-in-out;
        --x: 15px;
        --y: 15px;
        filter: drop-shadow(0 0 10px rgba(255, 244, 79, 0.8));
    }

    /* ========== CHECKLIST CARDS - GLASSMORPHISM BUBBLES ========== */
    .checklist-card {
        width: 100% !important;
        min-height: 160px !important;
        padding: 28px 24px !important;
        margin-bottom: 25px !important;
        border-radius: 30px !important;
        background: rgba(255, 255, 255, 0.3) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border: 2px solid rgba(255, 255, 255, 0.4) !important;
        box-shadow: 0 8px 32px rgba(137, 207, 240, 0.2),
                    inset 0 2px 10px rgba(255, 255, 255, 0.3),
                    0 4px 16px rgba(255, 182, 193, 0.1) !important;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
        cursor: pointer !important;
        position: relative !important;
        overflow: visible !important;
    }

    /* Floating bubble decoration */
    .checklist-card::before {
        content: '○' !important;
        position: absolute !important;
        top: -12px !important;
        right: 20px !important;
        font-size: 28px !important;
        color: rgba(137, 207, 240, 0.4) !important;
        text-shadow: 0 0 10px rgba(137, 207, 240, 0.3) !important;
        animation: bubbleFloat 6s infinite ease-in-out !important;
        z-index: 0 !important;
    }

    .checklist-card:hover {
        transform: translateY(-8px) scale(1.02) !important;
        box-shadow: 0 12px 48px rgba(137, 207, 240, 0.35),
                    inset 0 2px 15px rgba(255, 255, 255, 0.5),
                    0 0 40px rgba(255, 182, 193, 0.25) !important;
        border-color: rgba(255, 244, 79, 0.6) !important;
    }

    .checklist-card.completed {
        opacity: 0.7 !important;
        background: rgba(230, 230, 250, 0.2) !important;
        filter: saturate(0.7) !important;
    }

    .checklist-card.completed::after {
        content: '✓' !important;
        position: absolute !important;
        top: 50% !important;
        left: 50% !important;
        transform: translate(-50%, -50%) rotate(-12deg) !important;
        font-size: 90px !important;
        color: rgba(137, 207, 240, 0.2) !important;
        font-weight: 900 !important;
        z-index: 1 !important;
        animation: checkPop 0.6s cubic-bezier(0.68, -0.55, 0.27, 1.55) !important;
        pointer-events: none !important;
    }

    @keyframes checkPop {
        0% { transform: translate(-50%, -50%) rotate(-12deg) scale(0); opacity: 0; }
        50% { transform: translate(-50%, -50%) rotate(-12deg) scale(1.2); opacity: 1; }
        100% { transform: translate(-50%, -50%) rotate(-12deg) scale(1); opacity: 1; }
    }

    .checklist-card-content {
        position: relative !important;
        z-index: 2 !important;
    }

    .checklist-card strong {
        color: var(--baby-blue) !important;
        font-size: 1.15em !important;
        font-weight: 600 !important;
        display: block !important;
        margin-bottom: 12px !important;
        line-height: 1.5 !important;
        text-shadow: 0 1px 3px rgba(255, 255, 255, 0.8) !important;
    }

    .checklist-card small {
        color: var(--soft-pink) !important;
        font-size: 0.9em !important;
        display: block !important;
        margin-top: 8px !important;
        font-weight: 500 !important;
    }

    .card-checkbox-container {
        display: flex !important;
        align-items: flex-start !important;
        gap: 12px !important;
        margin-bottom: 8px !important;
    }

    /* Card Action Buttons - Small and Clean */
    .card-actions {
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        gap: 12px !important;
        margin-top: 12px !important;
        padding: 0 4px !important;
    }

    /* Card action row - force proper layout with LEFT alignment */
    .card-action-row {
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        width: 100% !important;
        gap: 10px !important;
        margin-top: 10px !important;
        margin-left: 0 !important;
        padding: 0 !important;
    }

    /* Target Streamlit column wrappers directly */
    .card-action-row [data-testid="column"] {
        padding: 0 !important;
        margin: 0 !important;
    }

    .card-action-row [data-testid="column"]:first-child {
        flex: 1 1 auto !important;
        min-width: 0 !important;
        max-width: calc(100% - 46px) !important;
        padding-right: 10px !important;
        text-align: left !important;
    }

    .card-action-row [data-testid="column"]:last-child {
        flex: 0 0 auto !important;
        width: 40px !important;
        max-width: 40px !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* Checkbox container in card actions */
    .card-action-row .stCheckbox {
        margin: 0 !important;
        padding: 4px 8px !important;
        width: auto !important;
        display: inline-flex !important;
        align-items: center !important;
    }

    /* Small delete button for cards - SMALLER SIZE */
    .card-delete-btn .stButton,
    .card-delete-btn {
        width: 36px !important;
        max-width: 36px !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    .card-delete-btn .stButton>button,
    .card-delete-btn button {
        background: linear-gradient(135deg, #ffcdd2 0%, #ef9a9a 100%) !important;
        border: 2px solid #e57373 !important;
        border-radius: 50% !important;
        width: 36px !important;
        height: 36px !important;
        min-width: 36px !important;
        min-height: 36px !important;
        max-width: 36px !important;
        max-height: 36px !important;
        padding: 0 !important;
        margin: 0 !important;
        font-size: 18px !important;
        line-height: 1 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        box-shadow: 0 2px 8px rgba(239, 83, 80, 0.3) !important;
        transition: all 0.3s ease !important;
        text-transform: none !important;
        letter-spacing: normal !important;
        overflow: hidden !important;
    }

    .card-delete-btn .stButton>button::before,
    .card-delete-btn .stButton>button::after,
    .card-delete-btn button::before,
    .card-delete-btn button::after {
        content: none !important;
        display: none !important;
    }

    .card-delete-btn .stButton>button:hover,
    .card-delete-btn button:hover {
        background: linear-gradient(135deg, #ef5350 0%, #e53935 100%) !important;
        transform: scale(1.1) rotate(10deg) !important;
        box-shadow: 0 4px 12px rgba(239, 83, 80, 0.5) !important;
        animation: none !important;
        border-width: 2px !important;
    }

    /* Checkbox label alignment */
    .stCheckbox label {
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
        font-size: 14px !important;
        color: #546e7a !important;
        font-weight: 600 !important;
    }

    /* Ensure no extra padding in card action columns */
    .card-action-row [data-testid="column"] {
        padding: 0 5px !important;
        gap: 0 !important;
    }

    .card-action-row [data-testid="column"]:first-child {
        padding-right: 8px !important;
    }

    .card-action-row [data-testid="column"]:last-child {
        padding-left: 0 !important;
    }

    /* ========== IDEA CARDS - GLASSMORPHISM BUBBLES ========== */
    .idea-card {
        padding: 35px !important;
        margin: 25px auto !important;
        border-radius: 35px !important;
        width: 100% !important;
        max-width: 480px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        background: rgba(255, 255, 255, 0.35) !important;
        backdrop-filter: blur(15px) !important;
        -webkit-backdrop-filter: blur(15px) !important;
        box-shadow: 0 8px 32px rgba(255, 182, 193, 0.25),
                    inset 0 2px 12px rgba(255, 255, 255, 0.4),
                    0 4px 16px rgba(137, 207, 240, 0.15) !important;
        border: 3px solid rgba(255, 255, 255, 0.4) !important;
        color: var(--baby-blue) !important;
        position: relative !important;
        overflow: visible !important;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
        cursor: pointer !important;
        animation: gentlePulse 6s infinite ease-in-out;
    }

    /* Light bulb idea decoration */
    .idea-card::before {
        content: '💡';
        position: absolute;
        top: -18px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 32px;
        filter: drop-shadow(0 0 12px rgba(255, 244, 79, 0.8));
        animation: bounceIn 1.5s ease-out;
    }

    .idea-card:hover {
        transform: translateY(-10px) scale(1.04) rotate(1deg);
        box-shadow: 0 12px 48px rgba(255, 182, 193, 0.4),
                    inset 0 2px 18px rgba(255, 255, 255, 0.5),
                    0 0 50px rgba(255, 244, 79, 0.3);
        border-color: rgba(255, 244, 79, 0.7);
    }

    /* Sparkle trail */
    .idea-card::after {
        content: '✨';
        position: absolute;
        top: 25px;
        right: 25px;
        font-size: 2em;
        animation: sparkleTrail 5s infinite ease-in-out;
        --x: 15px;
        --y: 20px;
        filter: drop-shadow(0 0 8px rgba(255, 244, 79, 0.6));
    }

    .idea-card h3 {
        color: var(--soft-pink) !important;
        font-weight: 600 !important;
        text-align: center;
        margin-bottom: 12px;
        text-shadow: 0 2px 6px rgba(255, 255, 255, 0.6);
    }

    .idea-card p {
        color: var(--lavender) !important;
        text-align: center;
        font-size: 1em;
        line-height: 1.6;
    }

    .idea-card small {
        color: var(--baby-blue) !important;
        text-align: center;
        display: block;
        margin-top: 12px;
        font-weight: 500;
    }

    /* ========== BUTTONS - GLASSMORPHISM WITH SHINE ========== */
    .stButton>button {
        background: rgba(137, 207, 240, 0.3);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        color: var(--baby-blue);
        border: 2px solid rgba(255, 255, 255, 0.4);
        border-radius: 50px !important;
        padding: 14px 36px;
        min-width: 140px;
        font-weight: 600;
        font-size: 16px;
        box-shadow: 0 8px 24px rgba(137, 207, 240, 0.25),
                    inset 0 2px 8px rgba(255, 255, 255, 0.3);
        transition: all 0.4s cubic-bezier(0.68, -0.55, 0.27, 1.55);
        cursor: pointer;
        position: relative;
        overflow: hidden;
        text-transform: none;
        letter-spacing: 0.5px;
        font-family: 'Fredoka', sans-serif !important;
        text-shadow: 0 1px 3px rgba(255, 255, 255, 0.5);
    }

    /* Disney shine effect on buttons */
    .stButton>button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 50%;
        height: 100%;
        background: linear-gradient(
            90deg,
            transparent,
            rgba(255, 255, 255, 0.6),
            transparent
        );
        transition: left 0.6s ease;
    }

    .stButton>button:hover::before {
        left: 200%;
    }

    .stButton>button:hover {
        background: rgba(255, 182, 193, 0.4);
        color: var(--soft-pink);
        box-shadow: 0 12px 40px rgba(255, 182, 193, 0.4),
                    inset 0 2px 12px rgba(255, 255, 255, 0.4),
                    0 0 30px rgba(255, 244, 79, 0.3);
        border-color: rgba(255, 244, 79, 0.5);
        transform: translateY(-4px) scale(1.05);
    }

    .stButton>button:active {
        transform: scale(0.95);
    }

    /* OVERRIDE: Card delete button - SMALLER 36px - placed AFTER general button styles */
    .card-action-row .card-delete-btn .stButton>button,
    .card-delete-btn .stButton>button {
        background: linear-gradient(135deg, #ffcdd2 0%, #ef9a9a 100%) !important;
        border: 2px solid #e57373 !important;
        border-radius: 50% !important;
        width: 36px !important;
        height: 36px !important;
        min-width: 36px !important;
        min-height: 36px !important;
        max-width: 36px !important;
        max-height: 36px !important;
        padding: 0 !important;
        margin: 0 !important;
        font-size: 18px !important;
        line-height: 1 !important;
        text-transform: none !important;
        letter-spacing: 0 !important;
        overflow: hidden !important;
    }

    .card-action-row .card-delete-btn .stButton>button::before,
    .card-action-row .card-delete-btn .stButton>button::after,
    .card-delete-btn .stButton>button::before,
    .card-delete-btn .stButton>button::after {
        content: none !important;
        display: none !important;
    }

    .card-action-row .card-delete-btn .stButton>button:hover,
    .card-delete-btn .stButton>button:hover {
        background: linear-gradient(135deg, #ef5350 0%, #e53935 100%) !important;
        transform: scale(1.1) rotate(10deg) !important;
        animation: none !important;
        border-width: 2px !important;
    }

    /* Priority colors - adjusted for light theme */
    .priority-high {
        border-left-color: #e74c3c;
        background: linear-gradient(135deg, #fff5f5 0%, #ffe6e6 100%);
    }
    .priority-medium {
        border-left-color: #f39c12;
        background: linear-gradient(135deg, #fffef5 0%, #fff8e1 100%);
    }
    .priority-low {
        border-left-color: #27ae60;
        background: linear-gradient(135deg, #f5fff5 0%, #e8f5e9 100%);
    }

    /* ========== INPUT FIELDS - GLASSMORPHISM ========== */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stDateInput > div > div > input {
        color: var(--baby-blue) !important;
        background: rgba(255, 255, 255, 0.4) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        border: 2px solid rgba(255, 255, 255, 0.5) !important;
        border-radius: 25px !important;
        padding: 12px 20px !important;
        box-shadow: inset 0 2px 8px rgba(137, 207, 240, 0.1),
                    0 4px 12px rgba(137, 207, 240, 0.15) !important;
        font-family: 'Quicksand', sans-serif !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
    }

    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus,
    .stDateInput > div > div > input:focus {
        border-color: rgba(255, 182, 193, 0.6) !important;
        box-shadow: 0 0 24px rgba(255, 182, 193, 0.4),
                    inset 0 2px 8px rgba(137, 207, 240, 0.15),
                    0 0 40px rgba(255, 244, 79, 0.2) !important;
        background: rgba(255, 255, 255, 0.5) !important;
    }

    .stSelectbox > div > div > div,
    .stMultiSelect > div > div > div {
        color: var(--baby-blue) !important;
        background: rgba(255, 255, 255, 0.35) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        border: 2px solid rgba(255, 255, 255, 0.4) !important;
        border-radius: 25px !important;
        padding: 10px 18px !important;
        box-shadow: 0 4px 12px rgba(137, 207, 240, 0.15) !important;
    }

    /* Text area - Glassmorphism */
    .stTextArea > div > div > textarea {
        border-radius: 25px !important;
        border: 2px solid rgba(255, 255, 255, 0.4) !important;
        padding: 14px 18px !important;
        background: rgba(255, 255, 255, 0.35) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        color: var(--baby-blue) !important;
    }

    /* Labels - Playful 90's style */
    label {
        color: var(--soft-pink) !important;
        font-weight: 600 !important;
        font-family: 'Fredoka', sans-serif !important;
        text-transform: none !important;
        letter-spacing: 0.3px;
        font-size: 15px !important;
        text-shadow: 0 1px 3px rgba(255, 255, 255, 0.6) !important;
    }

    /* ========== TABS - GLASSMORPHISM PILLS ========== */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 50px !important;
        padding: 8px;
        border: 2px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 24px rgba(137, 207, 240, 0.2),
                    inset 0 2px 8px rgba(255, 255, 255, 0.3);
    }

    .stTabs [data-baseweb="tab"] {
        color: var(--baby-blue) !important;
        font-weight: 600 !important;
        border-radius: 50px !important;
        padding: 12px 24px !important;
        margin: 0 4px;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        font-family: 'Fredoka', sans-serif !important;
        text-transform: none;
        letter-spacing: 0.3px;
        background: rgba(255, 255, 255, 0.2);
        border: 2px solid transparent;
        box-shadow: 0 2px 8px rgba(137, 207, 240, 0.1);
    }

    .stTabs [data-baseweb="tab"]:hover {
        transform: translateY(-2px) scale(1.05);
        background: rgba(255, 182, 193, 0.3);
        color: var(--soft-pink) !important;
        box-shadow: 0 6px 18px rgba(255, 182, 193, 0.25);
        border-color: rgba(255, 244, 79, 0.4);
    }

    .stTabs [aria-selected="true"] {
        background: rgba(137, 207, 240, 0.4) !important;
        color: white !important;
        border-radius: 50px !important;
        box-shadow: 0 8px 24px rgba(137, 207, 240, 0.35),
                    inset 0 2px 10px rgba(255, 255, 255, 0.4),
                    0 0 30px rgba(255, 244, 79, 0.2) !important;
        border-color: rgba(255, 255, 255, 0.5) !important;
        text-shadow: 0 2px 6px rgba(137, 207, 240, 0.5) !important;
    }

    /* Progress bar - light blue */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #87ceeb 0%, #5dade2 100%);
    }

    /* Metrics - light styled */
    [data-testid="stMetricValue"] {
        color: #1e88e5 !important;
        font-weight: 700;
    }

    /* Chat messages - PILL SHAPED */
    .stChatMessage {
        background: linear-gradient(135deg, #ffffff 0%, #f8fbff 100%) !important;
        border: 3px solid #b0e0e6;
        border-radius: 50px !important;  /* PILL SHAPE! */
        padding: 15px 25px !important;
        box-shadow: 0 3px 12px rgba(135, 206, 235, 0.3);
    }

    /* Triangle decorative elements */
    .main::after {
        content: '';
        position: fixed;
        bottom: 10%;
        left: 5%;
        width: 0;
        height: 0;
        border-left: 30px solid transparent;
        border-right: 30px solid transparent;
        border-bottom: 52px solid rgba(135, 206, 235, 0.3);
        animation: float 5s infinite ease-in-out;
        pointer-events: none;
        z-index: 1;
    }

    [data-testid="stSidebar"]::after {
        content: '';
        position: absolute;
        bottom: 15%;
        left: 10%;
        width: 0;
        height: 0;
        border-left: 25px solid transparent;
        border-right: 25px solid transparent;
        border-bottom: 43px solid rgba(255, 215, 0, 0.4);
        animation: sparkle 3s infinite;
    }

    /* Expandable sections - DIAMOND-ISH */
    .streamlit-expanderHeader {
        border-radius: 15px !important;
        border: 3px solid #b0e0e6 !important;
        background: linear-gradient(135deg, #ffffff 0%, #f0f8ff 100%) !important;
        padding: 15px 20px !important;
    }

    /* Metric containers - CIRCLES */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, #ffffff 0%, #f8fbff 100%);
        border-radius: 50% !important;
        padding: 20px !important;
        border: 4px solid rgba(135, 206, 235, 0.4);
        box-shadow: 0 5px 15px rgba(135, 206, 235, 0.3);
        min-width: 120px;
        min-height: 120px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    /* Sparkle decorations throughout */
    h1::before, h2::before {
        content: '✨ ';
    }

    h1::after, h2::after {
        content: ' ✨';
    }

    /* Silver shimmer effect on hover for cards */
    .checklist-item::before,
    .idea-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(
            90deg,
            transparent,
            rgba(192, 192, 192, 0.2),
            transparent
        );
        transition: left 0.5s;
    }

    .checklist-item:hover::before,
    .idea-card:hover::before {
        left: 100%;
    }

    /* Trip code box - ROYAL BANNER */
    /* ========== TRIP CODE BOX - GLASSMORPHISM ========== */
    .trip-code-diamond {
        background: rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        padding: 40px 60px;
        border-radius: 40px;
        border: 3px solid rgba(255, 255, 255, 0.4);
        text-align: center;
        margin: 30px auto;
        max-width: 700px;
        box-shadow: 0 12px 40px rgba(137, 207, 240, 0.3),
                    inset 0 2px 12px rgba(255, 255, 255, 0.4),
                    0 0 50px rgba(255, 182, 193, 0.15);
        position: relative;
        animation: gentlePulse 5s infinite ease-in-out;
    }

    /* Sparkle decoration */
    .trip-code-diamond::before {
        content: '🎟️';
        position: absolute;
        top: -20px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 36px;
        filter: drop-shadow(0 0 15px rgba(255, 244, 79, 0.8));
        animation: bounceIn 1.2s ease-out;
    }

    .trip-code-diamond h3 {
        color: var(--baby-blue);
        margin: 0;
        font-size: 2.2em;
        font-weight: 700;
        text-shadow: 0 2px 8px rgba(255, 255, 255, 0.6);
        font-family: 'Fredoka', sans-serif !important;
        letter-spacing: 1px;
    }

    .trip-code-diamond p {
        color: var(--soft-pink);
        margin: 15px 0 0 0;
        font-size: 1.1em;
        text-shadow: 0 1px 4px rgba(255, 255, 255, 0.5);
        font-style: normal;
        font-weight: 500;
    }

    /* Alert boxes - CIRCULAR/PILL */
    .stAlert {
        border-radius: 50px !important;
        border-width: 3px !important;
        padding: 15px 30px !important;
    }

    /* Success/Info/Error boxes - PILL SHAPED */
    [data-testid="stNotification"] {
        border-radius: 50px !important;
        border-width: 3px !important;
    }

    /* Streamlit column overrides - remove square containers */
    [data-testid="column"] {
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
    }

    [data-testid="stVerticalBlock"] > div {
        background: transparent !important;
        border: none !important;
    }

    [data-testid="stHorizontalBlock"] {
        background: transparent !important;
        border: none !important;
    }

    /* Remove square borders from Streamlit containers */
    .element-container {
        border: none !important;
        background: transparent !important;
    }

    .stMarkdown {
        border: none !important;
        background: transparent !important;
    }

    /* Ensure our custom divs display properly */
    .stMarkdown > div {
        border: none !important;
        background: transparent !important;
    }

    /* MICKEY EARS CHECKBOXES - Soft and Magical (SMALLER) */
    input[type="checkbox"] {
        appearance: none !important;
        -webkit-appearance: none !important;
        width: 36px !important;
        height: 36px !important;
        min-width: 36px !important;
        background: linear-gradient(135deg, #e8e8e8 0%, #d3d3d3 100%) !important;
        border-radius: 50% !important;
        position: relative !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2),
                    inset 0 2px 0 rgba(255, 255, 255, 0.3) !important;
        border: 3px solid #C0C0C0 !important;
    }

    /* Shield decorative elements */
    input[type="checkbox"]::before {
        content: '🛡️' !important;
        position: absolute !important;
        width: 20px !important;
        height: 20px !important;
        background: linear-gradient(135deg, #e8e8e8 0%, #d3d3d3 100%) !important;
        border-radius: 50% !important;
        top: -9px !important;
        left: -3px !important;
        transition: all 0.3s ease !important;
    }

    /* Checkmark when checked */
    input[type="checkbox"]::after {
        content: '✓' !important;
        position: absolute !important;
        width: 20px !important;
        height: 20px !important;
        background: linear-gradient(135deg, #e8e8e8 0%, #d3d3d3 100%) !important;
        border-radius: 50% !important;
        top: -9px !important;
        right: -3px !important;
        transition: all 0.3s ease !important;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5) !important;
    }

    /* Checked state - Royal Gold! */
    input[type="checkbox"]:checked {
        background: linear-gradient(135deg, #FFD700 0%, #FFC107 100%) !important;
        border-color: #DAA520 !important;
        animation: royalPop 0.5s ease-out !important;
        box-shadow: 0 6px 15px rgba(255, 215, 0, 0.6),
                    inset 0 2px 0 rgba(255, 255, 255, 0.4),
                    0 0 20px rgba(255, 215, 0, 0.8) !important;
    }

    input[type="checkbox"]:checked::before {
        opacity: 1 !important;
        filter: brightness(1.3) drop-shadow(0 0 10px rgba(255, 215, 0, 0.8)) !important;
    }

    input[type="checkbox"]:checked::after {
        transform: translate(-50%, -50%) scale(1) !important;
    }

    @keyframes royalPop {
        0% { transform: scale(1); }
        50% { transform: scale(1.15) rotate(5deg); }
        100% { transform: scale(1); }
    }

    /* Filter Controls - Soft Princess Styling */
    .stCheckbox {
        background: linear-gradient(135deg, #fff0f5 0%, #ffe4e9 100%) !important;
        border-radius: 25px !important;
        padding: 12px 20px !important;
        border: 2px solid rgba(255, 192, 203, 0.4) !important;
        box-shadow: 0 2px 8px rgba(255, 182, 193, 0.2) !important;
    }

    .stCheckbox:hover {
        border-color: rgba(255, 192, 203, 0.6) !important;
        box-shadow: 0 3px 12px rgba(255, 182, 193, 0.3) !important;
    }

    .stMultiSelect > div {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 100%) !important;
        border-radius: 25px !important;
        padding: 8px !important;
        border: 2px solid rgba(135, 206, 235, 0.4) !important;
        box-shadow: 0 2px 8px rgba(135, 206, 235, 0.2) !important;
    }

    .stMultiSelect:hover > div {
        border-color: rgba(135, 206, 235, 0.6) !important;
        box-shadow: 0 3px 12px rgba(135, 206, 235, 0.3) !important;
    }

    /* Multi-select tags - soft pastel pills */
    .stMultiSelect [data-baseweb="tag"] {
        background: linear-gradient(135deg, #ffb6c1 0%, #ffc0cb 100%) !important;
        border-radius: 20px !important;
        border: none !important;
        color: #fff !important;
        font-weight: 600 !important;
        padding: 4px 12px !important;
        margin: 2px !important;
    }

    /* Ghost placeholders */
    input::placeholder {
        color: rgba(135, 206, 235, 0.4) !important;
        opacity: 1 !important;
        font-style: italic !important;
    }

    textarea::placeholder {
        color: rgba(135, 206, 235, 0.4) !important;
        opacity: 1 !important;
        font-style: italic !important;
    }

    /* Disney Castle Silhouettes - Floating decorations */
    body::before {
        content: '🏰';
        position: fixed;
        top: 12%;
        right: 6%;
        font-size: 50px;
        opacity: 0.12;
        animation: float 8s infinite ease-in-out;
        pointer-events: none;
        z-index: 0;
        filter: drop-shadow(0 2px 8px rgba(100, 149, 237, 0.3));
    }

    .main::before {
        content: '🌹';
        position: fixed;
        top: 35%;
        left: 3%;
        font-size: 38px;
        opacity: 0.07;
        animation: float 7s infinite ease-in-out 1s;
        pointer-events: none;
        z-index: 0;
        filter: grayscale(20%);
    }

    [data-testid="stSidebar"]::before {
        content: '🪝';
        position: absolute;
        top: 25%;
        right: 10%;
        font-size: 30px;
        opacity: 0.1;
        animation: sparkle 4s infinite;
        pointer-events: none;
        filter: grayscale(15%);
    }

    /* Additional floating silhouettes */
    .stApp::after {
        content: '🧚';
        position: fixed;
        bottom: 20%;
        right: 8%;
        font-size: 32px;
        opacity: 0.09;
        animation: float 5s infinite ease-in-out 2s;
        pointer-events: none;
        z-index: 0;
        filter: grayscale(20%);
    }

    /* Rapunzel's brush - floating decoration */
    .main::after {
        content: '🖌️';
        position: fixed;
        top: 65%;
        right: 4%;
        font-size: 33px;
        opacity: 0.08;
        animation: float 6.5s infinite ease-in-out 1.5s;
        pointer-events: none;
        z-index: 0;
        filter: grayscale(25%);
    }

    /* Login page beautification */
    .trip-code-entry {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 100%);
        padding: 60px 40px;
        border-radius: 30px;
        border: 4px solid rgba(135, 206, 235, 0.5);
        box-shadow: 0 10px 40px rgba(135, 206, 235, 0.3);
        position: relative;
        overflow: hidden;
    }

    .trip-code-entry::before {
        content: '✨';
        position: absolute;
        top: 20px;
        left: 20px;
        font-size: 30px;
        animation: sparkle 2s infinite;
    }

    .trip-code-entry::after {
        content: '🏰';
        position: absolute;
        bottom: 20px;
        right: 20px;
        font-size: 50px;
        opacity: 0.1;
        animation: float 8s infinite ease-in-out;
    }

    /* MOBILE RESPONSIVE - Optimized for iPhone */
    @media screen and (max-width: 768px) {
        /* Make card action rows more spacious on mobile */
        .card-action-row {
            gap: 12px !important;
            padding: 5px 0 !important;
        }

        /* Give more room to checkbox on mobile */
        .card-action-row [data-testid="column"]:first-child {
            max-width: calc(100% - 50px) !important;
            padding-right: 12px !important;
        }

        .card-action-row [data-testid="column"]:last-child {
            width: 38px !important;
            max-width: 38px !important;
            flex-shrink: 0 !important;
        }

        /* Ensure checkbox and button don't overlap on mobile */
        .card-action-row .stCheckbox {
            padding: 2px 6px !important;
            max-width: 100% !important;
        }

        /* Make delete button slightly larger hit target on mobile */
        .card-delete-btn .stButton>button,
        .card-delete-btn button {
            width: 38px !important;
            height: 38px !important;
            min-width: 38px !important;
            min-height: 38px !important;
            max-width: 38px !important;
            max-height: 38px !important;
        }

        /* Adjust Mickey ears for mobile */
        input[type="checkbox"] {
            width: 32px !important;
            height: 32px !important;
            min-width: 32px !important;
        }

        input[type="checkbox"]::before,
        input[type="checkbox"]::after {
            width: 18px !important;
            height: 18px !important;
        }

        /* Expander headers more compact on mobile */
        .streamlit-expanderHeader {
            font-size: 14px !important;
            padding: 8px 12px !important;
        }

        /* Ensure columns stack better on very small screens */
        [data-testid="column"] {
            min-width: auto !important;
        }

        /* Checklist cards - single column on very small screens */
        @media screen and (max-width: 480px) {
            .card-action-row {
                flex-direction: row !important;
                flex-wrap: nowrap !important;
            }

            .card-action-row [data-testid="column"]:first-child {
                flex: 1 !important;
                min-width: 0 !important;
            }

            .card-action-row [data-testid="column"]:last-child {
                flex: 0 0 38px !important;
            }
        }
    }
</style>
""", unsafe_allow_html=True)

# Data persistence functions
DATA_DIR = Path.home() / ".disney_trip_planner"
DATA_FILE = DATA_DIR / "trip_data.pkl"

# Limit data structures to save memory (free tier has 1GB RAM limit)
MAX_CHAT_HISTORY = 50
MAX_IDEAS = 30
MAX_PENDING_SUGGESTIONS = 20

def save_trip_data():
    """Save trip data to Firebase and local disk"""
    # Limit chat history size to conserve memory
    chat_history = st.session_state.chat_history
    if len(chat_history) > MAX_CHAT_HISTORY:
        chat_history = chat_history[-MAX_CHAT_HISTORY:]  # Keep only last 50 messages
        st.session_state.chat_history = chat_history

    # Limit ideas list to conserve memory
    ideas = st.session_state.ideas
    if len(ideas) > MAX_IDEAS:
        ideas = ideas[-MAX_IDEAS:]  # Keep only last 30 ideas
        st.session_state.ideas = ideas

    # Limit pending suggestions to conserve memory
    pending_suggestions = st.session_state.get('pending_suggestions', [])
    if len(pending_suggestions) > MAX_PENDING_SUGGESTIONS:
        pending_suggestions = pending_suggestions[-MAX_PENDING_SUGGESTIONS:]
        st.session_state.pending_suggestions = pending_suggestions

    data = {
        'trip_details': st.session_state.trip_details,
        'checklist': st.session_state.checklist,
        'ideas': ideas,
        'chat_history': chat_history,
        'rejected_items': st.session_state.get('rejected_items', set()),
        'pending_suggestions': pending_suggestions
    }

    # Try Firebase first if trip code is set
    trip_code = st.session_state.get('trip_code')
    if trip_code:
        firebase = get_firebase_manager()
        if firebase.is_enabled():
            try:
                firebase.save_trip(trip_code, data)
            except Exception as e:
                pass  # Fail silently to avoid UI clutter

    # Always save locally as backup (but don't if it fails)
    try:
        DATA_DIR.mkdir(exist_ok=True)
        with open(DATA_FILE, 'wb') as f:
            pickle.dump(data, f)
    except Exception:
        pass  # Fail silently

def load_trip_data(trip_code: str = None):
    """Load trip data from Firebase or local disk"""
    # Try Firebase first if trip code is provided
    if trip_code:
        firebase = get_firebase_manager()
        if firebase.is_enabled():
            try:
                data = firebase.load_trip(trip_code)
                if data:
                    return data
            except Exception as e:
                st.warning(f"Could not load from cloud: {e}")

    # Fall back to local storage
    try:
        if DATA_FILE.exists():
            with open(DATA_FILE, 'rb') as f:
                data = pickle.load(f)
                return data
    except Exception as e:
        st.warning(f"Could not load locally: {e}")

    return None

# Get API key from Streamlit secrets or environment
def get_api_key():
    """Get API key from secrets or environment"""
    # Try Streamlit secrets first (for cloud deployment)
    try:
        if 'OPENAI_API_KEY' in st.secrets:
            return st.secrets['OPENAI_API_KEY']
    except:
        pass

    # Fall back to environment variable (for local)
    return os.getenv('OPENAI_API_KEY')

# Initialize session state
if 'agent' not in st.session_state:
    api_key = get_api_key()
    if api_key:
        st.session_state.agent = TripPlannerAgent(api_key)
    else:
        st.session_state.agent = None

if 'trip_details' not in st.session_state:
    # Try to load saved data
    saved_data = load_trip_data()
    if saved_data:
        st.session_state.trip_details = saved_data.get('trip_details')
        st.session_state.checklist = saved_data.get('checklist', [])

        # Limit loaded data to conserve memory
        ideas = saved_data.get('ideas', [])
        st.session_state.ideas = ideas[-MAX_IDEAS:] if len(ideas) > MAX_IDEAS else ideas

        chat_history = saved_data.get('chat_history', [])
        st.session_state.chat_history = chat_history[-MAX_CHAT_HISTORY:] if len(chat_history) > MAX_CHAT_HISTORY else chat_history

        # Ensure rejected_items is always a set (Firebase returns it as a list)
        rejected = saved_data.get('rejected_items', set())
        st.session_state.rejected_items = set(rejected) if isinstance(rejected, (list, set)) else set()

        pending_suggestions = saved_data.get('pending_suggestions', [])
        st.session_state.pending_suggestions = pending_suggestions[-MAX_PENDING_SUGGESTIONS:] if len(pending_suggestions) > MAX_PENDING_SUGGESTIONS else pending_suggestions
    else:
        st.session_state.trip_details = None
        st.session_state.checklist = []
        st.session_state.ideas = []
        st.session_state.chat_history = []
        st.session_state.rejected_items = set()
        st.session_state.pending_suggestions = []

if 'checklist' not in st.session_state:
    st.session_state.checklist = []

if 'ideas' not in st.session_state:
    st.session_state.ideas = []

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'rejected_items' not in st.session_state:
    st.session_state.rejected_items = set()
else:
    # Ensure it's always a set, even if it somehow became a list
    if not isinstance(st.session_state.rejected_items, set):
        st.session_state.rejected_items = set(st.session_state.rejected_items)

if 'pending_suggestions' not in st.session_state:
    st.session_state.pending_suggestions = []


def main():
    """Main application"""
    # Header
    st.markdown('<h1 class="main-header">🏰 Disney Trip Planning Agent ✨</h1>', unsafe_allow_html=True)

    # Check for API key
    if not st.session_state.agent:
        st.error("⚠️ OpenAI API key not configured!")
        st.info("The API key should be configured in Streamlit Cloud secrets or your .env file")
        st.markdown("""
        **For Streamlit Cloud:** Add `OPENAI_API_KEY` in your app settings → Secrets

        **For Local:** Create a `.env` file with `OPENAI_API_KEY=your_key_here`
        """)
        return

    # Trip Code Setup - Multi-User Collaboration
    if 'trip_code' not in st.session_state:
        st.session_state.trip_code = None

    # Show trip code input if not set or if user wants to change
    if not st.session_state.trip_code:
        st.markdown("---")
        st.subheader("🔐 Trip Code for Multi-User Collaboration")
        st.info("💡 **Share your trip with family and friends!** Enter a trip code to collaborate on planning together. Everyone with the same code can view and edit the trip.")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Create New Trip**")
            new_trip_code = st.text_input(
                "Enter your trip code",
                value="",
                max_chars=50,
                placeholder="e.g., 'Ohboy' or 'DisneyDreams'",
                help="This code will be shared with your travel companions"
            )

            if st.button("🎉 Create New Trip", use_container_width=True):
                if new_trip_code and len(new_trip_code) >= 3:
                    firebase = get_firebase_manager()
                    if firebase.is_enabled():
                        if firebase.trip_exists(new_trip_code):
                            st.error(f"❌ Trip code '{new_trip_code}' already exists! Use 'Join Existing Trip' instead.")
                        else:
                            st.session_state.trip_code = new_trip_code
                            st.success(f"✅ Created trip with code: **{new_trip_code}**")
                            st.info("🔗 Share this code with your travel companions so they can join!")
                            st.rerun()
                    else:
                        # Firebase not configured - use local only
                        st.session_state.trip_code = new_trip_code
                        st.warning("⚠️ Cloud sync not configured. Trip will be saved locally only.")
                        st.rerun()
                else:
                    st.error("Trip code must be at least 3 characters long")

        with col2:
            st.markdown("**Join Existing Trip**")
            join_trip_code = st.text_input(
                "Enter trip code to join",
                value="",
                max_chars=50,
                placeholder="Enter your friend's trip code",
                help="Get this code from your travel companion"
            )

            if st.button("🤝 Join Trip", use_container_width=True):
                if join_trip_code:
                    firebase = get_firebase_manager()
                    if firebase.is_enabled():
                        if firebase.trip_exists(join_trip_code):
                            st.session_state.trip_code = join_trip_code
                            # Load the trip data
                            trip_data = load_trip_data(join_trip_code)
                            if trip_data:
                                st.session_state.trip_details = trip_data.get('trip_details')
                                st.session_state.checklist = trip_data.get('checklist', [])
                                st.session_state.ideas = trip_data.get('ideas', [])
                                st.session_state.chat_history = trip_data.get('chat_history', [])
                                # Ensure rejected_items is always a set (Firebase returns it as a list)
                                rejected = trip_data.get('rejected_items', set())
                                st.session_state.rejected_items = set(rejected) if isinstance(rejected, (list, set)) else set()
                                st.session_state.pending_suggestions = trip_data.get('pending_suggestions', [])
                            st.success(f"✅ Joined trip: **{join_trip_code}**")
                            st.rerun()
                        else:
                            st.error(f"❌ Trip code '{join_trip_code}' not found!")
                    else:
                        st.error("⚠️ Cloud sync not configured. Cannot join remote trips.")
                else:
                    st.error("Please enter a trip code")

        st.markdown("---")
        return

    # Display current trip code - DIAMOND SHAPE!
    st.markdown(f"""
    <div class="trip-code-diamond">
        <h3>💎 Trip Code: {st.session_state.trip_code} 💎</h3>
        <p>Share this code with your travel companions!</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🔄 Change Trip Code"):
            st.session_state.trip_code = None
            st.rerun()

    # Sidebar - Trip Setup
    with st.sidebar:
        st.header("🎯 Your Trip Details")

        # Load saved values if available
        default_destination = st.session_state.trip_details.destination if st.session_state.trip_details else "Walt Disney World"
        default_start = st.session_state.trip_details.start_date.date() if st.session_state.trip_details else datetime.now().date() + timedelta(days=90)
        default_end = st.session_state.trip_details.end_date.date() if st.session_state.trip_details else datetime.now().date() + timedelta(days=94)
        default_party = st.session_state.trip_details.party_size if st.session_state.trip_details else 4
        default_ages = ", ".join(map(str, st.session_state.trip_details.ages)) if st.session_state.trip_details else "8, 10, 35, 37"
        default_interests = st.session_state.trip_details.interests if st.session_state.trip_details else ["Character Meet & Greets", "Fireworks & Parades"]
        default_budget = st.session_state.trip_details.budget_range if st.session_state.trip_details else "Moderate"
        default_needs = st.session_state.trip_details.special_needs if st.session_state.trip_details else []

        destination = st.selectbox(
            "Destination",
            ["Walt Disney World", "Disneyland Resort", "Disneyland Paris",
             "Tokyo Disney Resort", "Hong Kong Disneyland", "Shanghai Disney Resort"],
            index=["Walt Disney World", "Disneyland Resort", "Disneyland Paris",
                   "Tokyo Disney Resort", "Hong Kong Disneyland", "Shanghai Disney Resort"].index(default_destination)
        )

        trip_date = st.date_input(
            "Trip Start Date",
            value=default_start,
            min_value=datetime.now().date()
        )

        trip_end_date = st.date_input(
            "Trip End Date",
            value=default_end,
            min_value=trip_date
        )

        party_size = st.number_input("Party Size", min_value=1, max_value=20, value=default_party)

        ages_input = st.text_input("Ages (comma-separated)", default_ages)
        ages = [int(age.strip()) for age in ages_input.split(',') if age.strip().isdigit()]

        interests = st.multiselect(
            "Interests",
            ["Thrill Rides", "Character Meet & Greets", "Shows & Entertainment",
             "Dining Experiences", "Shopping", "Relaxation", "Photography",
             "Fireworks & Parades", "Water Parks", "Resort Activities"],
            default=default_interests
        )

        budget = st.selectbox(
            "Budget Range",
            ["Budget-Friendly", "Moderate", "Deluxe", "No Budget Constraints"],
            index=["Budget-Friendly", "Moderate", "Deluxe", "No Budget Constraints"].index(default_budget)
        )

        special_needs = st.multiselect(
            "Special Considerations",
            ["Wheelchair Access", "Dietary Restrictions", "First-Time Visitors",
             "Celebrating Special Occasion", "Traveling with Toddlers", "Traveling with Teens"],
            default=default_needs
        )

        if st.button("🚀 Create/Update Trip Plan", use_container_width=True):
            with st.spinner("Creating your magical trip plan..."):
                # Convert dates to datetime
                start_dt = datetime.combine(trip_date, datetime.min.time())
                end_dt = datetime.combine(trip_end_date, datetime.min.time())
                start_dt = pytz.UTC.localize(start_dt)
                end_dt = pytz.UTC.localize(end_dt)

                st.session_state.trip_details = TripDetails(
                    destination=destination,
                    start_date=start_dt,
                    end_date=end_dt,
                    party_size=party_size,
                    ages=ages,
                    interests=interests,
                    budget_range=budget,
                    special_needs=special_needs
                )

                # Generate checklist
                st.session_state.checklist = st.session_state.agent.generate_comprehensive_checklist(
                    st.session_state.trip_details
                )

                # Generate initial ideas
                st.session_state.ideas = st.session_state.agent.brainstorm_ideas(
                    st.session_state.trip_details
                )

                # Save data
                save_trip_data()

                st.success("✅ Trip plan created and saved!")
                st.rerun()

    # Main content
    if not st.session_state.trip_details:
        st.info("👈 Start by entering your trip details in the sidebar and click 'Create Trip Plan'")
        st.markdown("""
        ### Welcome to Your Disney Trip Planning Agent! 🎉

        This AI-powered assistant will help you with:
        - ✅ **Comprehensive packing checklists** (never forget the essentials!)
        - 💡 **Creative trip ideas** and suggestions
        - ⏰ **Countdown timer** to your magical adventure
        - 🤖 **AI assistant** for all your Disney questions

        ### 💾 Your Trip is Always Saved!
        - **Everything is saved automatically** - trip details, checklists, checked items, chat history
        - **Come back anytime** - your trip will be right here waiting for you
        - **No login needed** - your data is securely saved on your device
        - **Close and reopen** - everything will be exactly as you left it!
        """)
        return

    # Countdown Timer
    st.markdown("---")
    days, hours, minutes, seconds = calculate_countdown(st.session_state.trip_details.start_date)
    countdown_text = format_countdown(days, hours, minutes, seconds)

    st.markdown(f"""
    <div class="countdown-box">
        ⏰ {countdown_text} until your magical adventure! 🎉
    </div>
    """, unsafe_allow_html=True)

    # Tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs([
        "✅ Checklists",
        "💡 Ideas & Suggestions",
        "🤖 AI Assistant",
        "📋 Trip Summary"
    ])

    # Tab 1: Checklists
    with tab1:
        st.header("Trip Planning Checklist")

        # Top row: Subheader on left, Add Custom Item on right - MOBILE OPTIMIZED
        top_col1, top_col2 = st.columns([3, 2])
        with top_col1:
            st.subheader("Your Personalized Checklist")
        with top_col2:
            # Add custom item - compact version
            with st.expander("➕ Add Item", expanded=False):
                new_item_text = st.text_input("Item description", key="new_item", placeholder="e.g., Pack sunscreen")
                new_col1, new_col2 = st.columns(2)
                with new_col1:
                    new_item_category = st.text_input("Category", "custom", key="new_category")
                with new_col2:
                    new_item_priority = st.selectbox("Priority", ["high", "medium", "low"], key="new_priority")

                if st.button("Add to Checklist", use_container_width=True) and new_item_text:
                    from src.utils.helpers import generate_checklist_id
                    new_item = ChecklistItem(
                        id=generate_checklist_id(),
                        text=new_item_text,
                        category=new_item_category,
                        priority=new_item_priority,
                        completed=False
                    )
                    st.session_state.checklist.append(new_item)
                    save_trip_data()
                    st.success(f"✅ Added: {new_item_text}")
                    st.rerun()

        # Action buttons row - MOBILE OPTIMIZED (simplified layout)
        if st.button("🔍 Find Forgotten Items", use_container_width=True):
            with st.spinner("Analyzing checklist..."):
                # Get AI suggestions
                forgotten = st.session_state.agent.suggest_forgotten_items(
                    st.session_state.checklist
                )

                if forgotten:
                    # Get current checklist item texts (lowercase for comparison)
                    existing_items = {item.text.lower().strip() for item in st.session_state.checklist}

                    # Filter out duplicates and rejected items
                    new_items = []
                    for item_text in forgotten:
                        item_lower = item_text.lower().strip()
                        if item_lower not in existing_items and item_lower not in st.session_state.rejected_items:
                            new_items.append(item_text)

                    if new_items:
                        # Add new items to checklist
                        from src.utils.helpers import generate_checklist_id
                        for item_text in new_items:
                            new_item = ChecklistItem(
                                id=generate_checklist_id(),
                                text=item_text,
                                category="forgotten-items",
                                priority="medium",
                                completed=False
                            )
                            st.session_state.checklist.append(new_item)

                        # Save data
                        save_trip_data()

                        st.success(f"✅ Added {len(new_items)} forgotten item{'s' if len(new_items) != 1 else ''} to your checklist!")
                        st.rerun()
                    else:
                        st.info("✨ Great job! You haven't forgotten anything important.")

        # Collapsible Filter options - EASY TO FIND
        with st.expander("🔍 Filters", expanded=False):
            filter_col1, filter_col2, filter_col3 = st.columns(3)
            with filter_col1:
                show_completed = st.checkbox("Show Completed", value=True)
            with filter_col2:
                priority_filter = st.multiselect(
                    "Filter by Priority",
                    ["high", "medium", "low"],
                    default=["high", "medium", "low"]
                )
            with filter_col3:
                category_filter = st.multiselect(
                    "Filter by Category",
                    list(set([item.category for item in st.session_state.checklist])),
                    default=list(set([item.category for item in st.session_state.checklist]))
                )

        # Display checklist - 3 Cards Per Row Grid
        filtered_items = []
        for idx, item in enumerate(st.session_state.checklist):
            if not show_completed and item.completed:
                continue
            if item.priority not in priority_filter:
                continue
            if item.category not in category_filter:
                continue
            filtered_items.append((idx, item))

        # Display in rows of 3
        for row_idx in range(0, len(filtered_items), 3):
            cols = st.columns(3)

            for col_idx in range(3):
                if row_idx + col_idx < len(filtered_items):
                    idx, item = filtered_items[row_idx + col_idx]

                    with cols[col_idx]:
                        completed_class = "completed" if item.completed else ""
                        priority_class = f"priority-{item.priority}"

                        # Card with checkbox inside
                        st.markdown(f"""
                        <div class="checklist-card {completed_class} {priority_class}">
                            <div class="checklist-card-content">
                                <strong>{item.text}</strong>
                                <small>📁 {item.category} | ⭐ {item.priority.upper()}
                                {f"| 📅 {item.deadline}" if item.deadline else ""}</small>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                        # Checkbox and delete button below the card - wrapped for proper layout
                        st.markdown('<div class="card-action-row">', unsafe_allow_html=True)

                        action_col1, action_col2 = st.columns([7, 1], gap="small")
                        with action_col1:
                            checked = st.checkbox(
                                "Complete",
                                value=item.completed,
                                key=f"check_{idx}",
                                label_visibility="visible"
                            )
                            if checked != item.completed:
                                st.session_state.checklist[idx].completed = checked
                                save_trip_data()

                        with action_col2:
                            st.markdown('<div class="card-delete-btn">', unsafe_allow_html=True)
                            if st.button("🗑️", key=f"delete_{idx}", use_container_width=False):
                                deleted_text = st.session_state.checklist[idx].text.lower().strip()
                                st.session_state.rejected_items.add(deleted_text)
                                st.session_state.checklist.pop(idx)
                                save_trip_data()
                                st.rerun()
                            st.markdown('</div>', unsafe_allow_html=True)

                        st.markdown('</div>', unsafe_allow_html=True)

    # Tab 2: Ideas & Suggestions
    with tab2:
        st.header("💡 Trip Ideas & Suggestions")

        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader("Brainstormed Ideas for Your Trip")
        with col2:
            focus = st.selectbox(
                "Focus",
                ["general", "dining", "activities", "surprises", "budget-friendly", "photos"]
            )
            if st.button("🔄 Generate New Ideas"):
                with st.spinner("Brainstorming magical ideas..."):
                    new_ideas = st.session_state.agent.brainstorm_ideas(
                        st.session_state.trip_details,
                        focus=focus
                    )
                    st.session_state.ideas.extend(new_ideas)
                    save_trip_data()
                    st.rerun()

        # Display ideas
        for idx, idea in enumerate(st.session_state.ideas):
            st.markdown(f"""
            <div class="idea-card">
                <h3>{idea.title}</h3>
                <p>{idea.description}</p>
                <small>🏷️ {idea.category} | Tags: {', '.join(idea.tags)}</small>
            </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns([6, 1])
            with col2:
                if st.button("💾" if not idea.saved else "❤️", key=f"save_idea_{idx}"):
                    st.session_state.ideas[idx].saved = not idea.saved
                    save_trip_data()
                    st.rerun()

    # Tab 3: AI Assistant
    with tab3:
        st.header("🤖 AI Trip Planning Assistant")
        st.write("Ask me anything about your Disney trip!")
        st.info("💡 **Pro tip:** I can help you add items to your checklist! Just tell me what you need to remember, or I'll proactively suggest items based on our conversation.")

        # Chat interface
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        # Display any pending suggested items from the last AI response
        if 'pending_suggestions' in st.session_state and st.session_state.pending_suggestions:
            st.markdown("---")
            st.markdown("### ✨ Suggested Checklist Items")
            st.write("The AI assistant has some suggestions for your checklist:")

            for idx, suggestion in enumerate(st.session_state.pending_suggestions):
                col1, col2, col3 = st.columns([4, 1, 1])
                with col1:
                    priority_emoji = {"high": "🔴", "medium": "🟡", "low": "🟢"}
                    emoji = priority_emoji.get(suggestion.get('priority', 'medium'), '🟡')
                    st.markdown(f"{emoji} **{suggestion['text']}**")
                    st.caption(f"Category: {suggestion['category']} | Priority: {suggestion['priority']}")
                with col2:
                    if st.button("➕ Add", key=f"add_suggestion_{idx}"):
                        # Add to checklist
                        from src.utils.helpers import generate_checklist_id
                        new_item = ChecklistItem(
                            id=generate_checklist_id(),
                            text=suggestion['text'],
                            category=suggestion['category'],
                            priority=suggestion['priority'],
                            completed=False
                        )
                        st.session_state.checklist.append(new_item)

                        # Remove this suggestion from pending
                        st.session_state.pending_suggestions.pop(idx)

                        # Save data
                        save_trip_data()

                        st.success(f"✅ Added '{suggestion['text']}' to your checklist!")
                        st.rerun()
                with col3:
                    if st.button("❌ Skip", key=f"skip_suggestion_{idx}"):
                        # Add to rejected items
                        rejected_text = suggestion['text'].lower().strip()
                        st.session_state.rejected_items.add(rejected_text)

                        # Remove this suggestion from pending
                        st.session_state.pending_suggestions.pop(idx)

                        # Save data
                        save_trip_data()
                        st.rerun()

            if st.button("❌ Skip All Suggestions"):
                # Add all to rejected items
                for suggestion in st.session_state.pending_suggestions:
                    rejected_text = suggestion['text'].lower().strip()
                    st.session_state.rejected_items.add(rejected_text)

                st.session_state.pending_suggestions = []
                save_trip_data()
                st.rerun()

            st.markdown("---")

        # User input
        user_question = st.chat_input("Ask a question about your trip...")

        if user_question:
            # Add user message
            st.session_state.chat_history.append({
                "role": "user",
                "content": user_question
            })

            # Get AI response
            with st.spinner("Thinking..."):
                response = st.session_state.agent.get_personalized_suggestion(
                    st.session_state.trip_details,
                    user_question
                )

            # Parse response for suggested items
            from src.agents.trip_planner_agent import TripPlannerAgent
            cleaned_response, suggested_items = TripPlannerAgent.parse_item_suggestions(response)

            # Filter out duplicates and rejected items
            if suggested_items:
                existing_items = {item.text.lower().strip() for item in st.session_state.checklist}
                filtered_suggestions = []

                for suggestion in suggested_items:
                    suggestion_lower = suggestion['text'].lower().strip()
                    if suggestion_lower not in existing_items and suggestion_lower not in st.session_state.rejected_items:
                        filtered_suggestions.append(suggestion)

                # Store filtered suggestions in session state
                st.session_state.pending_suggestions = filtered_suggestions

            # Add cleaned assistant message (without [ADD_ITEM...] tags)
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": cleaned_response
            })

            # Save chat history
            save_trip_data()

            st.rerun()

    # Tab 4: Trip Summary
    with tab4:
        st.header("📋 Trip Summary")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Trip Details")
            st.write(f"**Destination:** {st.session_state.trip_details.destination}")
            st.write(f"**Start Date:** {st.session_state.trip_details.start_date.strftime('%B %d, %Y')}")
            st.write(f"**End Date:** {st.session_state.trip_details.end_date.strftime('%B %d, %Y')}")
            trip_length = (st.session_state.trip_details.end_date - st.session_state.trip_details.start_date).days
            st.write(f"**Trip Length:** {trip_length} days")
            st.write(f"**Party Size:** {st.session_state.trip_details.party_size}")
            st.write(f"**Ages:** {', '.join(map(str, st.session_state.trip_details.ages))}")

        with col2:
            st.subheader("Planning Progress")
            total_items = len(st.session_state.checklist)
            completed_items = sum(1 for item in st.session_state.checklist if item.completed)
            progress = (completed_items / total_items * 100) if total_items > 0 else 0

            st.metric("Checklist Progress", f"{progress:.0f}%")
            st.progress(progress / 100)

            st.metric("Total Tasks", total_items)
            st.metric("Completed", completed_items)
            st.metric("Remaining", total_items - completed_items)

        st.markdown("---")
        st.subheader("Interests & Preferences")
        st.write(f"**Interests:** {', '.join(st.session_state.trip_details.interests)}")
        st.write(f"**Budget:** {st.session_state.trip_details.budget_range}")
        if st.session_state.trip_details.special_needs:
            st.write(f"**Special Considerations:** {', '.join(st.session_state.trip_details.special_needs)}")

        st.markdown("---")
        st.subheader("Data Management")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💾 Save Trip Data"):
                save_trip_data()
                st.success("Trip data saved!")
        with col2:
            if st.button("🗑️ Clear All Data"):
                st.session_state.trip_details = None
                st.session_state.checklist = []
                st.session_state.ideas = []
                st.session_state.chat_history = []
                if DATA_FILE.exists():
                    DATA_FILE.unlink()
                st.success("All data cleared!")
                st.rerun()


if __name__ == "__main__":
    main()
