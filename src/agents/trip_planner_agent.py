"""
Disney Trip Planning Agent - AI-powered trip planning assistant
"""
import os
import json
from typing import List, Dict, Any
from openai import OpenAI
from datetime import datetime

from src.models.trip_data import TripDetails, ChecklistItem, IdeaSuggestion
from src.utils.helpers import get_trip_phase, generate_checklist_id


class TripPlannerAgent:
    """
    AI Agent responsible for:
    - Creating comprehensive checklists
    - Brainstorming trip ideas
    - Providing suggestions
    - Managing pre-trip needs
    """

    def __init__(self, api_key: str, model: str = "gpt-4-turbo-preview"):
        """Initialize the Trip Planner Agent with OpenAI"""
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.system_prompt = self._build_system_prompt()

    def _build_system_prompt(self) -> str:
        """Build the system prompt for the agent"""
        return """You are an expert Disney trip planning assistant with deep knowledge of:
- Walt Disney World, Disneyland, and other Disney destinations
- Trip planning logistics and timelines
- Family travel needs and considerations
- Disney-specific tips, tricks, and hidden gems

Your role is to help families plan magical Disney vacations by:
1. Creating comprehensive, personalized checklists
2. Brainstorming creative ideas and suggestions
3. Anticipating needs (both obvious and easily forgotten)
4. Providing actionable, specific advice

Be enthusiastic, helpful, and thorough. Consider different age groups, special needs,
budget constraints, and timeframes when making recommendations."""

    def generate_comprehensive_checklist(self, trip_details: TripDetails) -> List[ChecklistItem]:
        """
        Generate a comprehensive checklist based on trip details
        Includes obvious items and easily forgotten ones
        """
        phase = get_trip_phase(trip_details.start_date)
        days_until = (trip_details.start_date - datetime.now()).days

        prompt = f"""Generate a comprehensive Disney trip checklist for the following trip:

Destination: {trip_details.destination}
Trip Date: {trip_details.start_date.strftime('%B %d, %Y')}
Days Until Trip: {days_until}
Party Size: {trip_details.party_size}
Ages: {', '.join(map(str, trip_details.ages)) if trip_details.ages else 'Not specified'}
Interests: {', '.join(trip_details.interests) if trip_details.interests else 'General Disney experience'}
Special Needs: {', '.join(trip_details.special_needs) if trip_details.special_needs else 'None'}

Planning Phase: {phase}

Create a checklist with:
1. Time-sensitive items (booking, reservations)
2. Pre-trip preparations (what to buy, arrange)
3. Packing essentials
4. Day-of-travel items
5. IMPORTANT: Include easily forgotten items (phone chargers, portable batteries, medications, rain gear, etc.)
6. Disney-specific items (MagicBands, park tickets confirmation, Genie+ planning, etc.)

For each item, specify:
- The task description
- Category (booking, shopping, packing, documents, tech, disney-specific, etc.)
- Priority (high, medium, low)
- Suggested deadline (relative to trip date)

Return ONLY a valid JSON array of checklist items with this structure:
[
  {{
    "text": "Book park reservations",
    "category": "booking",
    "priority": "high",
    "deadline": "60 days before"
  }}
]"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                response_format={"type": "json_object"}
            )

            content = response.choices[0].message.content
            # Parse the response - handle both direct array and object with items key
            data = json.loads(content)
            if isinstance(data, dict) and "items" in data:
                items_data = data["items"]
            elif isinstance(data, list):
                items_data = data
            else:
                items_data = list(data.values())[0] if data else []

            checklist = []
            for item in items_data:
                checklist.append(ChecklistItem(
                    id=generate_checklist_id(),
                    text=item.get("text", ""),
                    category=item.get("category", "general"),
                    priority=item.get("priority", "medium"),
                    deadline=item.get("deadline"),
                    completed=False
                ))

            return checklist

        except Exception as e:
            print(f"Error generating checklist: {e}")
            return self._get_fallback_checklist()

    def brainstorm_ideas(self, trip_details: TripDetails, focus: str = "general") -> List[IdeaSuggestion]:
        """
        Brainstorm creative ideas and suggestions for the trip

        Args:
            trip_details: Trip information
            focus: Specific focus area (dining, activities, surprises, budget-friendly, etc.)
        """
        prompt = f"""Brainstorm creative Disney trip ideas for:

Destination: {trip_details.destination}
Party Size: {trip_details.party_size}
Ages: {', '.join(map(str, trip_details.ages)) if trip_details.ages else 'Not specified'}
Interests: {', '.join(trip_details.interests) if trip_details.interests else 'All Disney experiences'}
Budget: {trip_details.budget_range or 'Not specified'}
Focus Area: {focus}

Generate 8-10 creative, specific ideas that could enhance this trip. Include:
- Unique dining experiences
- Special activities or experiences
- Hidden gems and lesser-known attractions
- Photo opportunities
- Budget-friendly magic moments
- Special surprises for kids/family
- Time-saving tips specific to their situation

Return ONLY a valid JSON object with an "ideas" array:
{{
  "ideas": [
    {{
      "title": "Brief catchy title",
      "description": "Detailed description of the idea",
      "category": "dining|activities|photos|surprises|tips",
      "tags": ["tag1", "tag2"]
    }}
  ]
}}"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.9,  # Higher temperature for creativity
                response_format={"type": "json_object"}
            )

            content = response.choices[0].message.content
            data = json.loads(content)
            ideas_data = data.get("ideas", [])

            ideas = []
            for idea in ideas_data:
                ideas.append(IdeaSuggestion(
                    id=generate_checklist_id(),
                    title=idea.get("title", ""),
                    description=idea.get("description", ""),
                    category=idea.get("category", "general"),
                    tags=idea.get("tags", []),
                    saved=False
                ))

            return ideas

        except Exception as e:
            print(f"Error brainstorming ideas: {e}")
            return []

    def get_personalized_suggestion(self, trip_details: TripDetails, question: str) -> str:
        """
        Get a personalized suggestion or answer to a specific question
        """
        prompt = f"""Answer this question about a Disney trip:

Question: {question}

Trip Context:
- Destination: {trip_details.destination}
- Date: {trip_details.start_date.strftime('%B %d, %Y')}
- Party Size: {trip_details.party_size}
- Ages: {', '.join(map(str, trip_details.ages)) if trip_details.ages else 'Not specified'}
- Interests: {', '.join(trip_details.interests) if trip_details.interests else 'General'}

Provide a helpful, specific answer tailored to their situation. Be conversational and enthusiastic."""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"I apologize, but I encountered an error: {str(e)}"

    def suggest_forgotten_items(self, current_checklist: List[ChecklistItem]) -> List[str]:
        """
        Analyze current checklist and suggest commonly forgotten items
        """
        current_items = [item.text for item in current_checklist]

        prompt = f"""Given this Disney trip checklist, what commonly forgotten items are missing?

Current checklist:
{json.dumps(current_items, indent=2)}

List 5-10 commonly forgotten items that aren't on this list. Focus on:
- Technology items (chargers, batteries, etc.)
- Comfort items (sunscreen, band-aids, etc.)
- Disney-specific items
- Travel documents or confirmations
- Weather-related items

Return as a simple JSON array of strings:
{{"forgotten_items": ["item 1", "item 2"]}}"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                response_format={"type": "json_object"}
            )

            content = response.choices[0].message.content
            data = json.loads(content)
            return data.get("forgotten_items", [])

        except Exception as e:
            print(f"Error suggesting forgotten items: {e}")
            return []

    def _get_fallback_checklist(self) -> List[ChecklistItem]:
        """Fallback checklist if AI generation fails"""
        fallback_items = [
            ("Book park reservations", "booking", "high"),
            ("Purchase park tickets", "booking", "high"),
            ("Book dining reservations (180 days out)", "booking", "high"),
            ("Book hotel accommodations", "booking", "high"),
            ("Purchase travel insurance", "booking", "medium"),
            ("Charge MagicBands", "disney-specific", "medium"),
            ("Download My Disney Experience app", "tech", "high"),
            ("Pack phone chargers and portable battery", "tech", "high"),
            ("Pack comfortable walking shoes", "packing", "high"),
            ("Pack sunscreen and hats", "packing", "high"),
            ("Pack rain ponchos", "packing", "medium"),
            ("Prepare day bags/backpacks", "packing", "medium"),
            ("Print park tickets and confirmations", "documents", "high"),
            ("Pack medications and first aid kit", "packing", "high"),
            ("Notify bank of travel plans", "documents", "medium"),
        ]

        return [
            ChecklistItem(
                id=generate_checklist_id(),
                text=text,
                category=category,
                priority=priority,
                completed=False
            )
            for text, category, priority in fallback_items
        ]
