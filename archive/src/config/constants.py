"""
Application Constants for Disney Trip Planner
Centralized configuration for app-wide settings
"""
from pathlib import Path

# ============================================================================
# MEMORY LIMITS (Critical for Streamlit Cloud free tier - 1GB RAM)
# ============================================================================
MAX_CHAT_HISTORY = 50           # Max chat messages to retain
MAX_IDEAS = 30                   # Max idea suggestions to retain
MAX_PENDING_SUGGESTIONS = 20     # Max pending AI suggestions

# ============================================================================
# FILE PATHS
# ============================================================================
DATA_DIR = Path.home() / '.disney_trip_planner'
DATA_FILE = DATA_DIR / 'trip_data.pkl'

# ============================================================================
# OPENAI CONFIGURATION
# ============================================================================
DEFAULT_MODEL = "gpt-4-turbo-preview"
DEFAULT_TEMPERATURE = 0.7
MAX_TOKENS = 2000

# ============================================================================
# UI THEME COLORS - Disney Magical Kingdom Palette
# ============================================================================
THEME_COLORS = {
    # Disney Castle Blues
    'royal_blue': '#1a237e',
    'midnight': '#0d1b3e',
    'sky': '#5c6bc0',
    'light_blue': '#7986cb',
    'ice': '#e8eaf6',
    # Disney Golds & Sparkles
    'gold': '#FFD700',
    'light_gold': '#FFECB3',
    'bronze': '#CD853F',
    'sparkle': '#FFF8DC',
    # Disney Princess Purples & Pinks
    'purple': '#7b1fa2',
    'light_purple': '#CE93D8',
    'pink': '#F48FB1',
    'rose': '#FCE4EC',
    # Disney Magic Accents
    'teal': '#00BCD4',
    'turquoise': '#4DD0E1',
    'mint': '#B2DFDB',
    # Legacy Support
    'sky_blue': '#5c6bc0',
    'silver': '#CE93D8',
    'pastel_pink': '#F48FB1',
    'soft_purple': '#CE93D8',
    'cream': '#FFF8DC',
}

# ============================================================================
# FONTS - Disney-Inspired Typography
# ============================================================================
HEADER_FONT = 'Cinzel'
BODY_FONT = 'Quicksand'
SCRIPT_FONT = 'Satisfy'

# ============================================================================
# CHECKLIST CATEGORIES
# ============================================================================
CHECKLIST_CATEGORIES = [
    "General",
    "Documents",
    "Clothing",
    "Toiletries",
    "Electronics",
    "Park Essentials",
    "Comfort Items",
    "Special Items"
]

# ============================================================================
# IDEA CATEGORIES
# ============================================================================
IDEA_CATEGORIES = [
    "dining",
    "activities",
    "photos",
    "surprises",
    "tips"
]

# ============================================================================
# PRIORITY LEVELS
# ============================================================================
PRIORITY_LEVELS = ["low", "medium", "high"]

# ============================================================================
# DISNEY DESTINATIONS
# ============================================================================
DISNEY_DESTINATIONS = [
    "Walt Disney World (Florida)",
    "Disneyland Resort (California)",
    "Disneyland Paris",
    "Tokyo Disney Resort",
    "Hong Kong Disneyland",
    "Shanghai Disneyland"
]

# ============================================================================
# INTERESTS/PREFERENCES
# ============================================================================
INTEREST_OPTIONS = [
    "Thrill rides",
    "Character meet & greets",
    "Shows and entertainment",
    "Dining experiences",
    "Photography",
    "Shopping",
    "Relaxation",
    "Educational experiences"
]

# ============================================================================
# SPECIAL NEEDS OPTIONS
# ============================================================================
SPECIAL_NEEDS_OPTIONS = [
    "Wheelchair accessibility",
    "Dietary restrictions",
    "Sensory sensitivities",
    "Medical needs",
    "Language assistance"
]

# ============================================================================
# EMOJI CONSTANTS - Disney Magical Language
# ============================================================================
EMOJI = {
    # Disney Icons
    'castle': '🏰',
    'mickey': '🐭',
    'crown': '👑',
    'fairy': '🧚',
    'wand': '🪄',
    'magic': '🪄',
    # Sparkle & Magic
    'sparkle': '✨',
    'star': '⭐',
    'stars': '🌟',
    'fireworks': '🎆',
    'rainbow': '🌈',
    'diamond': '💎',
    # Actions & Status
    'check': '✅',
    'party': '🎉',
    'idea': '💡',
    'chat': '💬',
    'calendar': '📅',
    'clock': '⏰',
    'search': '🔍',
    'plus': '➕',
    'trash': '🗑️',
    'save': '💾',
    'download': '⬇️',
    'share': '🔗',
    # Notifications
    'warning': '⚠️',
    'info': 'ℹ️',
    'success': '✅',
    'error': '❌',
    # Family & Fun
    'family': '👨‍👩‍👧‍👦',
    'heart': '❤️',
    'gift': '🎁',
    'balloon': '🎈',
    'camera': '📸',
}

# ============================================================================
# TRIP PHASES (for contextual messaging)
# ============================================================================
TRIP_PHASES = {
    'early': 90,      # More than 90 days away
    'mid': 30,        # 30-90 days away
    'final': 7,       # 7-30 days away
    'imminent': 0     # Less than 7 days away
}
