"""
Disney Trip Planning Agent - Magical Disney Castle Theme
A stunning, immersive Disney experience with castles, Mickey heads,
sparkles, and pure Disney magic!

🏰 FLEX THE MUSCLES EDITION 🏰
"""


def apply_custom_styles() -> str:
    """
    Returns a spectacular Disney-themed CSS with:
    - Castle silhouettes
    - Mickey Mouse head icons
    - Magical sparkle animations
    - Disney color palette (royal blues, golds, purples)
    - Fireworks and stars
    - Smooth magical transitions
    - ALL FUNCTIONALITY PRESERVED

    Returns:
        str: Complete magical CSS within <style> tags
    """
    return """
<style>
    /* ============================================================================
       🏰 DISNEY MAGICAL KINGDOM THEME 🏰
       A spectacular, immersive Disney experience
    ============================================================================ */

    /* Import Disney-inspired fonts */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700;800;900&family=Quicksand:wght@300;400;500;600;700&family=Satisfy&display=swap');

    /* ============================================================================
       ROOT RESET - Clean magical slate
    ============================================================================ */

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    /* ============================================================================
       🎨 DISNEY DESIGN TOKENS - Royal Magic Palette
    ============================================================================ */

    :root {
        /* Disney Castle Blues */
        --disney-royal-blue: #1a237e;
        --disney-midnight: #0d1b3e;
        --disney-sky: #5c6bc0;
        --disney-light-blue: #7986cb;
        --disney-ice: #e8eaf6;

        /* Disney Golds & Sparkles */
        --disney-gold: #ffd700;
        --disney-light-gold: #ffecb3;
        --disney-bronze: #cd853f;
        --disney-sparkle: #fff8dc;

        /* Disney Princess Purples & Pinks */
        --disney-purple: #7b1fa2;
        --disney-light-purple: #ce93d8;
        --disney-pink: #f48fb1;
        --disney-rose: #fce4ec;

        /* Disney Magic Accents */
        --disney-teal: #00bcd4;
        --disney-turquoise: #4dd0e1;
        --disney-mint: #b2dfdb;

        /* Legacy support - map old names */
        --primary: var(--disney-royal-blue);
        --secondary: var(--disney-sky);
        --accent: var(--disney-gold);
        --primary-blue: var(--disney-royal-blue);
        --primary-teal: var(--disney-sky);
        --accent-gold: var(--disney-gold);
        --accent-purple: var(--disney-purple);

        /* Neutrals */
        --white: #FFFFFF;
        --gray-50: #FAFAFA;
        --gray-100: #F5F5F5;
        --gray-200: #EEEEEE;
        --gray-300: #E0E0E0;
        --gray-400: #BDBDBD;
        --gray-500: #9E9E9E;
        --gray-600: #757575;
        --gray-700: #616161;
        --gray-800: #424242;
        --gray-900: #212121;

        /* Magical Backgrounds */
        --bg-primary: linear-gradient(135deg, #1a237e 0%, #283593 50%, #3949ab 100%);
        --bg-secondary: linear-gradient(180deg, #e8eaf6 0%, #fff 50%, #fce4ec 100%);
        --bg-card: rgba(255, 255, 255, 0.95);
        --bg-glass: rgba(255, 255, 255, 0.85);

        /* Spacing */
        --space-1: 0.25rem;
        --space-2: 0.5rem;
        --space-3: 0.75rem;
        --space-4: 1rem;
        --space-5: 1.25rem;
        --space-6: 1.5rem;
        --space-8: 2rem;
        --space-10: 2.5rem;
        --space-12: 3rem;

        /* Radius */
        --radius-sm: 0.5rem;
        --radius-md: 0.75rem;
        --radius-lg: 1rem;
        --radius-xl: 1.5rem;
        --radius-2xl: 2rem;
        --radius-full: 9999px;

        /* Magical Shadows */
        --shadow-sm: 0 2px 4px rgba(26, 35, 126, 0.1);
        --shadow: 0 4px 12px rgba(26, 35, 126, 0.15);
        --shadow-md: 0 8px 24px rgba(26, 35, 126, 0.2);
        --shadow-lg: 0 12px 40px rgba(26, 35, 126, 0.25);
        --shadow-xl: 0 20px 60px rgba(26, 35, 126, 0.3);
        --shadow-glow: 0 0 30px rgba(255, 215, 0, 0.4);
        --shadow-pink-glow: 0 0 20px rgba(244, 143, 177, 0.3);

        /* Transitions */
        --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        --transition-slow: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        --transition-bounce: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    }

    /* ============================================================================
       ✨ MAGICAL ANIMATIONS
    ============================================================================ */

    @keyframes sparkle {
        0%, 100% { opacity: 0; transform: scale(0) rotate(0deg); }
        50% { opacity: 1; transform: scale(1) rotate(180deg); }
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }

    @keyframes shimmer {
        0% { background-position: -200% center; }
        100% { background-position: 200% center; }
    }

    @keyframes twinkle {
        0%, 100% { opacity: 0.3; transform: scale(0.8); }
        50% { opacity: 1; transform: scale(1.2); }
    }

    @keyframes glow-pulse {
        0%, 100% { box-shadow: 0 0 20px rgba(255, 215, 0, 0.3); }
        50% { box-shadow: 0 0 40px rgba(255, 215, 0, 0.6); }
    }

    @keyframes castle-fade {
        0%, 100% { opacity: 0.03; }
        50% { opacity: 0.06; }
    }

    @keyframes mickey-bob {
        0%, 100% { transform: translateY(0) rotate(-5deg); }
        50% { transform: translateY(-5px) rotate(5deg); }
    }

    @keyframes firework {
        0% { transform: scale(0); opacity: 1; }
        50% { transform: scale(1); opacity: 0.8; }
        100% { transform: scale(1.5); opacity: 0; }
    }

    @keyframes rainbow-border {
        0% { border-color: var(--disney-gold); }
        25% { border-color: var(--disney-pink); }
        50% { border-color: var(--disney-purple); }
        75% { border-color: var(--disney-teal); }
        100% { border-color: var(--disney-gold); }
    }

    /* ============================================================================
       🏰 CASTLE & MICKEY SVG BACKGROUNDS
    ============================================================================ */

    /* Castle silhouette pattern */
    .castle-bg {
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 200'%3E%3Cpath fill='%231a237e' fill-opacity='0.03' d='M100 180 L100 120 L80 120 L80 100 L70 100 L70 80 L60 80 L60 60 L50 60 L50 40 L70 40 L70 30 L75 30 L75 20 L80 20 L80 30 L90 30 L90 40 L100 40 L100 30 L105 30 L105 20 L110 20 L110 30 L120 30 L120 40 L130 40 L130 60 L140 60 L140 80 L150 80 L150 100 L140 100 L140 120 L120 120 L120 180 Z'/%3E%3C/svg%3E");
        background-size: 150px 150px;
    }

    /* Mickey head pattern */
    .mickey-pattern {
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='55' r='25' fill='%231a237e' fill-opacity='0.04'/%3E%3Ccircle cx='30' cy='30' r='15' fill='%231a237e' fill-opacity='0.04'/%3E%3Ccircle cx='70' cy='30' r='15' fill='%231a237e' fill-opacity='0.04'/%3E%3C/svg%3E");
        background-size: 80px 80px;
    }

    /* ============================================================================
       BASE STYLES - Disney Typography
    ============================================================================ */

    body {
        font-family: 'Quicksand', -apple-system, BlinkMacSystemFont, sans-serif !important;
        font-size: 16px;
        line-height: 1.7;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        background: var(--bg-secondary) !important;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Cinzel', serif !important;
        font-weight: 700;
        line-height: 1.3;
        color: var(--disney-royal-blue);
        letter-spacing: 0.02em;
    }

    p {
        line-height: 1.7;
        color: var(--gray-700);
    }

    /* ============================================================================
       🌟 MAIN LAYOUT - Magical Background
    ============================================================================ */

    .main {
        background: linear-gradient(180deg,
            #e8eaf6 0%,
            #ffffff 30%,
            #fff8e1 60%,
            #fce4ec 100%) !important;
        padding: var(--space-6) !important;
        position: relative;
        min-height: 100vh;
    }

    /* Floating castle watermark */
    .main::before {
        content: '';
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 600px;
        height: 600px;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 200'%3E%3Cpath fill='%231a237e' fill-opacity='0.025' d='M100 180 L100 120 L80 120 L80 100 L70 100 L70 80 L60 80 L60 60 L50 60 L50 40 L70 40 L70 30 L75 30 L75 15 L80 15 L80 30 L90 30 L90 40 L100 40 L100 25 L105 25 L105 10 L110 10 L110 25 L120 25 L120 40 L130 40 L130 60 L140 60 L140 80 L150 80 L150 100 L140 100 L140 120 L120 120 L120 180 Z'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-position: center;
        background-size: contain;
        pointer-events: none;
        z-index: 0;
        animation: castle-fade 8s ease-in-out infinite;
    }

    /* Sparkle particles */
    .main::after {
        content: '✦';
        position: fixed;
        font-size: 20px;
        color: var(--disney-gold);
        top: 20%;
        right: 10%;
        animation: twinkle 3s ease-in-out infinite;
        pointer-events: none;
        z-index: 0;
    }

    .main .block-container {
        max-width: 1400px !important;
        padding: var(--space-8) var(--space-6) !important;
        position: relative;
        z-index: 1;
    }

    /* ============================================================================
       🎀 SIDEBAR - Magical Kingdom Panel
    ============================================================================ */

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg,
            var(--disney-royal-blue) 0%,
            #283593 40%,
            #3949ab 100%) !important;
        border-right: 3px solid var(--disney-gold) !important;
        box-shadow: var(--shadow-lg) !important;
        position: relative;
        overflow: hidden;
    }

    /* Mickey pattern overlay on sidebar */
    [data-testid="stSidebar"]::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='55' r='25' fill='white' fill-opacity='0.03'/%3E%3Ccircle cx='30' cy='30' r='15' fill='white' fill-opacity='0.03'/%3E%3Ccircle cx='70' cy='30' r='15' fill='white' fill-opacity='0.03'/%3E%3C/svg%3E");
        background-size: 100px 100px;
        pointer-events: none;
    }

    [data-testid="stSidebar"] > div {
        padding: var(--space-6) var(--space-4) !important;
        position: relative;
        z-index: 1;
    }

    /* Sidebar headers */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: var(--white) !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    [data-testid="stSidebar"] h1 {
        font-size: 1.5rem;
        margin-bottom: var(--space-6);
        padding-bottom: var(--space-4);
        border-bottom: 2px solid var(--disney-gold);
        display: flex;
        align-items: center;
        gap: var(--space-2);
    }

    [data-testid="stSidebar"] h1::before {
        content: '🏰';
        font-size: 1.3rem;
    }

    [data-testid="stSidebar"] h2 {
        font-size: 1.125rem;
        margin-top: var(--space-6);
        margin-bottom: var(--space-3);
    }

    [data-testid="stSidebar"] label {
        color: var(--disney-light-gold) !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        margin-bottom: var(--space-2) !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }

    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span {
        color: rgba(255,255,255,0.9) !important;
    }

    /* Sidebar collapse button */
    [data-testid="stSidebar"] button[kind="header"] {
        background: var(--disney-gold) !important;
        border: none !important;
        padding: var(--space-2) !important;
        color: var(--disney-royal-blue) !important;
        border-radius: var(--radius-full) !important;
        font-size: 0 !important;
    }

    /* ============================================================================
       👑 HEADER - Magical Castle Banner
    ============================================================================ */

    .main-header {
        background: linear-gradient(135deg,
            var(--disney-royal-blue) 0%,
            var(--disney-purple) 50%,
            var(--disney-sky) 100%);
        padding: var(--space-10) var(--space-8);
        border-radius: var(--radius-2xl);
        margin-bottom: var(--space-8);
        text-align: center;
        box-shadow: var(--shadow-xl), inset 0 -3px 0 rgba(0,0,0,0.1);
        position: relative;
        overflow: hidden;
        border: 3px solid var(--disney-gold);
    }

    /* Castle silhouette in header */
    .main-header::before {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 300px;
        height: 150px;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 100'%3E%3Cpath fill='rgba(255,255,255,0.1)' d='M100 100 L100 60 L85 60 L85 50 L75 50 L75 40 L65 40 L65 25 L80 25 L80 15 L85 15 L85 10 L90 10 L90 20 L100 20 L100 10 L105 10 L105 5 L110 5 L110 15 L115 15 L115 25 L120 25 L120 40 L135 40 L135 50 L125 50 L125 60 L115 60 L115 100 Z'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-position: center bottom;
        background-size: contain;
        pointer-events: none;
    }

    /* Mickey heads decorating header */
    .main-header::after {
        content: '';
        position: absolute;
        top: 15px;
        right: 20px;
        width: 60px;
        height: 60px;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='55' r='25' fill='rgba(255,215,0,0.3)'/%3E%3Ccircle cx='30' cy='30' r='15' fill='rgba(255,215,0,0.3)'/%3E%3Ccircle cx='70' cy='30' r='15' fill='rgba(255,215,0,0.3)'/%3E%3C/svg%3E");
        background-size: contain;
        animation: mickey-bob 4s ease-in-out infinite;
    }

    /* Sparkle decorations */
    .main-header h1::before,
    .main-header h1::after {
        content: '✨';
        animation: twinkle 2s ease-in-out infinite;
    }

    .main-header h1::after {
        animation-delay: 1s;
    }

    .main-header h1 {
        color: var(--white) !important;
        font-size: 2.75rem;
        margin: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: var(--space-4);
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3), 0 0 30px rgba(255,215,0,0.3);
        position: relative;
        z-index: 2;
        animation: float 6s ease-in-out infinite;
    }

    .main-header p {
        color: var(--disney-light-gold) !important;
        font-size: 1.25rem;
        margin-top: var(--space-4);
        margin-bottom: 0;
        font-family: 'Satisfy', cursive !important;
        font-weight: 400;
        position: relative;
        z-index: 2;
    }

    /* ============================================================================
       🎭 TABS - Magical Navigation
    ============================================================================ */

    .stTabs {
        background: var(--bg-card);
        border-radius: var(--radius-xl);
        padding: var(--space-5);
        box-shadow: var(--shadow-md);
        margin-bottom: var(--space-6);
        border: 2px solid var(--disney-light-purple);
        position: relative;
        overflow: hidden;
    }

    /* Subtle mickey pattern in tabs */
    .stTabs::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='55' r='25' fill='%237b1fa2' fill-opacity='0.02'/%3E%3Ccircle cx='30' cy='30' r='15' fill='%237b1fa2' fill-opacity='0.02'/%3E%3Ccircle cx='70' cy='30' r='15' fill='%237b1fa2' fill-opacity='0.02'/%3E%3C/svg%3E");
        background-size: 60px 60px;
        pointer-events: none;
    }

    [data-baseweb="tab-list"] {
        gap: var(--space-3);
        background: linear-gradient(135deg, var(--disney-ice) 0%, var(--disney-rose) 100%) !important;
        border-radius: var(--radius-lg) !important;
        padding: var(--space-2) !important;
        border: 1px solid var(--disney-light-purple);
    }

    [data-baseweb="tab"] {
        background: transparent !important;
        border: none !important;
        border-radius: var(--radius-lg) !important;
        padding: var(--space-3) var(--space-6) !important;
        color: var(--disney-royal-blue) !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        transition: var(--transition) !important;
        white-space: nowrap !important;
        position: relative;
    }

    [data-baseweb="tab"]:hover {
        background: rgba(255,255,255,0.8) !important;
        color: var(--disney-purple) !important;
        transform: translateY(-2px);
    }

    [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, var(--white) 0%, var(--disney-sparkle) 100%) !important;
        color: var(--disney-royal-blue) !important;
        box-shadow: var(--shadow), 0 0 15px rgba(255,215,0,0.2) !important;
        font-weight: 700 !important;
        border: 2px solid var(--disney-gold) !important;
    }

    [data-baseweb="tab"][aria-selected="true"]::before {
        content: '✨';
        position: absolute;
        top: -8px;
        right: -5px;
        font-size: 14px;
        animation: twinkle 2s ease-in-out infinite;
    }

    /* Hide the tab underline */
    [data-baseweb="tab-highlight"] {
        display: none !important;
    }

    /* ============================================================================
       🎁 CARDS - Magical Card Design
    ============================================================================ */

    .card {
        background: var(--bg-card);
        border: 2px solid var(--disney-light-purple);
        border-radius: var(--radius-xl);
        padding: var(--space-6);
        margin-bottom: var(--space-4);
        transition: var(--transition);
        box-shadow: var(--shadow);
        position: relative;
        overflow: hidden;
    }

    .card::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 50px;
        height: 50px;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='55' r='25' fill='%23ffd700' fill-opacity='0.1'/%3E%3Ccircle cx='30' cy='30' r='15' fill='%23ffd700' fill-opacity='0.1'/%3E%3Ccircle cx='70' cy='30' r='15' fill='%23ffd700' fill-opacity='0.1'/%3E%3C/svg%3E");
        background-size: contain;
        opacity: 0;
        transition: var(--transition);
    }

    .card:hover {
        border-color: var(--disney-gold);
        box-shadow: var(--shadow-lg), var(--shadow-glow);
        transform: translateY(-4px);
    }

    .card:hover::before {
        opacity: 1;
    }

    /* ============================================================================
       ✅ CHECKLIST CARDS - Magical Task Cards
    ============================================================================ */

    .checklist-card {
        background: linear-gradient(135deg, var(--white) 0%, var(--disney-sparkle) 100%);
        border: 2px solid var(--disney-light-purple);
        border-left: 5px solid var(--disney-gold);
        border-radius: var(--radius-lg);
        padding: var(--space-5);
        margin-bottom: var(--space-3);
        transition: var(--transition);
        position: relative;
        overflow: hidden;
        width: 100%;
    }

    .checklist-card::before {
        content: '';
        position: absolute;
        top: -20px;
        right: -20px;
        width: 60px;
        height: 60px;
        background: radial-gradient(circle, var(--disney-gold) 0%, transparent 70%);
        opacity: 0;
        transition: var(--transition);
    }

    .checklist-card:hover {
        border-color: var(--disney-gold);
        box-shadow: var(--shadow-md), 0 0 20px rgba(255,215,0,0.15);
        transform: translateX(5px);
    }

    .checklist-card:hover::before {
        opacity: 0.3;
    }

    .checklist-card.completed {
        background: linear-gradient(135deg, var(--gray-50) 0%, var(--disney-mint) 100%);
        opacity: 0.85;
        border-left-color: #10B981;
    }

    .checklist-card.completed::after {
        content: '✓';
        position: absolute;
        top: 10px;
        right: 15px;
        font-size: 24px;
        color: #10B981;
        font-weight: bold;
    }

    /* Priority colors with Disney flair */
    .checklist-card.priority-high,
    .checklist-card[data-priority="high"] {
        border-left-color: #E91E63;
        background: linear-gradient(135deg, var(--white) 0%, #fce4ec 100%);
    }

    .checklist-card.priority-medium,
    .checklist-card[data-priority="medium"] {
        border-left-color: var(--disney-gold);
        background: linear-gradient(135deg, var(--white) 0%, var(--disney-light-gold) 100%);
    }

    .checklist-card.priority-low,
    .checklist-card[data-priority="low"] {
        border-left-color: var(--disney-teal);
        background: linear-gradient(135deg, var(--white) 0%, var(--disney-mint) 100%);
    }

    .checklist-card strong {
        color: var(--disney-royal-blue);
        font-size: 1.05rem;
        font-weight: 700;
        display: block;
        margin-bottom: var(--space-2);
    }

    .checklist-card small {
        color: var(--gray-600);
        font-size: 0.85rem;
    }

    .checklist-card-content {
        position: relative;
        z-index: 1;
    }

    /* ============================================================================
       💡 IDEA CARDS - Sparkling Suggestion Cards
    ============================================================================ */

    .idea-card {
        background: linear-gradient(135deg, var(--white) 0%, var(--disney-rose) 50%, var(--disney-light-gold) 100%);
        border: 2px solid var(--disney-pink);
        border-radius: var(--radius-xl);
        padding: var(--space-6);
        margin-bottom: var(--space-4);
        transition: var(--transition);
        box-shadow: var(--shadow);
        position: relative;
        overflow: hidden;
    }

    .idea-card::before {
        content: '💡';
        position: absolute;
        top: 15px;
        right: 20px;
        font-size: 28px;
        opacity: 0.3;
        animation: float 3s ease-in-out infinite;
    }

    .idea-card:hover {
        border-color: var(--disney-gold);
        box-shadow: var(--shadow-lg), var(--shadow-pink-glow);
        transform: scale(1.02);
    }

    .idea-card h3 {
        color: var(--disney-purple) !important;
        font-size: 1.25rem;
        margin-bottom: var(--space-3);
    }

    .idea-card p {
        color: var(--gray-700);
        line-height: 1.6;
    }

    .idea-card small {
        color: var(--gray-500);
        display: block;
        margin-top: var(--space-3);
        padding-top: var(--space-3);
        border-top: 1px dashed var(--disney-light-purple);
    }

    /* ============================================================================
       ⏰ COUNTDOWN BOX - Magical Timer
    ============================================================================ */

    .countdown-box {
        background: linear-gradient(135deg,
            var(--disney-royal-blue) 0%,
            var(--disney-purple) 50%,
            var(--disney-pink) 100%);
        color: var(--white);
        padding: var(--space-6) var(--space-8);
        border-radius: var(--radius-2xl);
        text-align: center;
        font-size: 1.4rem;
        font-weight: 700;
        font-family: 'Cinzel', serif;
        box-shadow: var(--shadow-xl);
        margin: var(--space-6) 0;
        position: relative;
        overflow: hidden;
        border: 3px solid var(--disney-gold);
        animation: glow-pulse 4s ease-in-out infinite;
    }

    .countdown-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='55' r='25' fill='white' fill-opacity='0.05'/%3E%3Ccircle cx='30' cy='30' r='15' fill='white' fill-opacity='0.05'/%3E%3Ccircle cx='70' cy='30' r='15' fill='white' fill-opacity='0.05'/%3E%3C/svg%3E");
        background-size: 80px 80px;
        pointer-events: none;
    }

    .countdown-box::after {
        content: '✨🏰✨';
        display: block;
        font-size: 0.9rem;
        margin-top: var(--space-2);
        letter-spacing: 8px;
        animation: twinkle 3s ease-in-out infinite;
    }

    /* ============================================================================
       💎 TRIP CODE DIAMOND - Magical Code Display
    ============================================================================ */

    .trip-code-diamond {
        background: linear-gradient(135deg,
            var(--disney-royal-blue) 0%,
            var(--disney-purple) 100%);
        color: var(--white);
        padding: var(--space-6);
        border-radius: var(--radius-xl);
        text-align: center;
        margin: var(--space-6) 0;
        box-shadow: var(--shadow-lg);
        position: relative;
        border: 3px solid var(--disney-gold);
    }

    .trip-code-diamond::before,
    .trip-code-diamond::after {
        content: '💎';
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        font-size: 2rem;
        animation: twinkle 2s ease-in-out infinite;
    }

    .trip-code-diamond::before {
        left: 20px;
    }

    .trip-code-diamond::after {
        right: 20px;
        animation-delay: 1s;
    }

    .trip-code-diamond h3 {
        color: var(--disney-gold) !important;
        font-size: 1.5rem;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    .trip-code-diamond p {
        color: rgba(255,255,255,0.9) !important;
        margin-top: var(--space-2);
        margin-bottom: 0;
        font-size: 0.95rem;
    }

    /* ============================================================================
       🎯 BUTTONS - Magical Disney Buttons
    ============================================================================ */

    .stButton {
        margin: 0 !important;
    }

    .stButton > button {
        background: linear-gradient(135deg,
            var(--disney-royal-blue) 0%,
            var(--disney-purple) 50%,
            var(--disney-sky) 100%) !important;
        color: var(--white) !important;
        border: 2px solid var(--disney-gold) !important;
        border-radius: var(--radius-lg) !important;
        padding: var(--space-3) var(--space-6) !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        font-family: 'Quicksand', sans-serif !important;
        transition: var(--transition-bounce) !important;
        box-shadow: var(--shadow), 0 0 0 0 rgba(255,215,0,0.4) !important;
        cursor: pointer !important;
        width: 100% !important;
        text-align: center !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        position: relative !important;
        overflow: hidden !important;
    }

    /* Shimmer effect */
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,0.3),
            transparent
        );
        transition: 0.5s;
    }

    .stButton > button:hover::before {
        left: 100%;
    }

    .stButton > button:hover {
        box-shadow: var(--shadow-lg), 0 0 20px rgba(255,215,0,0.5) !important;
        transform: translateY(-3px) scale(1.02);
        border-color: var(--disney-light-gold) !important;
    }

    .stButton > button:active {
        transform: translateY(-1px) scale(0.98);
    }

    /* Delete button - Magical trash */
    .card-delete-btn {
        flex-shrink: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
        width: 40px !important;
        max-width: 40px !important;
        overflow: hidden !important;
        position: relative !important;
    }

    .card-delete-btn .stButton {
        margin: 0 !important;
        padding: 0 !important;
        width: 40px !important;
        min-width: 40px !important;
        max-width: 40px !important;
        overflow: hidden !important;
    }

    .card-delete-btn button {
        background: linear-gradient(135deg, #E91E63 0%, #AD1457 100%) !important;
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
        font-size: 1.1rem !important;
        overflow: hidden !important;
        position: relative !important;
        left: 0 !important;
        right: 0 !important;
        border: 2px solid #F48FB1 !important;
    }

    .card-delete-btn button:hover {
        background: linear-gradient(135deg, #C2185B 0%, #880E4F 100%) !important;
        transform: scale(1.1) rotate(10deg);
        box-shadow: 0 0 15px rgba(233,30,99,0.4) !important;
    }

    /* Button row layout */
    .button-row {
        display: flex !important;
        gap: var(--space-3) !important;
        align-items: center !important;
        justify-content: space-between !important;
        margin-top: var(--space-3) !important;
        width: 100% !important;
    }

    .button-row > *:not(.card-delete-btn) {
        flex: 1 1 auto !important;
        min-width: 0 !important;
    }

    .button-row .card-delete-btn {
        flex: 0 0 40px !important;
        min-width: 40px !important;
        max-width: 40px !important;
        margin-left: var(--space-3) !important;
    }

    /* Card action row */
    .card-action-row {
        display: flex !important;
        align-items: center !important;
        gap: var(--space-2) !important;
        margin-top: var(--space-3) !important;
    }

    /* ============================================================================
       📝 INPUTS - Magical Form Fields
    ============================================================================ */

    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div,
    .stMultiSelect > div > div,
    .stNumberInput > div > div > input,
    .stDateInput > div > div > input {
        background: var(--white) !important;
        border: 2px solid var(--disney-light-purple) !important;
        border-radius: var(--radius-md) !important;
        padding: var(--space-3) var(--space-4) !important;
        font-size: 0.95rem !important;
        color: var(--gray-900) !important;
        transition: var(--transition) !important;
        font-family: 'Quicksand', sans-serif !important;
    }

    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div:focus-within,
    .stNumberInput > div > div > input:focus,
    .stDateInput > div > div > input:focus {
        border-color: var(--disney-gold) !important;
        box-shadow: 0 0 0 3px rgba(255,215,0,0.2), var(--shadow) !important;
        outline: none !important;
    }

    /* Sidebar inputs */
    [data-testid="stSidebar"] .stTextInput > div > div > input,
    [data-testid="stSidebar"] .stSelectbox > div > div,
    [data-testid="stSidebar"] .stMultiSelect > div > div,
    [data-testid="stSidebar"] .stNumberInput > div > div > input,
    [data-testid="stSidebar"] .stDateInput > div > div > input {
        background: rgba(255,255,255,0.95) !important;
        border-color: var(--disney-gold) !important;
    }

    /* ============================================================================
       ☑️ CHECKBOXES - Disney Style Checkboxes
    ============================================================================ */

    .stCheckbox {
        padding: var(--space-2) 0;
    }

    .stCheckbox > label {
        color: var(--disney-royal-blue) !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        display: flex !important;
        align-items: center !important;
        gap: var(--space-3) !important;
    }

    .stCheckbox input[type="checkbox"] {
        width: 22px !important;
        height: 22px !important;
        border-radius: var(--radius-sm) !important;
        border: 2px solid var(--disney-light-purple) !important;
        background: var(--white) !important;
        cursor: pointer !important;
        flex-shrink: 0 !important;
        transition: var(--transition) !important;
    }

    .stCheckbox input[type="checkbox"]:checked {
        background: linear-gradient(135deg, var(--disney-royal-blue), var(--disney-purple)) !important;
        border-color: var(--disney-gold) !important;
    }

    .stCheckbox input[type="checkbox"]:hover {
        border-color: var(--disney-gold) !important;
        box-shadow: 0 0 10px rgba(255,215,0,0.3) !important;
    }

    /* Sidebar checkboxes */
    [data-testid="stSidebar"] .stCheckbox > label {
        color: var(--white) !important;
    }

    /* ============================================================================
       🏷️ BADGES - Magical Pill Badges
    ============================================================================ */

    .badge {
        display: inline-flex;
        align-items: center;
        padding: var(--space-1) var(--space-3);
        border-radius: var(--radius-full);
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .badge-primary {
        background: linear-gradient(135deg, var(--disney-ice), var(--disney-light-purple));
        color: var(--disney-royal-blue);
        border: 1px solid var(--disney-light-purple);
    }

    .badge-success {
        background: linear-gradient(135deg, #E8F5E9, #C8E6C9);
        color: #2E7D32;
        border: 1px solid #A5D6A7;
    }

    .badge-warning {
        background: linear-gradient(135deg, var(--disney-light-gold), #FFE082);
        color: #F57F17;
        border: 1px solid var(--disney-gold);
    }

    .badge-danger {
        background: linear-gradient(135deg, #FCE4EC, #F8BBD9);
        color: #C2185B;
        border: 1px solid #F48FB1;
    }

    /* ============================================================================
       🔔 ALERTS - Magical Notifications
    ============================================================================ */

    .stAlert {
        background: var(--white) !important;
        border: 2px solid var(--disney-light-purple) !important;
        border-left: 5px solid var(--disney-royal-blue) !important;
        border-radius: var(--radius-lg) !important;
        padding: var(--space-4) !important;
        margin: var(--space-4) 0 !important;
        box-shadow: var(--shadow) !important;
    }

    .stSuccess {
        border-left-color: #4CAF50 !important;
        background: linear-gradient(135deg, var(--white), #E8F5E9) !important;
    }

    .stWarning {
        border-left-color: var(--disney-gold) !important;
        background: linear-gradient(135deg, var(--white), var(--disney-light-gold)) !important;
    }

    .stError {
        border-left-color: #E91E63 !important;
        background: linear-gradient(135deg, var(--white), #FCE4EC) !important;
    }

    .stInfo {
        border-left-color: var(--disney-sky) !important;
        background: linear-gradient(135deg, var(--white), var(--disney-ice)) !important;
    }

    /* ============================================================================
       💬 CHAT INTERFACE - Magical Message Bubbles
    ============================================================================ */

    .stChatMessage {
        background: var(--white) !important;
        border: 2px solid var(--disney-light-purple) !important;
        border-radius: var(--radius-xl) !important;
        padding: var(--space-5) !important;
        margin-bottom: var(--space-4) !important;
        box-shadow: var(--shadow) !important;
        position: relative;
    }

    .stChatMessage[data-testid="chat-message-user"] {
        background: linear-gradient(135deg, var(--disney-ice), var(--disney-rose)) !important;
        border-color: var(--disney-pink) !important;
        margin-left: 10%;
    }

    .stChatMessage[data-testid="chat-message-user"]::before {
        content: '👤';
        position: absolute;
        top: -10px;
        right: 15px;
        font-size: 20px;
    }

    .stChatMessage[data-testid="chat-message-assistant"] {
        background: linear-gradient(135deg, var(--white), var(--disney-light-gold)) !important;
        border-color: var(--disney-gold) !important;
        margin-right: 10%;
    }

    .stChatMessage[data-testid="chat-message-assistant"]::before {
        content: '🤖✨';
        position: absolute;
        top: -10px;
        left: 15px;
        font-size: 20px;
    }

    /* Chat input */
    .stChatInput {
        border: 2px solid var(--disney-light-purple) !important;
        border-radius: var(--radius-xl) !important;
        overflow: hidden;
    }

    .stChatInput:focus-within {
        border-color: var(--disney-gold) !important;
        box-shadow: 0 0 15px rgba(255,215,0,0.2) !important;
    }

    /* ============================================================================
       📊 METRICS - Magical Dashboard Cards
    ============================================================================ */

    [data-testid="stMetric"] {
        background: linear-gradient(135deg, var(--white), var(--disney-sparkle));
        border: 2px solid var(--disney-light-purple);
        border-radius: var(--radius-xl);
        padding: var(--space-6);
        box-shadow: var(--shadow);
        transition: var(--transition);
        position: relative;
        overflow: hidden;
    }

    [data-testid="stMetric"]::before {
        content: '✨';
        position: absolute;
        top: 10px;
        right: 15px;
        font-size: 20px;
        opacity: 0.5;
        animation: twinkle 3s ease-in-out infinite;
    }

    [data-testid="stMetric"]:hover {
        border-color: var(--disney-gold);
        box-shadow: var(--shadow-md), var(--shadow-glow);
        transform: translateY(-3px);
    }

    [data-testid="stMetricLabel"] {
        color: var(--disney-purple);
        font-size: 0.9rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    [data-testid="stMetricValue"] {
        color: var(--disney-royal-blue);
        font-size: 2.25rem;
        font-weight: 800;
        margin-top: var(--space-2);
        font-family: 'Cinzel', serif;
    }

    /* ============================================================================
       📈 PROGRESS BAR - Magical Progress
    ============================================================================ */

    .stProgress > div > div {
        background: linear-gradient(90deg, var(--disney-ice), var(--disney-light-purple)) !important;
        border-radius: var(--radius-full) !important;
        height: 12px !important;
        border: 1px solid var(--disney-light-purple);
    }

    .stProgress > div > div > div {
        background: linear-gradient(90deg,
            var(--disney-royal-blue) 0%,
            var(--disney-purple) 50%,
            var(--disney-pink) 100%) !important;
        border-radius: var(--radius-full) !important;
        position: relative;
        overflow: hidden;
    }

    .stProgress > div > div > div::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(
            90deg,
            transparent 0%,
            rgba(255,255,255,0.4) 50%,
            transparent 100%
        );
        animation: shimmer 2s infinite;
    }

    /* ============================================================================
       📂 EXPANDER - Magical Accordion
    ============================================================================ */

    .streamlit-expanderHeader {
        background: linear-gradient(135deg, var(--white), var(--disney-sparkle)) !important;
        border: 2px solid var(--disney-light-purple) !important;
        border-radius: var(--radius-lg) !important;
        padding: var(--space-4) !important;
        font-weight: 700 !important;
        color: var(--disney-royal-blue) !important;
        transition: var(--transition) !important;
    }

    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, var(--disney-sparkle), var(--disney-light-gold)) !important;
        border-color: var(--disney-gold) !important;
        box-shadow: var(--shadow) !important;
    }

    .streamlit-expanderContent {
        border: 2px solid var(--disney-light-purple) !important;
        border-top: none !important;
        border-radius: 0 0 var(--radius-lg) var(--radius-lg) !important;
        padding: var(--space-5) !important;
        background: var(--white) !important;
    }

    /* ============================================================================
       📜 SCROLLBAR - Magical Scrollbar
    ============================================================================ */

    ::-webkit-scrollbar {
        width: 14px;
        height: 14px;
    }

    ::-webkit-scrollbar-track {
        background: var(--disney-ice);
        border-radius: var(--radius-full);
    }

    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, var(--disney-light-purple), var(--disney-pink));
        border-radius: var(--radius-full);
        border: 3px solid var(--disney-ice);
    }

    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, var(--disney-purple), var(--disney-pink));
    }

    /* ============================================================================
       📱 RESPONSIVE DESIGN
    ============================================================================ */

    @media (max-width: 768px) {
        .main .block-container {
            padding: var(--space-4) var(--space-3) !important;
        }

        .main-header h1 {
            font-size: 1.75rem;
        }

        .main-header {
            padding: var(--space-6) var(--space-4);
        }

        .main-header::after {
            display: none;
        }

        [data-baseweb="tab"] {
            padding: var(--space-2) var(--space-3) !important;
            font-size: 0.85rem !important;
        }

        .card, .checklist-card, .idea-card {
            padding: var(--space-4);
        }

        .countdown-box {
            font-size: 1.1rem;
            padding: var(--space-4) var(--space-5);
        }

        .trip-code-diamond::before,
        .trip-code-diamond::after {
            display: none;
        }
    }

    /* ============================================================================
       🔧 STREAMLIT-SPECIFIC FIXES
    ============================================================================ */

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Fix toolbar */
    .stApp [data-testid="stToolbar"] {
        display: none;
    }

    /* Fix columns */
    [data-testid="column"] {
        padding: 0 var(--space-2) !important;
        overflow: hidden !important;
        position: relative !important;
    }

    [data-testid="column"]:first-child {
        padding-left: 0 !important;
    }

    [data-testid="column"]:last-child {
        padding-right: 0 !important;
        flex: 0 0 44px !important;
        width: 44px !important;
        min-width: 44px !important;
        max-width: 44px !important;
        overflow: hidden !important;
    }

    /* Checklist card columns */
    .checklist-card [data-testid="column"] {
        display: flex !important;
        align-items: center !important;
        overflow: hidden !important;
    }

    .checklist-card [data-testid="column"]:first-child {
        flex: 1 1 auto !important;
        min-width: 0 !important;
        padding-right: var(--space-3) !important;
    }

    .checklist-card [data-testid="column"]:last-child {
        flex: 0 0 44px !important;
        width: 44px !important;
        max-width: 44px !important;
        justify-content: center !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* Force delete button bounds */
    .checklist-card [data-testid="column"]:last-child * {
        max-width: 40px !important;
        max-height: 40px !important;
    }

    /* Stacking context */
    .stButton,
    .stCheckbox,
    .stTextInput,
    .stSelectbox {
        position: relative;
        z-index: 1;
    }

    /* Spinner */
    .stSpinner > div {
        border-color: var(--disney-gold) transparent var(--disney-purple) transparent !important;
    }

    /* ============================================================================
       🎨 UTILITY CLASSES
    ============================================================================ */

    .mt-1 { margin-top: var(--space-1) !important; }
    .mt-2 { margin-top: var(--space-2) !important; }
    .mt-3 { margin-top: var(--space-3) !important; }
    .mt-4 { margin-top: var(--space-4) !important; }
    .mt-6 { margin-top: var(--space-6) !important; }
    .mt-8 { margin-top: var(--space-8) !important; }

    .mb-1 { margin-bottom: var(--space-1) !important; }
    .mb-2 { margin-bottom: var(--space-2) !important; }
    .mb-3 { margin-bottom: var(--space-3) !important; }
    .mb-4 { margin-bottom: var(--space-4) !important; }
    .mb-6 { margin-bottom: var(--space-6) !important; }
    .mb-8 { margin-bottom: var(--space-8) !important; }

    .flex { display: flex !important; }
    .items-center { align-items: center !important; }
    .justify-between { justify-content: space-between !important; }
    .gap-2 { gap: var(--space-2) !important; }
    .gap-3 { gap: var(--space-3) !important; }
    .gap-4 { gap: var(--space-4) !important; }

    .text-center { text-align: center !important; }
    .font-bold { font-weight: 700 !important; }
    .text-sm { font-size: 0.875rem !important; }
    .text-xs { font-size: 0.75rem !important; }

    /* ============================================================================
       🌟 SPECIAL DISNEY FLOURISHES
    ============================================================================ */

    /* Dividers with Mickey heads */
    hr {
        border: none;
        height: 3px;
        background: linear-gradient(90deg,
            transparent 0%,
            var(--disney-light-purple) 20%,
            var(--disney-gold) 50%,
            var(--disney-light-purple) 80%,
            transparent 100%);
        margin: var(--space-8) 0;
        position: relative;
    }

    hr::after {
        content: '🏰';
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        background: var(--white);
        padding: 0 var(--space-3);
        font-size: 1.25rem;
    }

    /* Selection highlight */
    ::selection {
        background: var(--disney-light-gold);
        color: var(--disney-royal-blue);
    }

    /* Focus outline */
    :focus-visible {
        outline: 3px solid var(--disney-gold);
        outline-offset: 2px;
    }

</style>
"""
