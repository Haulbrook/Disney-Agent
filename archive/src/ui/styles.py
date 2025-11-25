"""
Disney Trip Planning Agent - Royal Princess Theme
Elegant, magical design fit for a princess family
Built from scratch with sophisticated aesthetics
"""


def apply_custom_styles() -> str:
    """
    Returns elegant princess-themed CSS styling with magical touches.

    Design Philosophy:
    - Royal color palette: Lavenders, rose golds, soft pinks, pearls
    - Elegant typography with Playfair Display
    - Magical effects: Gradients, sparkles, glass morphism
    - Sophisticated yet warm and inviting

    Returns:
        str: Complete CSS within <style> tags
    """
    return """
<style>
    /* ============================================================================
       ROYAL PRINCESS THEME - DISNEY MAGIC
       Elegant, sophisticated design for a princess family
    ============================================================================ */

    /* Import elegant fonts */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700;800;900&family=Cormorant+Garamond:wght@300;400;500;600;700&family=Montserrat:wght@300;400;500;600;700&display=swap');

    /* ============================================================================
       ROOT RESET
    ============================================================================ */

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    /* ============================================================================
       ROYAL COLOR PALETTE - Princess Theme
    ============================================================================ */

    :root {
        /* Royal Princess Colors */
        --royal-purple: #8B5FBF;
        --soft-lavender: #B8A4D9;
        --blush-pink: #FFB6C1;
        --rose-gold: #B76E79;
        --pearl-white: #F8F6F9;
        --champagne: #F7E7CE;
        --dusty-rose: #D4A5A5;
        --deep-purple: #6B46A8;
        --soft-peach: #FFE5D9;
        --lavender-mist: #E6E6FA;

        /* Accent Colors */
        --gold: #D4AF37;
        --rose: #FF69B4;
        --mint: #98D8C8;

        /* Neutrals */
        --white: #FFFFFF;
        --ivory: #FFFFF0;
        --cream: #FFF8F0;
        --light-gray: #F5F5F5;
        --medium-gray: #D3D3D3;
        --soft-gray: #E8E8E8;
        --charcoal: #4A4A4A;
        --deep-charcoal: #2D2D2D;

        /* Gradients */
        --gradient-royal: linear-gradient(135deg, #8B5FBF 0%, #B8A4D9 100%);
        --gradient-sunset: linear-gradient(135deg, #FFB6C1 0%, #B76E79 100%);
        --gradient-pearl: linear-gradient(135deg, #F8F6F9 0%, #E6E6FA 100%);
        --gradient-gold: linear-gradient(135deg, #D4AF37 0%, #F7E7CE 100%);
        --gradient-magic: linear-gradient(135deg, #8B5FBF 0%, #FFB6C1 50%, #D4AF37 100%);

        /* Spacing System (8px base) */
        --space-xs: 0.25rem;   /* 4px */
        --space-sm: 0.5rem;    /* 8px */
        --space-md: 1rem;      /* 16px */
        --space-lg: 1.5rem;    /* 24px */
        --space-xl: 2rem;      /* 32px */
        --space-2xl: 3rem;     /* 48px */
        --space-3xl: 4rem;     /* 64px */

        /* Border Radius */
        --radius-sm: 0.5rem;
        --radius-md: 1rem;
        --radius-lg: 1.5rem;
        --radius-xl: 2rem;
        --radius-full: 9999px;

        /* Shadows - Elegant and soft */
        --shadow-soft: 0 2px 8px rgba(139, 95, 191, 0.08);
        --shadow-md: 0 4px 16px rgba(139, 95, 191, 0.12);
        --shadow-lg: 0 8px 32px rgba(139, 95, 191, 0.16);
        --shadow-xl: 0 16px 48px rgba(139, 95, 191, 0.2);
        --shadow-glow: 0 0 20px rgba(255, 182, 193, 0.3);
        --shadow-gold: 0 4px 16px rgba(212, 175, 55, 0.2);

        /* Transitions */
        --transition-fast: all 200ms cubic-bezier(0.4, 0, 0.2, 1);
        --transition-smooth: all 350ms cubic-bezier(0.4, 0, 0.2, 1);
        --transition-elegant: all 500ms cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* ============================================================================
       BASE STYLES
    ============================================================================ */

    body {
        font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif !important;
        font-size: 16px;
        line-height: 1.7;
        color: var(--charcoal);
        background: var(--gradient-pearl);
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Playfair Display', serif !important;
        font-weight: 700;
        line-height: 1.3;
        color: var(--deep-purple);
        letter-spacing: -0.02em;
    }

    h1 { font-size: 3.5rem; }
    h2 { font-size: 2.5rem; }
    h3 { font-size: 2rem; }
    h4 { font-size: 1.5rem; }
    h5 { font-size: 1.25rem; }
    h6 { font-size: 1rem; }

    p {
        line-height: 1.7;
        color: var(--charcoal);
        font-weight: 400;
    }

    /* ============================================================================
       MAIN LAYOUT
    ============================================================================ */

    .main {
        background: var(--gradient-pearl) !important;
        padding: var(--space-xl) !important;
        min-height: 100vh;
    }

    .main .block-container {
        max-width: 1400px !important;
        padding: var(--space-2xl) var(--space-xl) !important;
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: var(--radius-xl);
        box-shadow: var(--shadow-lg);
    }

    /* ============================================================================
       SIDEBAR - Royal Elegance
    ============================================================================ */

    [data-testid="stSidebar"] {
        background: var(--gradient-royal) !important;
        border-right: none !important;
        box-shadow: var(--shadow-xl) !important;
    }

    [data-testid="stSidebar"] > div {
        padding: var(--space-xl) var(--space-lg) !important;
    }

    [data-testid="stSidebar"] * {
        color: var(--white) !important;
    }

    [data-testid="stSidebar"] h1 {
        font-size: 1.75rem;
        color: var(--white) !important;
        margin-bottom: var(--space-xl);
        padding-bottom: var(--space-lg);
        border-bottom: 2px solid rgba(255, 255, 255, 0.3);
        text-align: center;
    }

    [data-testid="stSidebar"] h2 {
        font-size: 1.25rem;
        color: var(--champagne) !important;
        margin-top: var(--space-xl);
        margin-bottom: var(--space-md);
    }

    [data-testid="stSidebar"] label {
        color: var(--lavender-mist) !important;
        font-weight: 500 !important;
        font-size: 0.9rem !important;
        margin-bottom: var(--space-sm) !important;
    }

    /* Sidebar inputs - Light styling for contrast */
    [data-testid="stSidebar"] input,
    [data-testid="stSidebar"] select,
    [data-testid="stSidebar"] textarea {
        background: rgba(255, 255, 255, 0.95) !important;
        color: var(--deep-purple) !important;
        border: 2px solid rgba(255, 255, 255, 0.5) !important;
        border-radius: var(--radius-md) !important;
    }

    /* ============================================================================
       HEADER - Magical Disney Entrance
    ============================================================================ */

    .main-header {
        background: var(--gradient-magic);
        padding: var(--space-3xl) var(--space-xl);
        border-radius: var(--radius-xl);
        margin-bottom: var(--space-2xl);
        text-align: center;
        box-shadow: var(--shadow-xl), var(--shadow-glow);
        position: relative;
        overflow: hidden;
    }

    .main-header::before {
        content: '✨';
        position: absolute;
        top: 20px;
        left: 30px;
        font-size: 2rem;
        animation: sparkle 3s infinite;
    }

    .main-header::after {
        content: '✨';
        position: absolute;
        bottom: 20px;
        right: 30px;
        font-size: 2rem;
        animation: sparkle 3s infinite 1.5s;
    }

    @keyframes sparkle {
        0%, 100% { opacity: 0.3; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.2); }
    }

    .main-header h1 {
        color: var(--white) !important;
        font-size: 3.5rem;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        display: flex;
        align-items: center;
        justify-content: center;
        gap: var(--space-md);
    }

    .main-header p {
        color: var(--ivory);
        font-size: 1.25rem;
        margin-top: var(--space-md);
        margin-bottom: 0;
    }

    /* ============================================================================
       COUNTDOWN BOX - Royal Timer
    ============================================================================ */

    .countdown-box {
        background: var(--gradient-sunset);
        padding: var(--space-xl);
        border-radius: var(--radius-lg);
        text-align: center;
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--white);
        box-shadow: var(--shadow-lg), var(--shadow-glow);
        margin: var(--space-xl) 0;
        border: 3px solid rgba(255, 255, 255, 0.3);
    }

    /* ============================================================================
       TRIP CODE DIAMOND - Royal Seal
    ============================================================================ */

    .trip-code-diamond {
        background: var(--gradient-gold);
        padding: var(--space-xl) var(--space-2xl);
        margin: var(--space-2xl) 0;
        text-align: center;
        border-radius: var(--radius-lg);
        box-shadow: var(--shadow-gold);
        border: 3px solid var(--gold);
        position: relative;
    }

    .trip-code-diamond h3 {
        color: var(--deep-purple) !important;
        margin: 0 0 var(--space-sm) 0;
        font-size: 1.75rem;
    }

    .trip-code-diamond p {
        color: var(--charcoal);
        margin: 0;
        font-size: 1rem;
    }

    /* ============================================================================
       TABS - Royal Navigation
    ============================================================================ */

    .stTabs {
        background: var(--white);
        border-radius: var(--radius-lg);
        padding: var(--space-lg);
        box-shadow: var(--shadow-md);
        margin-bottom: var(--space-xl);
    }

    [data-baseweb="tab-list"] {
        gap: var(--space-sm);
        background: var(--lavender-mist) !important;
        border-radius: var(--radius-md) !important;
        padding: var(--space-sm) !important;
    }

    [data-baseweb="tab"] {
        background: transparent !important;
        border: none !important;
        border-radius: var(--radius-md) !important;
        padding: var(--space-md) var(--space-xl) !important;
        color: var(--royal-purple) !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: var(--transition-smooth) !important;
        font-family: 'Cormorant Garamond', serif !important;
    }

    [data-baseweb="tab"]:hover {
        background: rgba(255, 255, 255, 0.7) !important;
        color: var(--deep-purple) !important;
        transform: translateY(-2px);
    }

    [data-baseweb="tab"][aria-selected="true"] {
        background: var(--gradient-royal) !important;
        color: var(--white) !important;
        box-shadow: var(--shadow-md) !important;
        font-weight: 700 !important;
    }

    [data-baseweb="tab-highlight"] {
        display: none !important;
    }

    /* ============================================================================
       CARDS - Elegant Design
    ============================================================================ */

    .card {
        background: var(--white);
        border: 2px solid var(--lavender-mist);
        border-radius: var(--radius-lg);
        padding: var(--space-xl);
        margin-bottom: var(--space-lg);
        transition: var(--transition-smooth);
        box-shadow: var(--shadow-soft);
    }

    .card:hover {
        border-color: var(--royal-purple);
        box-shadow: var(--shadow-lg);
        transform: translateY(-4px);
    }

    /* Checklist Card - Royal Task Cards */
    .checklist-card {
        background: linear-gradient(135deg, var(--white) 0%, var(--pearl-white) 100%);
        border: 2px solid var(--lavender-mist);
        border-left: 6px solid var(--soft-lavender);
        border-radius: var(--radius-lg);
        padding: var(--space-lg);
        margin-bottom: var(--space-md);
        transition: var(--transition-smooth);
        position: relative;
        overflow: hidden;
        box-shadow: var(--shadow-soft);
    }

    .checklist-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: var(--gradient-magic);
        opacity: 0;
        transition: var(--transition-smooth);
    }

    .checklist-card:hover {
        border-left-color: var(--royal-purple);
        box-shadow: var(--shadow-md);
        transform: translateX(4px);
    }

    .checklist-card:hover::before {
        opacity: 1;
    }

    .checklist-card.completed {
        background: var(--lavender-mist);
        opacity: 0.7;
        border-left-color: var(--gold);
    }

    .checklist-card.priority-high {
        border-left-color: var(--rose);
    }

    .checklist-card.priority-medium {
        border-left-color: var(--gold);
    }

    .checklist-card.priority-low {
        border-left-color: var(--mint);
    }

    .checklist-card strong {
        color: var(--deep-purple);
        font-size: 1.125rem;
        font-weight: 600;
        display: block;
        margin-bottom: var(--space-sm);
        font-family: 'Cormorant Garamond', serif;
    }

    .checklist-card small {
        color: var(--charcoal);
        font-size: 0.875rem;
        opacity: 0.8;
    }

    .checklist-card-content {
        padding-right: var(--space-md);
    }

    /* Card action row for checkboxes and buttons */
    .card-action-row {
        display: flex;
        align-items: center;
        gap: var(--space-md);
        margin-top: var(--space-md);
        width: 100%;
    }

    /* ============================================================================
       IDEA CARDS - Magical Suggestions
    ============================================================================ */

    .idea-card {
        background: linear-gradient(135deg, var(--soft-peach) 0%, var(--pearl-white) 100%);
        border: 2px solid var(--dusty-rose);
        border-radius: var(--radius-lg);
        padding: var(--space-xl);
        margin-bottom: var(--space-lg);
        box-shadow: var(--shadow-soft);
        transition: var(--transition-smooth);
    }

    .idea-card:hover {
        border-color: var(--rose-gold);
        box-shadow: var(--shadow-md), var(--shadow-glow);
        transform: translateY(-4px);
    }

    .idea-card h3 {
        color: var(--deep-purple) !important;
        margin-bottom: var(--space-md);
        font-size: 1.5rem;
    }

    .idea-card p {
        color: var(--charcoal);
        margin-bottom: var(--space-md);
        line-height: 1.7;
    }

    .idea-card small {
        color: var(--charcoal);
        opacity: 0.7;
        font-size: 0.875rem;
    }

    /* ============================================================================
       BUTTONS - Royal Actions
    ============================================================================ */

    .stButton {
        margin: 0 !important;
    }

    .stButton > button {
        background: var(--gradient-royal) !important;
        color: var(--white) !important;
        border: none !important;
        border-radius: var(--radius-lg) !important;
        padding: var(--space-md) var(--space-xl) !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        font-family: 'Montserrat', sans-serif !important;
        transition: var(--transition-smooth) !important;
        box-shadow: var(--shadow-md) !important;
        cursor: pointer !important;
        width: 100% !important;
        text-align: center !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .stButton > button:hover {
        box-shadow: var(--shadow-lg), var(--shadow-glow) !important;
        transform: translateY(-2px) scale(1.02);
    }

    .stButton > button:active {
        transform: translateY(0) scale(0.98);
    }

    /* Delete button - Elegant red */
    .card-delete-btn {
        flex-shrink: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
        width: 40px !important;
        max-width: 40px !important;
        overflow: hidden !important;
    }

    .card-delete-btn .stButton {
        margin: 0 !important;
        padding: 0 !important;
        width: 40px !important;
        max-width: 40px !important;
    }

    .card-delete-btn button {
        background: var(--gradient-sunset) !important;
        width: 40px !important;
        height: 40px !important;
        min-width: 40px !important;
        min-height: 40px !important;
        max-width: 40px !important;
        max-height: 40px !important;
        padding: 0 !important;
        margin: 0 !important;
        border-radius: var(--radius-full) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 1.125rem !important;
        box-shadow: var(--shadow-soft) !important;
    }

    .card-delete-btn button:hover {
        background: linear-gradient(135deg, #FF1493 0%, #C71585 100%) !important;
        transform: scale(1.1) rotate(5deg);
        box-shadow: var(--shadow-md) !important;
    }

    /* ============================================================================
       INPUTS - Elegant Form Fields
    ============================================================================ */

    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div,
    .stMultiSelect > div > div,
    .stNumberInput > div > div > input,
    .stDateInput > div > div > input {
        background: var(--white) !important;
        border: 2px solid var(--lavender-mist) !important;
        border-radius: var(--radius-md) !important;
        padding: var(--space-md) var(--space-lg) !important;
        font-size: 1rem !important;
        color: var(--deep-purple) !important;
        transition: var(--transition-smooth) !important;
        font-family: 'Montserrat', sans-serif !important;
    }

    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div:focus-within,
    .stNumberInput > div > div > input:focus,
    .stDateInput > div > div > input:focus {
        border-color: var(--royal-purple) !important;
        box-shadow: 0 0 0 4px rgba(139, 95, 191, 0.1) !important;
        outline: none !important;
    }

    /* ============================================================================
       CHECKBOXES - Royal Checks
    ============================================================================ */

    .stCheckbox {
        padding: var(--space-sm) 0;
    }

    .stCheckbox > label {
        color: var(--deep-purple) !important;
        font-weight: 500 !important;
        cursor: pointer !important;
        display: flex !important;
        align-items: center !important;
        gap: var(--space-md) !important;
        font-size: 1rem !important;
    }

    .stCheckbox input[type="checkbox"] {
        width: 24px !important;
        height: 24px !important;
        border-radius: var(--radius-sm) !important;
        border: 2px solid var(--soft-lavender) !important;
        background: var(--white) !important;
        cursor: pointer !important;
        flex-shrink: 0 !important;
    }

    .stCheckbox input[type="checkbox"]:checked {
        background: var(--gradient-royal) !important;
        border-color: var(--royal-purple) !important;
    }

    /* ============================================================================
       ALERTS - Royal Notifications
    ============================================================================ */

    .stAlert {
        background: var(--white) !important;
        border: 2px solid var(--lavender-mist) !important;
        border-left: 6px solid var(--royal-purple) !important;
        border-radius: var(--radius-md) !important;
        padding: var(--space-lg) !important;
        margin: var(--space-lg) 0 !important;
        box-shadow: var(--shadow-soft);
    }

    .stSuccess {
        border-left-color: var(--mint) !important;
        background: linear-gradient(135deg, var(--white) 0%, #F0FFF4 100%) !important;
    }

    .stWarning {
        border-left-color: var(--gold) !important;
        background: linear-gradient(135deg, var(--white) 0%, var(--champagne) 100%) !important;
    }

    .stError {
        border-left-color: var(--rose) !important;
        background: linear-gradient(135deg, var(--white) 0%, #FFF0F5 100%) !important;
    }

    .stInfo {
        border-left-color: var(--royal-purple) !important;
        background: linear-gradient(135deg, var(--white) 0%, var(--lavender-mist) 100%) !important;
    }

    /* ============================================================================
       CHAT INTERFACE - Royal Conversation
    ============================================================================ */

    .stChatMessage {
        background: var(--white) !important;
        border: 2px solid var(--lavender-mist) !important;
        border-radius: var(--radius-lg) !important;
        padding: var(--space-lg) !important;
        margin-bottom: var(--space-md) !important;
        box-shadow: var(--shadow-soft);
    }

    .stChatMessage[data-testid="chat-message-user"] {
        background: linear-gradient(135deg, var(--soft-peach) 0%, var(--pearl-white) 100%) !important;
        border-color: var(--dusty-rose) !important;
    }

    .stChatMessage[data-testid="chat-message-assistant"] {
        background: linear-gradient(135deg, var(--lavender-mist) 0%, var(--pearl-white) 100%) !important;
        border-color: var(--soft-lavender) !important;
    }

    /* ============================================================================
       METRICS - Royal Dashboard
    ============================================================================ */

    [data-testid="stMetric"] {
        background: var(--gradient-pearl);
        border: 2px solid var(--lavender-mist);
        border-radius: var(--radius-lg);
        padding: var(--space-xl);
        box-shadow: var(--shadow-soft);
    }

    [data-testid="stMetricLabel"] {
        color: var(--royal-purple);
        font-size: 0.875rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-family: 'Montserrat', sans-serif;
    }

    [data-testid="stMetricValue"] {
        color: var(--deep-purple);
        font-size: 2.5rem;
        font-weight: 700;
        margin-top: var(--space-sm);
        font-family: 'Playfair Display', serif;
    }

    /* ============================================================================
       PROGRESS BAR - Royal Progress
    ============================================================================ */

    .stProgress > div > div {
        background: var(--lavender-mist) !important;
        border-radius: var(--radius-full) !important;
        height: 12px !important;
    }

    .stProgress > div > div > div {
        background: var(--gradient-magic) !important;
        border-radius: var(--radius-full) !important;
        box-shadow: var(--shadow-glow);
    }

    /* ============================================================================
       EXPANDER - Elegant Accordion
    ============================================================================ */

    .streamlit-expanderHeader {
        background: var(--gradient-pearl) !important;
        border: 2px solid var(--lavender-mist) !important;
        border-radius: var(--radius-md) !important;
        padding: var(--space-lg) !important;
        font-weight: 600 !important;
        color: var(--deep-purple) !important;
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 1.125rem !important;
    }

    .streamlit-expanderHeader:hover {
        background: var(--white) !important;
        border-color: var(--royal-purple) !important;
        box-shadow: var(--shadow-soft);
    }

    .streamlit-expanderContent {
        border: 2px solid var(--lavender-mist) !important;
        border-top: none !important;
        border-radius: 0 0 var(--radius-md) var(--radius-md) !important;
        padding: var(--space-lg) !important;
        background: var(--white);
    }

    /* ============================================================================
       SCROLLBAR - Royal Scrolling
    ============================================================================ */

    ::-webkit-scrollbar {
        width: 14px;
        height: 14px;
    }

    ::-webkit-scrollbar-track {
        background: var(--lavender-mist);
        border-radius: var(--radius-md);
    }

    ::-webkit-scrollbar-thumb {
        background: var(--gradient-royal);
        border-radius: var(--radius-md);
        border: 3px solid var(--lavender-mist);
    }

    ::-webkit-scrollbar-thumb:hover {
        background: var(--deep-purple);
    }

    /* ============================================================================
       RESPONSIVE DESIGN
    ============================================================================ */

    @media (max-width: 768px) {
        .main .block-container {
            padding: var(--space-lg) var(--space-md) !important;
        }

        .main-header h1 {
            font-size: 2rem;
        }

        .main-header {
            padding: var(--space-xl) var(--space-lg);
        }

        h1 { font-size: 2rem; }
        h2 { font-size: 1.75rem; }
        h3 { font-size: 1.5rem; }

        [data-baseweb="tab"] {
            padding: var(--space-sm) var(--space-md) !important;
            font-size: 0.875rem !important;
        }
    }

    /* ============================================================================
       STREAMLIT FIXES
    ============================================================================ */

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    .stApp [data-testid="stToolbar"] {
        display: none;
    }

    /* Column fixes to prevent overlap */
    [data-testid="column"] {
        padding: 0 var(--space-sm) !important;
        overflow: hidden !important;
    }

    [data-testid="column"]:first-child {
        padding-left: 0 !important;
    }

    [data-testid="column"]:last-child {
        padding-right: 0 !important;
    }

    /* Spinner */
    .stSpinner > div {
        border-color: var(--royal-purple) transparent var(--royal-purple) transparent !important;
    }

    /* ============================================================================
       MAGICAL ANIMATIONS
    ============================================================================ */

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes shimmer {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
    }

    .card, .checklist-card, .idea-card {
        animation: fadeIn 0.5s ease-out;
    }

    /* Magical sparkle effect */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }

</style>
"""
