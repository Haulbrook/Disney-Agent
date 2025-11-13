"""
Disney Trip Planning Agent - Custom Styles Module

This module contains all the custom CSS styling for the Disney Trip Planning Agent
application. It provides a magical Disney Castle theme with sky blue, silver, and
pastel pink color schemes.

Theme Features:
- Custom Disney fonts (Cinzel and Cormorant Garamond)
- Animated effects (sparkle, shimmer, bounce, float, fireworks)
- Castle-themed sidebar with tower decorations
- Countdown box styled as a castle tower with battlements
- Checklist cards styled as castle wall banners/plaques
- Mickey Mouse ear checkboxes with shield decorations
- Circular delete buttons with hover effects
- Royal castle-styled buttons with sparkles
- Tab styling as castle archways
- Pill-shaped chat messages and alerts
- Responsive design for mobile devices
- Floating Disney silhouettes and decorative elements

Usage:
    import streamlit as st
    from src.ui.styles import apply_custom_styles

    # Apply the custom styles to your Streamlit app
    st.markdown(apply_custom_styles(), unsafe_allow_html=True)
"""


def apply_custom_styles() -> str:
    """
    Returns the complete CSS styling for the Disney Trip Planning Agent.

    This function encapsulates all custom CSS styling including:
    - Font imports from Google Fonts
    - CSS animations (sparkle, shimmer, bounce, float, firework, magicPulse, royalPop)
    - Main background with castle sky gradient
    - Sidebar castle tower theme with decorative elements
    - Countdown box styled as a castle tower
    - Checklist card styling with castle banner theme
    - Idea cards as treasure chest scrolls
    - Button styling with royal castle theme
    - Input field styling
    - Tab styling as castle archways
    - Chat interface with pill-shaped messages
    - Mickey Mouse ear checkboxes
    - Circular delete buttons
    - Responsive design for mobile devices
    - Various decorative elements and floating silhouettes

    Returns:
        str: A string containing all CSS within <style> tags, ready to be
             passed to st.markdown() with unsafe_allow_html=True

    Example:
        >>> css = apply_custom_styles()
        >>> st.markdown(css, unsafe_allow_html=True)
    """
    return """
<style>
    /* Import magical Disney fonts */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Cormorant+Garamond:wght@300;400;600;700&display=swap');

    * {
        font-family: 'Cormorant Garamond', serif !important;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Cinzel', serif !important;
    }

    /* Sparkle animation */
    @keyframes sparkle {
        0%, 100% { opacity: 0; transform: scale(0) rotate(0deg); }
        50% { opacity: 1; transform: scale(1) rotate(180deg); }
    }

    @keyframes shimmer {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
    }

    /* Button shimmy/bounce animation */
    @keyframes shimmy {
        0%, 100% { transform: translateX(0) rotate(0deg); }
        25% { transform: translateX(-5px) rotate(-2deg); }
        75% { transform: translateX(5px) rotate(2deg); }
    }

    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    /* Fireworks animation */
    @keyframes firework {
        0% {
            transform: translate(0, 0) scale(0);
            opacity: 1;
        }
        50% {
            opacity: 1;
        }
        100% {
            transform: translate(var(--tx), var(--ty)) scale(1);
            opacity: 0;
        }
    }

    /* Floating sparkles */
    @keyframes float {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(180deg); }
    }

    /* Magical pulse */
    @keyframes magicPulse {
        0%, 100% {
            box-shadow: 0 0 5px rgba(135, 206, 235, 0.5),
                        0 0 10px rgba(135, 206, 235, 0.3),
                        0 0 15px rgba(135, 206, 235, 0.2);
        }
        50% {
            box-shadow: 0 0 20px rgba(135, 206, 235, 0.8),
                        0 0 30px rgba(135, 206, 235, 0.6),
                        0 0 40px rgba(135, 206, 235, 0.4);
        }
    }

    /* Main background - Castle Sky with gradient */
    .main {
        background: linear-gradient(180deg, #87CEEB 0%, #B0E0E6 30%, #FFB6C1 70%, #FFC0CB 100%);
        position: relative;
        overflow: hidden;
    }

    /* Castle stone texture overlay */
    .main::after {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image:
            radial-gradient(circle at 20% 50%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 50%, rgba(255, 255, 255, 0.1) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
    }

    .main::before, .main::after {
        content: '✨';
        position: fixed;
        font-size: 24px;
        animation: float 4s infinite ease-in-out;
        pointer-events: none;
        z-index: 1;
    }

    .main::before {
        top: 20%;
        left: 10%;
        animation-delay: 0s;
    }

    .main::after {
        top: 60%;
        right: 15%;
        animation-delay: 2s;
    }

    /* Sidebar - Castle Tower */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #6495ED 0%, #4682B4 50%, #4169E1 100%);
        position: relative;
        border-right: 8px solid #C0C0C0;
        box-shadow: inset -10px 0 30px rgba(0, 0, 0, 0.3),
                    4px 0 20px rgba(135, 206, 235, 0.5);
    }

    /* Castle tower top decoration */
    [data-testid="stSidebar"]::after {
        content: '';
        position: absolute;
        top: -20px;
        left: 0;
        right: 0;
        height: 20px;
        background: repeating-linear-gradient(
            90deg,
            #C0C0C0 0px,
            #C0C0C0 30px,
            transparent 30px,
            transparent 40px
        );
        border-top: 3px solid #C0C0C0;
    }

    [data-testid="stSidebar"]::before {
        content: '⭐';
        position: absolute;
        top: 10%;
        right: 10%;
        font-size: 20px;
        animation: sparkle 2s infinite;
    }

    /* Main header - CASTLE with TURRETS */
    .main-header {
        text-align: center;
        font-size: 4em;
        font-weight: 900;
        padding: 60px 40px 40px 40px;
        background: linear-gradient(135deg, #4169E1 0%, #6495ED 30%, #87CEEB 60%, #FFB6C1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        position: relative;
        letter-spacing: 4px;
        text-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        border-bottom: 8px solid #C0C0C0;
        margin-bottom: 30px;
    }

    /* Castle turrets on header */
    .main-header::before,
    .main-header::after {
        content: '🏰';
        position: absolute;
        top: 10px;
        font-size: 0.5em;
        animation: float 6s infinite ease-in-out;
        filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.3));
    }

    .main-header::before {
        left: 5%;
    }

    .main-header::after {
        right: 5%;
        animation-delay: 3s;
    }

    /* Fireworks container */
    .main-header::before {
        content: '🎆';
        position: absolute;
        top: -20px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 2em;
        animation: firework 3s infinite;
        --tx: -100px;
        --ty: -100px;
    }

    .main-header::after {
        content: '🎇';
        position: absolute;
        top: -20px;
        right: 10%;
        font-size: 1.5em;
        animation: firework 3s infinite 1s;
        --tx: 100px;
        --ty: -80px;
    }

    /* Countdown box - CASTLE TOWER */
    .countdown-box {
        background: linear-gradient(135deg, #6495ED 0%, #4682B4 50%, #87CEEB 100%) !important;
        padding: 50px 40px !important;
        border-radius: 15px 15px 0 0 !important;
        width: 500px !important;
        margin: 30px auto !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        color: #ffffff !important;
        text-align: center !important;
        font-size: 2em !important;
        font-weight: 900 !important;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.4),
                    inset 0 -4px 0 rgba(0, 0, 0, 0.2),
                    inset 0 2px 0 rgba(255,255,255,0.3) !important;
        border: 6px solid #C0C0C0 !important;
        border-bottom: 10px solid #A9A9A9 !important;
        position: relative !important;
        overflow: visible !important;
        text-shadow: 0 3px 6px rgba(0, 0, 0, 0.4) !important;
    }

    /* Castle tower battlements */
    .countdown-box::before {
        content: '';
        position: absolute;
        top: -25px;
        left: -6px;
        right: -6px;
        height: 25px;
        background: repeating-linear-gradient(
            90deg,
            #C0C0C0 0px,
            #C0C0C0 40px,
            transparent 40px,
            transparent 50px
        );
        border-top: 6px solid #C0C0C0;
        border-left: 6px solid #C0C0C0;
        border-right: 6px solid #C0C0C0;
    }

    .countdown-box::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(
            45deg,
            transparent 30%,
            rgba(255, 255, 255, 0.4) 50%,
            transparent 70%
        );
        animation: shimmer 3s infinite;
        border-radius: 50%;
    }

    .countdown-box::after {
        content: '🌟';
        position: absolute;
        top: 20px;
        right: 20px;
        font-size: 1.8em;
        animation: sparkle 2s infinite;
    }

    /* Checklist items - CASTLE WALL BANNERS/PLAQUES */
    .checklist-card {
        width: 100% !important;
        min-height: 180px !important;
        padding: 25px 20px 20px 20px !important;
        margin-bottom: 30px !important;
        border-radius: 8px !important;
        background: linear-gradient(135deg, #F0F8FF 0%, #E6F3FF 50%, #FFE4E1 100%) !important;
        border: 4px solid #C0C0C0 !important;
        border-top: 15px solid #B0C4DE !important;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3),
                    inset 0 2px 0 rgba(255, 255, 255, 0.8) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        cursor: pointer !important;
        position: relative !important;
        overflow: visible !important;
    }

    /* Castle banner chain/rope hanging effect */
    .checklist-card::before {
        content: '🔗' !important;
        position: absolute !important;
        top: -20px !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        font-size: 24px !important;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.4)) !important;
        z-index: 10 !important;
    }

    .checklist-card:hover {
        transform: translateY(-5px) !important;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4),
                    inset 0 2px 0 rgba(255, 255, 255, 0.9),
                    0 0 30px rgba(255, 215, 0, 0.6) !important;
        border-color: #FFD700 !important;
        border-top-color: #DAA520 !important;
    }

    .checklist-card.completed {
        opacity: 0.75 !important;
        background: linear-gradient(135deg, #f5f5f5 0%, #e8f4f8 100%) !important;
        filter: grayscale(20%) !important;
    }

    .checklist-card.completed::before {
        content: '✓' !important;
        position: absolute !important;
        top: 50% !important;
        left: 50% !important;
        transform: translate(-50%, -50%) rotate(-15deg) !important;
        font-size: 100px !important;
        color: rgba(39, 174, 96, 0.25) !important;
        font-weight: 900 !important;
        z-index: 1 !important;
        animation: checkPop 0.5s ease-out !important;
        pointer-events: none !important;
    }

    @keyframes checkPop {
        0% { transform: translate(-50%, -50%) rotate(-15deg) scale(0); }
        50% { transform: translate(-50%, -50%) rotate(-15deg) scale(1.3); }
        100% { transform: translate(-50%, -50%) rotate(-15deg) scale(1); }
    }

    .checklist-card-content {
        position: relative !important;
        z-index: 2 !important;
    }

    .checklist-card strong {
        color: #1e88e5 !important;
        font-size: 1.1em !important;
        font-weight: 700 !important;
        display: block !important;
        margin-bottom: 12px !important;
        line-height: 1.4 !important;
    }

    .checklist-card small {
        color: #546e7a !important;
        font-size: 0.85em !important;
        display: block !important;
        margin-top: 8px !important;
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

    /* Idea cards - TREASURE CHEST SCROLLS */
    /* Idea cards - CIRCLE SHAPE with sparkle and shimmy */
    .idea-card {
        padding: 30px !important;
        margin: 20px auto !important;
        border-radius: 15px !important;
        width: 100% !important;
        max-width: 450px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        background: linear-gradient(135deg, #FFF8DC 0%, #FFE4E1 50%, #FFB6C1 100%) !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3) !important;
        border: 5px solid #DAA520 !important;
        color: #2C3E50 !important;
        position: relative !important;
        overflow: visible !important;
        transition: all 0.3s ease !important;
        cursor: pointer !important;
    }

    /* Treasure chest lock */
    .idea-card::before {
        content: '🔐';
        position: absolute;
        top: -15px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 28px;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.4));
    }

    .idea-card:hover {
        transform: translateY(-8px) scale(1.03);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4),
                    0 0 30px rgba(255, 215, 0, 0.6);
        border-color: #FFD700;
    }

    .idea-card::after {
        content: '✨';
        position: absolute;
        top: 30px;
        right: 30px;
        font-size: 2.5em;
        animation: sparkle 2s infinite;
    }

    .idea-card h3 {
        color: #1e88e5 !important;
        font-weight: 700;
        text-align: center;
        margin-bottom: 10px;
    }

    .idea-card p {
        color: #37474f !important;
        text-align: center;
        font-size: 0.95em;
    }

    .idea-card small {
        color: #607d8b !important;
        text-align: center;
        display: block;
        margin-top: 10px;
    }

    /* Buttons - ROYAL CASTLE STYLE */
    .stButton>button {
        background: linear-gradient(135deg, #6495ED 0%, #4169E1 100%);
        color: white;
        border: 4px solid #C0C0C0;
        border-radius: 12px !important;
        padding: 16px 40px;
        min-width: 150px;
        font-weight: 800;
        font-size: 17px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3),
                    inset 0 2px 0 rgba(255, 255, 255, 0.3);
        transition: all 0.3s ease;
        cursor: pointer;
        position: relative;
        overflow: visible;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-family: 'Cinzel', serif !important;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }

    .stButton>button::before {
        content: '✨';
        position: absolute;
        left: 15px;
        animation: sparkle 1.5s infinite;
        font-size: 1.2em;
    }

    .stButton>button::after {
        content: '✨';
        position: absolute;
        right: 15px;
        animation: sparkle 1.5s infinite 0.5s;
        font-size: 1.2em;
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #FFB6C1 0%, #FFC0CB 100%);
        box-shadow: 0 12px 40px rgba(255, 182, 193, 0.7),
                    inset 0 2px 0 rgba(255, 255, 255, 0.5),
                    0 0 30px rgba(255, 182, 193, 0.8);
        border-color: #FFD700;
        transform: translateY(-3px) scale(1.05);
        border-width: 4px;
    }

    .stButton>button:active {
        transform: scale(0.9);
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

    /* Input fields - CASTLE STYLE */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stDateInput > div > div > input {
        color: #2C3E50 !important;
        background: linear-gradient(180deg, #FFFFFF 0%, #F0F8FF 100%) !important;
        border: 3px solid #C0C0C0 !important;
        border-radius: 12px !important;
        padding: 14px 24px !important;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1),
                    0 4px 10px rgba(0, 0, 0, 0.1);
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 16px !important;
    }

    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus,
    .stDateInput > div > div > input:focus {
        border-color: #6495ED !important;
        box-shadow: 0 0 20px rgba(100, 149, 237, 0.6),
                    inset 0 2px 4px rgba(0, 0, 0, 0.1);
        border-width: 3px !important;
    }

    .stSelectbox > div > div > div,
    .stMultiSelect > div > div > div {
        color: #2c3e50 !important;
        background-color: white !important;
        border: 3px solid #b0e0e6 !important;
        border-radius: 50px !important;  /* PILL SHAPE! */
        padding: 8px 20px !important;
    }

    /* Text area - ROUNDED */
    .stTextArea > div > div > textarea {
        border-radius: 30px !important;
        border: 3px solid #b0e0e6 !important;
        padding: 15px 20px !important;
    }

    /* Labels - Royal Castle theme */
    label {
        color: #4169E1 !important;
        font-weight: 700 !important;
        font-family: 'Cinzel', serif !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 14px !important;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }

    /* Tabs styling - CASTLE ARCHWAYS */
    .stTabs [data-baseweb="tab-list"] {
        background: linear-gradient(135deg, #B0C4DE 0%, #87CEEB 100%);
        border-radius: 0 !important;
        padding: 12px 8px;
        border: 4px solid #C0C0C0;
        border-bottom: 6px solid #A9A9A9;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3),
                    inset 0 2px 0 rgba(255, 255, 255, 0.3);
    }

    .stTabs [data-baseweb="tab"] {
        color: #2C3E50 !important;
        font-weight: 800;
        border-radius: 12px 12px 0 0 !important;
        padding: 16px 28px !important;
        margin: 0 5px;
        transition: all 0.3s ease;
        font-family: 'Cinzel', serif !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        background: linear-gradient(180deg, #E6F3FF 0%, #B0C4DE 100%);
        border: 3px solid #C0C0C0;
        border-bottom: none;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }

    .stTabs [data-baseweb="tab"]:hover {
        transform: translateY(-3px);
        background: linear-gradient(180deg, #FFE4E1 0%, #FFB6C1 100%);
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(180deg, #6495ED 0%, #4169E1 100%) !important;
        color: white !important;
        border-radius: 12px 12px 0 0 !important;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4),
                    inset 0 2px 0 rgba(255, 255, 255, 0.3);
        border-color: #FFD700;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
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
    .trip-code-diamond {
        background: linear-gradient(135deg, #6495ED 0%, #4169E1 50%, #FFB6C1 100%);
        padding: 35px 60px;
        border-radius: 15px;
        border: 6px solid #C0C0C0;
        border-top: 20px solid #FFD700;
        text-align: center;
        margin: 30px auto;
        max-width: 700px;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.4),
                    inset 0 2px 0 rgba(255, 255, 255, 0.3);
        position: relative;
    }

    /* Royal banner hanging chain */
    .trip-code-diamond::before {
        content: '⛓️';
        position: absolute;
        top: -30px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 30px;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.5));
    }

    .trip-code-diamond h3 {
        color: white;
        margin: 0;
        font-size: 2em;
        font-weight: 900;
        text-shadow: 0 3px 6px rgba(0, 0, 0, 0.4);
        font-family: 'Cinzel', serif !important;
        letter-spacing: 3px;
    }

    .trip-code-diamond p {
        color: #FFE4E1;
        margin: 15px 0 0 0;
        font-size: 1.1em;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
        font-style: italic;
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
"""
