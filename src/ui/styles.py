"""
Disney Trip Planning Agent - Premium Modern Styles Module

A sleek, professional Disney-inspired design system featuring:
- Modern glassmorphism and depth
- Sophisticated color palette with Disney magic
- Smooth micro-interactions and transitions
- Premium typography and spacing
- Elegant animations and effects
"""


def apply_custom_styles() -> str:
    """
    Returns premium, modern CSS styling with sophisticated Disney aesthetics.

    Features:
    - Glassmorphism and frosted effects
    - Deep navy blues, elegant golds, and magical teals
    - Smooth animations and micro-interactions
    - Professional typography with Poppins and Inter
    - Clean, spacious layout with perfect hierarchy
    - Subtle Disney magic without overwhelming design

    Returns:
        str: Complete CSS within <style> tags for st.markdown()
    """
    return """
<style>
    /* ============================================================================
       MODERN DISNEY PREMIUM THEME
       Sleek, Professional, with Magical Touches
    ============================================================================ */

    /* Import Modern Professional Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

    /* ============================================================================
       ROOT VARIABLES - Premium Disney Palette
    ============================================================================ */
    :root {
        /* Primary Colors - Deep & Sophisticated */
        --disney-navy: #0A2540;
        --disney-royal-blue: #1E3A8A;
        --disney-sky: #3B82F6;
        --disney-teal: #14B8A6;
        --disney-gold: #F59E0B;
        --disney-rose: #F472B6;

        /* Neutral Colors - Clean & Modern */
        --white: #FFFFFF;
        --off-white: #F8FAFC;
        --light-gray: #E2E8F0;
        --mid-gray: #94A3B8;
        --dark-gray: #334155;
        --black: #0F172A;

        /* Glass Effects */
        --glass-bg: rgba(255, 255, 255, 0.1);
        --glass-border: rgba(255, 255, 255, 0.2);

        /* Shadows - Depth & Elevation */
        --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
        --shadow-2xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);

        /* Magic Glow */
        --glow-blue: 0 0 20px rgba(59, 130, 246, 0.3);
        --glow-gold: 0 0 20px rgba(245, 158, 11, 0.3);
        --glow-teal: 0 0 20px rgba(20, 184, 166, 0.3);

        /* Spacing System */
        --space-xs: 0.25rem;
        --space-sm: 0.5rem;
        --space-md: 1rem;
        --space-lg: 1.5rem;
        --space-xl: 2rem;
        --space-2xl: 3rem;

        /* Border Radius */
        --radius-sm: 0.375rem;
        --radius-md: 0.5rem;
        --radius-lg: 0.75rem;
        --radius-xl: 1rem;
        --radius-2xl: 1.5rem;
        --radius-full: 9999px;

        /* Transitions */
        --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
        --transition-base: 250ms cubic-bezier(0.4, 0, 0.2, 1);
        --transition-slow: 350ms cubic-bezier(0.4, 0, 0.2, 1);
        --transition-bounce: 500ms cubic-bezier(0.68, -0.55, 0.265, 1.55);
    }

    /* ============================================================================
       MODERN ANIMATIONS
    ============================================================================ */

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeInScale {
        from {
            opacity: 0;
            transform: scale(0.95);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }

    @keyframes magicSparkle {
        0%, 100% {
            opacity: 0;
            transform: scale(0) rotate(0deg);
        }
        50% {
            opacity: 1;
            transform: scale(1) rotate(180deg);
        }
    }

    @keyframes gentleFloat {
        0%, 100% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-8px);
        }
    }

    @keyframes shimmerGlow {
        0% {
            background-position: -200% center;
        }
        100% {
            background-position: 200% center;
        }
    }

    @keyframes pulseGlow {
        0%, 100% {
            box-shadow: var(--shadow-md);
        }
        50% {
            box-shadow: var(--shadow-xl), var(--glow-blue);
        }
    }

    @keyframes gradientShift {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }

    /* ============================================================================
       BASE STYLES - Typography & Layout
    ============================================================================ */

    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
        letter-spacing: -0.01em;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Poppins', sans-serif !important;
        font-weight: 600;
        letter-spacing: -0.02em;
        line-height: 1.2;
    }

    h1 {
        font-size: 2.5rem;
        font-weight: 700;
    }

    h2 {
        font-size: 2rem;
        font-weight: 600;
    }

    h3 {
        font-size: 1.5rem;
    }

    /* ============================================================================
       MAIN BACKGROUND - Elegant Gradient
    ============================================================================ */

    .main {
        background: linear-gradient(
            135deg,
            #0A2540 0%,
            #1E3A8A 25%,
            #3B82F6 50%,
            #14B8A6 75%,
            #0EA5E9 100%
        );
        background-size: 400% 400%;
        animation: gradientShift 20s ease infinite;
        min-height: 100vh;
        position: relative;
    }

    /* Subtle magical overlay */
    .main::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background:
            radial-gradient(circle at 20% 30%, rgba(59, 130, 246, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 70%, rgba(20, 184, 166, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 50% 50%, rgba(245, 158, 11, 0.05) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
    }

    /* Floating sparkles */
    .main::after {
        content: '✨';
        position: fixed;
        top: 10%;
        right: 15%;
        font-size: 2rem;
        opacity: 0.6;
        animation: gentleFloat 6s ease-in-out infinite, magicSparkle 3s ease-in-out infinite;
        pointer-events: none;
        z-index: 1;
    }

    /* ============================================================================
       SIDEBAR - Modern Glass Panel
    ============================================================================ */

    [data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            rgba(10, 37, 64, 0.95) 0%,
            rgba(30, 58, 138, 0.95) 100%
        ) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-right: 1px solid var(--glass-border) !important;
        box-shadow: var(--shadow-2xl) !important;
    }

    [data-testid="stSidebar"] > div {
        padding: var(--space-lg) !important;
    }

    /* Sidebar title styling */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: var(--white) !important;
        margin-bottom: var(--space-lg) !important;
        background: linear-gradient(135deg, #FFFFFF 0%, #3B82F6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    /* Sidebar inputs and widgets */
    [data-testid="stSidebar"] label {
        color: var(--light-gray) !important;
        font-weight: 500 !important;
        font-size: 0.875rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: var(--space-sm) !important;
    }

    /* ============================================================================
       MAIN HEADER - Hero Title
    ============================================================================ */

    .main-header {
        text-align: center;
        font-size: 3.5rem;
        font-weight: 800;
        padding: var(--space-2xl) var(--space-xl);
        background: linear-gradient(
            135deg,
            #FFFFFF 0%,
            #3B82F6 30%,
            #14B8A6 60%,
            #F59E0B 100%
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        background-size: 200% auto;
        animation: shimmerGlow 4s linear infinite;
        position: relative;
        margin-bottom: var(--space-2xl);
        letter-spacing: -0.03em;
    }

    .main-header::before {
        content: '🏰';
        position: absolute;
        left: 5%;
        top: 50%;
        transform: translateY(-50%);
        font-size: 2.5rem;
        animation: gentleFloat 4s ease-in-out infinite;
        filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.2));
    }

    .main-header::after {
        content: '✨';
        position: absolute;
        right: 5%;
        top: 50%;
        transform: translateY(-50%);
        font-size: 2rem;
        animation: gentleFloat 4s ease-in-out infinite 2s, magicSparkle 3s ease-in-out infinite;
    }

    /* ============================================================================
       COUNTDOWN BOX - Premium Card
    ============================================================================ */

    .countdown-box {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(20, 184, 166, 0.1) 100%) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid var(--glass-border) !important;
        border-radius: var(--radius-2xl) !important;
        padding: var(--space-2xl) !important;
        margin: var(--space-xl) auto !important;
        max-width: 600px !important;
        box-shadow: var(--shadow-xl), var(--glow-blue) !important;
        transition: all var(--transition-slow) !important;
        animation: fadeInScale 0.6s ease-out !important;
    }

    .countdown-box:hover {
        transform: translateY(-4px) scale(1.02) !important;
        box-shadow: var(--shadow-2xl), var(--glow-teal) !important;
    }

    .countdown-box h2 {
        color: var(--white) !important;
        font-size: 3rem !important;
        font-weight: 800 !important;
        margin-bottom: var(--space-sm) !important;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3) !important;
    }

    .countdown-box p {
        color: var(--light-gray) !important;
        font-size: 1.125rem !important;
        font-weight: 500 !important;
    }

    /* ============================================================================
       TABS - Clean & Modern
    ============================================================================ */

    .stTabs {
        margin-top: var(--space-xl);
    }

    [data-baseweb="tab-list"] {
        gap: var(--space-md);
        background: var(--glass-bg) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: var(--radius-xl) !important;
        padding: var(--space-sm) !important;
        border: 1px solid var(--glass-border) !important;
    }

    [data-baseweb="tab"] {
        background: transparent !important;
        border: none !important;
        border-radius: var(--radius-lg) !important;
        padding: var(--space-md) var(--space-xl) !important;
        color: var(--light-gray) !important;
        font-weight: 500 !important;
        font-size: 0.875rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        transition: all var(--transition-base) !important;
    }

    [data-baseweb="tab"]:hover {
        background: var(--glass-bg) !important;
        color: var(--white) !important;
    }

    [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, var(--disney-sky) 0%, var(--disney-teal) 100%) !important;
        color: var(--white) !important;
        box-shadow: var(--shadow-lg), var(--glow-blue) !important;
    }

    /* ============================================================================
       CHECKLIST CARDS - Premium Glass Cards
    ============================================================================ */

    .checklist-card {
        background: var(--glass-bg) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid var(--glass-border) !important;
        border-radius: var(--radius-xl) !important;
        padding: var(--space-lg) !important;
        margin-bottom: var(--space-lg) !important;
        box-shadow: var(--shadow-lg) !important;
        transition: all var(--transition-slow) !important;
        cursor: pointer !important;
        position: relative !important;
        overflow: hidden !important;
        animation: fadeInUp 0.4s ease-out !important;
    }

    .checklist-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--disney-sky) 0%, var(--disney-teal) 50%, var(--disney-gold) 100%);
        opacity: 0;
        transition: opacity var(--transition-base);
    }

    .checklist-card:hover {
        transform: translateY(-4px) !important;
        box-shadow: var(--shadow-xl), var(--glow-blue) !important;
        border-color: var(--disney-sky) !important;
    }

    .checklist-card:hover::before {
        opacity: 1;
    }

    /* Priority indicators */
    .checklist-card[data-priority="high"]::after {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 4px;
        background: linear-gradient(180deg, #EF4444 0%, #DC2626 100%);
        box-shadow: 0 0 10px rgba(239, 68, 68, 0.5);
    }

    .checklist-card[data-priority="medium"]::after {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 4px;
        background: linear-gradient(180deg, #F59E0B 0%, #D97706 100%);
        box-shadow: 0 0 10px rgba(245, 158, 11, 0.5);
    }

    .checklist-card[data-priority="low"]::after {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 4px;
        background: linear-gradient(180deg, #10B981 0%, #059669 100%);
        box-shadow: 0 0 10px rgba(16, 185, 129, 0.5);
    }

    .checklist-card strong {
        color: var(--white) !important;
        font-size: 1.125rem !important;
        font-weight: 600 !important;
        display: block !important;
        margin-bottom: var(--space-sm) !important;
        line-height: 1.4 !important;
    }

    .checklist-card small {
        color: var(--mid-gray) !important;
        font-size: 0.875rem !important;
        display: block !important;
        margin-top: var(--space-sm) !important;
    }

    /* Completed state */
    .checklist-card.completed {
        opacity: 0.6 !important;
        background: rgba(30, 58, 138, 0.3) !important;
    }

    .checklist-card.completed strong {
        text-decoration: line-through;
        opacity: 0.7;
    }

    /* ============================================================================
       BADGES & PILLS
    ============================================================================ */

    .category-badge {
        display: inline-block;
        padding: var(--space-xs) var(--space-md);
        background: var(--glass-bg);
        backdrop-filter: blur(10px);
        border: 1px solid var(--glass-border);
        border-radius: var(--radius-full);
        color: var(--light-gray);
        font-size: 0.75rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-right: var(--space-sm);
    }

    .priority-badge {
        display: inline-block;
        padding: var(--space-xs) var(--space-md);
        border-radius: var(--radius-full);
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .priority-badge.priority-high {
        background: linear-gradient(135deg, #EF4444 0%, #DC2626 100%);
        color: var(--white);
        box-shadow: 0 2px 10px rgba(239, 68, 68, 0.3);
    }

    .priority-badge.priority-medium {
        background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
        color: var(--white);
        box-shadow: 0 2px 10px rgba(245, 158, 11, 0.3);
    }

    .priority-badge.priority-low {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%);
        color: var(--white);
        box-shadow: 0 2px 10px rgba(16, 185, 129, 0.3);
    }

    /* ============================================================================
       BUTTONS - Modern & Sleek
    ============================================================================ */

    .stButton > button {
        background: linear-gradient(135deg, var(--disney-sky) 0%, var(--disney-teal) 100%) !important;
        color: var(--white) !important;
        border: none !important;
        border-radius: var(--radius-lg) !important;
        padding: var(--space-md) var(--space-xl) !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        box-shadow: var(--shadow-lg), var(--glow-blue) !important;
        transition: all var(--transition-base) !important;
        cursor: pointer !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: var(--shadow-xl), var(--glow-teal) !important;
    }

    .stButton > button:active {
        transform: translateY(0) !important;
    }

    /* Delete button */
    .card-delete-btn button {
        background: linear-gradient(135deg, #EF4444 0%, #DC2626 100%) !important;
        width: 40px !important;
        height: 40px !important;
        min-width: 40px !important;
        padding: 0 !important;
        border-radius: var(--radius-full) !important;
        box-shadow: var(--shadow-md) !important;
    }

    .card-delete-btn button:hover {
        transform: scale(1.1) rotate(10deg) !important;
        box-shadow: var(--shadow-lg), 0 0 20px rgba(239, 68, 68, 0.5) !important;
    }

    /* ============================================================================
       INPUT FIELDS - Clean & Modern
    ============================================================================ */

    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select,
    .stMultiSelect > div > div {
        background: var(--glass-bg) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid var(--glass-border) !important;
        border-radius: var(--radius-md) !important;
        color: var(--white) !important;
        padding: var(--space-md) !important;
        font-size: 0.875rem !important;
        transition: all var(--transition-base) !important;
    }

    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus {
        border-color: var(--disney-sky) !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2) !important;
        outline: none !important;
    }

    /* ============================================================================
       CHECKBOXES - Modern Toggle Style
    ============================================================================ */

    .stCheckbox {
        padding: var(--space-sm) 0;
    }

    .stCheckbox > label {
        color: var(--light-gray) !important;
        font-weight: 500 !important;
        cursor: pointer !important;
        transition: color var(--transition-base) !important;
    }

    .stCheckbox > label:hover {
        color: var(--white) !important;
    }

    .stCheckbox input[type="checkbox"] {
        width: 20px;
        height: 20px;
        border-radius: var(--radius-sm);
        border: 2px solid var(--glass-border);
        background: var(--glass-bg);
        cursor: pointer;
        transition: all var(--transition-base);
    }

    .stCheckbox input[type="checkbox"]:checked {
        background: linear-gradient(135deg, var(--disney-sky) 0%, var(--disney-teal) 100%);
        border-color: var(--disney-sky);
        box-shadow: var(--glow-blue);
    }

    /* ============================================================================
       CHAT INTERFACE - Sleek Messages
    ============================================================================ */

    .stChatMessage {
        background: var(--glass-bg) !important;
        backdrop-filter: blur(20px) !important;
        border: 1px solid var(--glass-border) !important;
        border-radius: var(--radius-xl) !important;
        padding: var(--space-lg) !important;
        margin-bottom: var(--space-md) !important;
        animation: fadeInUp 0.3s ease-out !important;
    }

    .stChatMessage[data-testid="chat-message-user"] {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.2) 0%, rgba(20, 184, 166, 0.2) 100%) !important;
        border-color: var(--disney-sky) !important;
    }

    .stChatMessage[data-testid="chat-message-assistant"] {
        background: var(--glass-bg) !important;
    }

    /* ============================================================================
       ALERTS & NOTIFICATIONS
    ============================================================================ */

    .stAlert {
        background: var(--glass-bg) !important;
        backdrop-filter: blur(20px) !important;
        border: 1px solid var(--glass-border) !important;
        border-radius: var(--radius-lg) !important;
        padding: var(--space-lg) !important;
        margin: var(--space-md) 0 !important;
        animation: fadeInScale 0.3s ease-out !important;
    }

    .stSuccess {
        border-left: 4px solid #10B981 !important;
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.2) !important;
    }

    .stWarning {
        border-left: 4px solid #F59E0B !important;
        box-shadow: 0 0 20px rgba(245, 158, 11, 0.2) !important;
    }

    .stError {
        border-left: 4px solid #EF4444 !important;
        box-shadow: 0 0 20px rgba(239, 68, 68, 0.2) !important;
    }

    .stInfo {
        border-left: 4px solid #3B82F6 !important;
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.2) !important;
    }

    /* ============================================================================
       PROGRESS INDICATORS
    ============================================================================ */

    .stProgress > div > div {
        background: var(--glass-bg) !important;
        border-radius: var(--radius-full) !important;
    }

    .stProgress > div > div > div {
        background: linear-gradient(90deg, var(--disney-sky) 0%, var(--disney-teal) 50%, var(--disney-gold) 100%) !important;
        border-radius: var(--radius-full) !important;
        box-shadow: var(--glow-blue) !important;
    }

    /* ============================================================================
       EXPANDERS - Clean Accordions
    ============================================================================ */

    .streamlit-expanderHeader {
        background: var(--glass-bg) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid var(--glass-border) !important;
        border-radius: var(--radius-lg) !important;
        padding: var(--space-md) !important;
        color: var(--white) !important;
        font-weight: 600 !important;
        transition: all var(--transition-base) !important;
    }

    .streamlit-expanderHeader:hover {
        background: rgba(59, 130, 246, 0.2) !important;
        border-color: var(--disney-sky) !important;
    }

    /* ============================================================================
       METRICS - Dashboard Cards
    ============================================================================ */

    [data-testid="stMetric"] {
        background: var(--glass-bg) !important;
        backdrop-filter: blur(20px) !important;
        border: 1px solid var(--glass-border) !important;
        border-radius: var(--radius-xl) !important;
        padding: var(--space-lg) !important;
        box-shadow: var(--shadow-lg) !important;
        transition: all var(--transition-base) !important;
    }

    [data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-xl), var(--glow-blue);
    }

    [data-testid="stMetricLabel"] {
        color: var(--mid-gray) !important;
        font-size: 0.875rem !important;
        font-weight: 500 !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    [data-testid="stMetricValue"] {
        color: var(--white) !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
    }

    /* ============================================================================
       RESPONSIVE DESIGN - Mobile Optimization
    ============================================================================ */

    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem;
            padding: var(--space-xl) var(--space-md);
        }

        .countdown-box {
            padding: var(--space-lg) !important;
            margin: var(--space-md) !important;
        }

        .countdown-box h2 {
            font-size: 2rem !important;
        }

        .checklist-card {
            padding: var(--space-md) !important;
        }

        [data-baseweb="tab"] {
            padding: var(--space-sm) var(--space-md) !important;
            font-size: 0.75rem !important;
        }
    }

    @media (max-width: 480px) {
        .main-header {
            font-size: 1.5rem;
        }

        h1 {
            font-size: 1.75rem;
        }

        h2 {
            font-size: 1.5rem;
        }

        h3 {
            font-size: 1.25rem;
        }
    }

    /* ============================================================================
       SCROLLBAR - Modern Styling
    ============================================================================ */

    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }

    ::-webkit-scrollbar-track {
        background: var(--glass-bg);
        border-radius: var(--radius-md);
    }

    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, var(--disney-sky) 0%, var(--disney-teal) 100%);
        border-radius: var(--radius-md);
        box-shadow: var(--glow-blue);
    }

    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, var(--disney-teal) 0%, var(--disney-gold) 100%);
    }

    /* ============================================================================
       LOADING STATES - Skeleton Screens
    ============================================================================ */

    .skeleton {
        background: linear-gradient(
            90deg,
            var(--glass-bg) 25%,
            rgba(255, 255, 255, 0.2) 50%,
            var(--glass-bg) 75%
        );
        background-size: 200% 100%;
        animation: shimmerGlow 1.5s infinite;
        border-radius: var(--radius-md);
    }

    /* ============================================================================
       UTILITY CLASSES
    ============================================================================ */

    .text-gradient {
        background: linear-gradient(135deg, #FFFFFF 0%, #3B82F6 50%, #14B8A6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .glass-panel {
        background: var(--glass-bg);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid var(--glass-border);
        border-radius: var(--radius-xl);
        padding: var(--space-lg);
        box-shadow: var(--shadow-lg);
    }

    .magic-hover {
        transition: all var(--transition-base);
    }

    .magic-hover:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-xl), var(--glow-blue);
    }

</style>
"""
