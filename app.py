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

from src.agents.trip_planner_agent import TripPlannerAgent
from src.models.trip_data import TripDetails, ChecklistItem, IdeaSuggestion
from src.utils.helpers import calculate_countdown, format_countdown, get_trip_phase

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Disney Trip Planner",
    page_icon="🏰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Disney theming
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #0047AB;
        font-size: 3em;
        font-weight: bold;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .countdown-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        font-size: 2em;
        font-weight: bold;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .checklist-item {
        padding: 10px;
        margin: 5px 0;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        background-color: #f8f9fa;
    }
    .idea-card {
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        background: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #764ba2;
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .priority-high { border-left-color: #dc3545; }
    .priority-medium { border-left-color: #ffc107; }
    .priority-low { border-left-color: #28a745; }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'agent' not in st.session_state:
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        st.session_state.agent = TripPlannerAgent(api_key)
    else:
        st.session_state.agent = None

if 'trip_details' not in st.session_state:
    st.session_state.trip_details = None

if 'checklist' not in st.session_state:
    st.session_state.checklist = []

if 'ideas' not in st.session_state:
    st.session_state.ideas = []

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []


def main():
    """Main application"""
    # Header
    st.markdown('<h1 class="main-header">🏰 Disney Trip Planning Agent ✨</h1>', unsafe_allow_html=True)

    # Check for API key
    if not st.session_state.agent:
        st.error("⚠️ OpenAI API key not found!")
        st.info("Please create a `.env` file with your `OPENAI_API_KEY`")
        api_key = st.text_input("Or enter your API key here:", type="password")
        if api_key:
            st.session_state.agent = TripPlannerAgent(api_key)
            st.rerun()
        return

    # Sidebar - Trip Setup
    with st.sidebar:
        st.header("🎯 Trip Details")

        destination = st.selectbox(
            "Destination",
            ["Walt Disney World", "Disneyland Resort", "Disneyland Paris",
             "Tokyo Disney Resort", "Hong Kong Disneyland", "Shanghai Disney Resort"]
        )

        trip_date = st.date_input(
            "Trip Start Date",
            value=datetime.now() + timedelta(days=90),
            min_value=datetime.now()
        )

        trip_end_date = st.date_input(
            "Trip End Date",
            value=datetime.now() + timedelta(days=94),
            min_value=trip_date
        )

        party_size = st.number_input("Party Size", min_value=1, max_value=20, value=4)

        ages_input = st.text_input("Ages (comma-separated)", "8, 10, 35, 37")
        ages = [int(age.strip()) for age in ages_input.split(',') if age.strip().isdigit()]

        interests = st.multiselect(
            "Interests",
            ["Thrill Rides", "Character Meet & Greets", "Shows & Entertainment",
             "Dining Experiences", "Shopping", "Relaxation", "Photography",
             "Fireworks & Parades", "Water Parks", "Resort Activities"],
            default=["Character Meet & Greets", "Fireworks & Parades"]
        )

        budget = st.selectbox(
            "Budget Range",
            ["Budget-Friendly", "Moderate", "Deluxe", "No Budget Constraints"]
        )

        special_needs = st.multiselect(
            "Special Considerations",
            ["Wheelchair Access", "Dietary Restrictions", "First-Time Visitors",
             "Celebrating Special Occasion", "Traveling with Toddlers", "Traveling with Teens"]
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

                st.success("✅ Trip plan created!")
                st.rerun()

    # Main content
    if not st.session_state.trip_details:
        st.info("👈 Start by entering your trip details in the sidebar and click 'Create Trip Plan'")
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

        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader("Your Personalized Checklist")
        with col2:
            if st.button("🔍 Find Forgotten Items"):
                with st.spinner("Analyzing checklist..."):
                    forgotten = st.session_state.agent.suggest_forgotten_items(
                        st.session_state.checklist
                    )
                    if forgotten:
                        st.write("**Don't forget:**")
                        for item in forgotten:
                            st.write(f"- {item}")

        # Filter options
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

        # Display checklist
        for idx, item in enumerate(st.session_state.checklist):
            if not show_completed and item.completed:
                continue
            if item.priority not in priority_filter:
                continue
            if item.category not in category_filter:
                continue

            col1, col2, col3 = st.columns([1, 6, 2])

            with col1:
                checked = st.checkbox(
                    "Done",
                    value=item.completed,
                    key=f"check_{idx}",
                    label_visibility="collapsed"
                )
                if checked != item.completed:
                    st.session_state.checklist[idx].completed = checked

            with col2:
                priority_class = f"priority-{item.priority}"
                st.markdown(f"""
                <div class="checklist-item {priority_class}">
                    <strong>{item.text}</strong><br>
                    <small>📁 {item.category} | ⭐ {item.priority.upper()}
                    {f"| 📅 {item.deadline}" if item.deadline else ""}</small>
                </div>
                """, unsafe_allow_html=True)

            with col3:
                if st.button("🗑️", key=f"delete_{idx}"):
                    st.session_state.checklist.pop(idx)
                    st.rerun()

        # Add custom item
        st.markdown("---")
        st.subheader("➕ Add Custom Item")
        new_col1, new_col2, new_col3 = st.columns([3, 1, 1])
        with new_col1:
            new_item_text = st.text_input("Item description", key="new_item")
        with new_col2:
            new_item_category = st.text_input("Category", "custom", key="new_category")
        with new_col3:
            new_item_priority = st.selectbox("Priority", ["high", "medium", "low"], key="new_priority")

        if st.button("Add to Checklist") and new_item_text:
            from src.utils.helpers import generate_checklist_id
            new_item = ChecklistItem(
                id=generate_checklist_id(),
                text=new_item_text,
                category=new_item_category,
                priority=new_item_priority,
                completed=False
            )
            st.session_state.checklist.append(new_item)
            st.success(f"✅ Added: {new_item_text}")
            st.rerun()

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
                    st.rerun()

    # Tab 3: AI Assistant
    with tab3:
        st.header("🤖 AI Trip Planning Assistant")
        st.write("Ask me anything about your Disney trip!")

        # Chat interface
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.write(message["content"])

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

            # Add assistant message
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": response
            })

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


if __name__ == "__main__":
    main()
