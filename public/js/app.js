// ============================================================================
// DISNEY TRIP PLANNER - ROYAL PRINCESS EDITION
// Professional JavaScript Application
// ============================================================================

// Application State
const state = {
    tripCode: null,
    tripDetails: null,
    checklist: [],
    ideas: [],
    chatHistory: [],
    rejectedItems: new Set()
};

// ============================================================================
// INITIALIZATION
// ============================================================================

document.addEventListener('DOMContentLoaded', () => {
    initializeApp();
    setupEventListeners();
    loadSavedData();
});

function initializeApp() {
    console.log('🏰 Disney Trip Planner Initialized');

    // Set minimum date for trip dates to today
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('startDate').min = today;
    document.getElementById('endDate').min = today;

    // Update end date minimum when start date changes
    document.getElementById('startDate').addEventListener('change', (e) => {
        document.getElementById('endDate').min = e.target.value;
    });
}

function setupEventListeners() {
    // Tab navigation
    document.querySelectorAll('.tab-button').forEach(button => {
        button.addEventListener('click', () => switchTab(button.dataset.tab));
    });

    // Trip form submission
    document.getElementById('tripForm').addEventListener('submit', handleTripFormSubmit);

    // Chat input - Enter key
    document.getElementById('chatInput').addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage();
    });

    // Filter changes
    document.getElementById('showCompleted')?.addEventListener('change', renderChecklist);
    document.querySelectorAll('.priority-filter').forEach(filter => {
        filter.addEventListener('change', renderChecklist);
    });
}

// ============================================================================
// TRIP CODE MANAGEMENT
// ============================================================================

function createTrip() {
    const tripCode = document.getElementById('newTripCode').value.trim();

    if (!tripCode || tripCode.length < 3) {
        showNotification('Trip code must be at least 3 characters long', 'error');
        return;
    }

    // Check if trip exists (in real implementation, check with backend)
    const existingData = localStorage.getItem(`trip_${tripCode}`);
    if (existingData) {
        showNotification(`Trip code '${tripCode}' already exists! Use 'Join Existing Trip' instead.`, 'error');
        return;
    }

    state.tripCode = tripCode;
    showTripCodeDisplay();
    saveData();
    showNotification(`✅ Created trip with code: ${tripCode}`, 'success');
}

function joinTrip() {
    const tripCode = document.getElementById('joinTripCode').value.trim();

    if (!tripCode) {
        showNotification('Please enter a trip code', 'error');
        return;
    }

    // Try to load trip data
    const tripData = localStorage.getItem(`trip_${tripCode}`);
    if (!tripData) {
        showNotification(`Trip code '${tripCode}' not found!`, 'error');
        return;
    }

    state.tripCode = tripCode;
    loadTripData(tripCode);
    showTripCodeDisplay();
    showNotification(`✅ Joined trip: ${tripCode}`, 'success');
}

function changeTrip() {
    if (confirm('Are you sure you want to change trips? Unsaved progress may be lost.')) {
        document.getElementById('tripCodeSetup').classList.remove('hidden');
        document.getElementById('tripCodeDisplay').classList.add('hidden');
        document.getElementById('mainContent').classList.add('hidden');
        state.tripCode = null;
    }
}

function showTripCodeDisplay() {
    document.getElementById('tripCodeSetup').classList.add('hidden');
    document.getElementById('tripCodeDisplay').classList.remove('hidden');
    document.getElementById('currentTripCode').textContent = state.tripCode;
    document.getElementById('mainContent').classList.remove('hidden');
}

// ============================================================================
// TAB NAVIGATION
// ============================================================================

function switchTab(tabName) {
    // Update buttons
    document.querySelectorAll('.tab-button').forEach(btn => {
        btn.classList.remove('active');
    });
    event.target.classList.add('active');

    // Update content
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });
    document.getElementById(`${tabName}Tab`).classList.add('active');
}

// ============================================================================
// TRIP FORM HANDLING
// ============================================================================

async function handleTripFormSubmit(e) {
    e.preventDefault();

    showLoading(true);

    try {
        // Collect form data
        const formData = {
            destination: document.getElementById('destination').value,
            startDate: document.getElementById('startDate').value,
            endDate: document.getElementById('endDate').value,
            partySize: parseInt(document.getElementById('partySize').value),
            ages: document.getElementById('ages').value.split(',').map(a => parseInt(a.trim())).filter(a => !isNaN(a)),
            interests: Array.from(document.querySelectorAll('input[name="interests"]:checked')).map(cb => cb.value),
            budget: document.getElementById('budget').value,
            specialNeeds: Array.from(document.querySelectorAll('input[name="special"]:checked')).map(cb => cb.value)
        };

        state.tripDetails = formData;

        // Start countdown
        startCountdown(formData.startDate);

        // Generate checklist and ideas
        await Promise.all([
            generateChecklist(formData),
            generateInitialIdeas(formData)
        ]);

        saveData();
        updateTripSummary();

        showNotification('✅ Trip plan created successfully!', 'success');
    } catch (error) {
        console.error('Error creating trip:', error);
        showNotification('Failed to create trip plan. Please try again.', 'error');
    } finally {
        showLoading(false);
    }
}

// ============================================================================
// COUNTDOWN TIMER
// ============================================================================

function startCountdown(targetDate) {
    const target = new Date(targetDate).getTime();

    function updateCountdown() {
        const now = new Date().getTime();
        const distance = target - now;

        if (distance < 0) {
            document.getElementById('countdownText').textContent = "🎉 Your magical day is here!";
            return;
        }

        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        document.getElementById('countdownText').textContent =
            `${days} days, ${hours} hours, ${minutes} minutes, ${seconds} seconds`;
    }

    updateCountdown();
    setInterval(updateCountdown, 1000);
}

// ============================================================================
// CHECKLIST MANAGEMENT
// ============================================================================

async function generateChecklist(tripDetails) {
    try {
        // In production, this would call a Netlify function
        // For now, generate a sample checklist
        const sampleChecklist = [
            { id: 1, text: 'Book Disney park tickets', category: 'bookings', priority: 'high', completed: false },
            { id: 2, text: 'Reserve hotel accommodations', category: 'bookings', priority: 'high', completed: false },
            { id: 3, text: 'Make dining reservations', category: 'dining', priority: 'high', completed: false },
            { id: 4, text: 'Pack sunscreen and sunglasses', category: 'packing', priority: 'medium', completed: false },
            { id: 5, text: 'Download Disney app', category: 'preparation', priority: 'medium', completed: false },
            { id: 6, text: 'Check weather forecast', category: 'preparation', priority: 'low', completed: false }
        ];

        state.checklist = sampleChecklist;
        renderChecklist();
    } catch (error) {
        console.error('Error generating checklist:', error);
    }
}

function renderChecklist() {
    const container = document.getElementById('checklistContainer');
    const showCompleted = document.getElementById('showCompleted')?.checked ?? true;
    const priorityFilters = Array.from(document.querySelectorAll('.priority-filter:checked')).map(cb => cb.value);

    const filtered = state.checklist.filter(item => {
        if (!showCompleted && item.completed) return false;
        if (priorityFilters.length > 0 && !priorityFilters.includes(item.priority)) return false;
        return true;
    });

    if (filtered.length === 0) {
        container.innerHTML = '<div class="empty-state"><p>No checklist items match your filters.</p></div>';
        return;
    }

    container.innerHTML = filtered.map(item => `
        <div class="checklist-item ${item.completed ? 'completed' : ''} priority-${item.priority}">
            <div class="checklist-item-title">${item.text}</div>
            <div class="checklist-item-meta">
                📁 ${item.category} | ⭐ ${item.priority.toUpperCase()}
            </div>
            <div class="checklist-item-actions">
                <label class="checkbox-label">
                    <input type="checkbox" ${item.completed ? 'checked' : ''}
                           onchange="toggleChecklistItem(${item.id})">
                    Complete
                </label>
                <button class="btn btn-delete" onclick="deleteChecklistItem(${item.id})">🗑️</button>
            </div>
        </div>
    `).join('');

    updateProgress();
}

function toggleChecklistItem(id) {
    const item = state.checklist.find(i => i.id === id);
    if (item) {
        item.completed = !item.completed;
        renderChecklist();
        saveData();
    }
}

function deleteChecklistItem(id) {
    const item = state.checklist.find(i => i.id === id);
    if (item) {
        state.rejectedItems.add(item.text.toLowerCase());
    }
    state.checklist = state.checklist.filter(i => i.id !== id);
    renderChecklist();
    saveData();
}

async function findForgottenItems() {
    showLoading(true);
    try {
        // In production, call Netlify function
        // For now, add sample forgotten items
        const forgottenItems = [
            { id: Date.now(), text: 'Portable phone charger', category: 'electronics', priority: 'medium', completed: false },
            { id: Date.now() + 1, text: 'Autograph book for characters', category: 'souvenirs', priority: 'low', completed: false }
        ];

        const newItems = forgottenItems.filter(item =>
            !state.rejectedItems.has(item.text.toLowerCase()) &&
            !state.checklist.some(existing => existing.text.toLowerCase() === item.text.toLowerCase())
        );

        if (newItems.length > 0) {
            state.checklist.push(...newItems);
            renderChecklist();
            saveData();
            showNotification(`✅ Added ${newItems.length} forgotten item(s) to your checklist!`, 'success');
        } else {
            showNotification('✨ Great job! You haven\'t forgotten anything important.', 'success');
        }
    } catch (error) {
        console.error('Error finding forgotten items:', error);
        showNotification('Failed to find forgotten items', 'error');
    } finally {
        showLoading(false);
    }
}

function toggleFilters() {
    const filterSection = document.getElementById('filterSection');
    filterSection.classList.toggle('hidden');
}

// ============================================================================
// IDEAS MANAGEMENT
// ============================================================================

async function generateInitialIdeas(tripDetails) {
    try {
        const sampleIdeas = [
            {
                id: 1,
                title: 'Character Breakfast at Cinderella\'s Royal Table',
                description: 'Start your day with a magical breakfast inside the castle with Disney princesses!',
                category: 'dining',
                tags: ['dining', 'characters', 'experience']
            },
            {
                id: 2,
                title: 'Catch the Evening Fireworks Show',
                description: 'End each day with the spectacular fireworks display. Arrive early for the best viewing spots!',
                category: 'entertainment',
                tags: ['fireworks', 'entertainment', 'evening']
            }
        ];

        state.ideas = sampleIdeas;
        renderIdeas();
    } catch (error) {
        console.error('Error generating ideas:', error);
    }
}

async function generateIdeas() {
    showLoading(true);
    try {
        const focus = document.getElementById('ideaFocus').value;

        // In production, call Netlify function with focus
        const newIdeas = [
            {
                id: Date.now(),
                title: `${focus.charAt(0).toUpperCase() + focus.slice(1)} Suggestion`,
                description: `A personalized suggestion based on your ${focus} preferences.`,
                category: focus,
                tags: [focus, 'ai-generated']
            }
        ];

        state.ideas.push(...newIdeas);
        renderIdeas();
        saveData();
        showNotification('✨ New ideas generated!', 'success');
    } catch (error) {
        console.error('Error generating ideas:', error);
        showNotification('Failed to generate ideas', 'error');
    } finally {
        showLoading(false);
    }
}

function renderIdeas() {
    const container = document.getElementById('ideasContainer');

    if (state.ideas.length === 0) {
        container.innerHTML = '<div class="empty-state"><p>✨ Generate your trip plan to see magical ideas!</p></div>';
        return;
    }

    container.innerHTML = state.ideas.map(idea => `
        <div class="idea-card">
            <h3>${idea.title}</h3>
            <p>${idea.description}</p>
            <div class="idea-card-meta">
                🏷️ ${idea.category} | Tags: ${idea.tags.join(', ')}
            </div>
        </div>
    `).join('');
}

// ============================================================================
// CHAT / AI ASSISTANT
// ============================================================================

async function sendMessage() {
    const input = document.getElementById('chatInput');
    const message = input.value.trim();

    if (!message) return;

    // Add user message
    addChatMessage('user', message);
    input.value = '';

    showLoading(true);

    try {
        // In production, call Netlify function
        const response = await getAIResponse(message);
        addChatMessage('assistant', response);
        saveData();
    } catch (error) {
        console.error('Error getting AI response:', error);
        addChatMessage('assistant', 'I apologize, but I\'m having trouble responding right now. Please try again later.');
    } finally {
        showLoading(false);
    }
}

async function getAIResponse(userMessage) {
    // In production, this would call a Netlify function
    // For now, return a sample response
    await new Promise(resolve => setTimeout(resolve, 1000));

    return `Thank you for your question about "${userMessage}". I'd be happy to help you plan your magical Disney vacation! Here are some suggestions based on your trip details...`;
}

function addChatMessage(role, content) {
    const container = document.getElementById('chatContainer');

    // Remove welcome message if it exists
    const welcome = container.querySelector('.chat-welcome');
    if (welcome) welcome.remove();

    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-message ${role}`;
    messageDiv.textContent = content;

    container.appendChild(messageDiv);
    container.scrollTop = container.scrollHeight;

    state.chatHistory.push({ role, content });
}

// ============================================================================
// TRIP SUMMARY
// ============================================================================

function updateTripSummary() {
    if (!state.tripDetails) return;

    const details = state.tripDetails;
    const detailsDisplay = document.getElementById('tripDetailsDisplay');

    const startDate = new Date(details.startDate);
    const endDate = new Date(details.endDate);
    const tripLength = Math.ceil((endDate - startDate) / (1000 * 60 * 60 * 24));

    detailsDisplay.innerHTML = `
        <p><strong>Destination:</strong> ${details.destination}</p>
        <p><strong>Start Date:</strong> ${startDate.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })}</p>
        <p><strong>End Date:</strong> ${endDate.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })}</p>
        <p><strong>Trip Length:</strong> ${tripLength} days</p>
        <p><strong>Party Size:</strong> ${details.partySize}</p>
        <p><strong>Ages:</strong> ${details.ages.join(', ')}</p>
        <p><strong>Interests:</strong> ${details.interests.join(', ')}</p>
        <p><strong>Budget:</strong> ${details.budget}</p>
        ${details.specialNeeds.length > 0 ? `<p><strong>Special Considerations:</strong> ${details.specialNeeds.join(', ')}</p>` : ''}
    `;

    updateProgress();
}

function updateProgress() {
    const total = state.checklist.length;
    const completed = state.checklist.filter(item => item.completed).length;
    const percentage = total > 0 ? Math.round((completed / total) * 100) : 0;

    document.getElementById('totalTasks').textContent = total;
    document.getElementById('completedTasks').textContent = completed;
    document.getElementById('remainingTasks').textContent = total - completed;
    document.getElementById('progressPercentage').textContent = `${percentage}%`;
    document.getElementById('progressFill').style.width = `${percentage}%`;
}

// ============================================================================
// DATA PERSISTENCE
// ============================================================================

function saveData() {
    if (!state.tripCode) return;

    const data = {
        tripDetails: state.tripDetails,
        checklist: state.checklist,
        ideas: state.ideas,
        chatHistory: state.chatHistory,
        rejectedItems: Array.from(state.rejectedItems)
    };

    localStorage.setItem(`trip_${state.tripCode}`, JSON.stringify(data));
    localStorage.setItem('lastTripCode', state.tripCode);
}

function loadSavedData() {
    const lastTripCode = localStorage.getItem('lastTripCode');

    if (lastTripCode) {
        const data = localStorage.getItem(`trip_${lastTripCode}`);
        if (data) {
            state.tripCode = lastTripCode;
            loadTripData(lastTripCode);
            showTripCodeDisplay();
        }
    }
}

function loadTripData(tripCode) {
    const data = JSON.parse(localStorage.getItem(`trip_${tripCode}`));

    if (data) {
        state.tripDetails = data.tripDetails;
        state.checklist = data.checklist || [];
        state.ideas = data.ideas || [];
        state.chatHistory = data.chatHistory || [];
        state.rejectedItems = new Set(data.rejectedItems || []);

        // Populate form if trip details exist
        if (state.tripDetails) {
            populateForm(state.tripDetails);
            startCountdown(state.tripDetails.startDate);
        }

        // Render all data
        renderChecklist();
        renderIdeas();
        updateTripSummary();

        // Restore chat history
        state.chatHistory.forEach(msg => {
            const container = document.getElementById('chatContainer');
            const welcome = container.querySelector('.chat-welcome');
            if (welcome) welcome.remove();

            const messageDiv = document.createElement('div');
            messageDiv.className = `chat-message ${msg.role}`;
            messageDiv.textContent = msg.content;
            container.appendChild(messageDiv);
        });
    }
}

function populateForm(details) {
    document.getElementById('destination').value = details.destination;
    document.getElementById('startDate').value = details.startDate;
    document.getElementById('endDate').value = details.endDate;
    document.getElementById('partySize').value = details.partySize;
    document.getElementById('ages').value = details.ages.join(', ');
    document.getElementById('budget').value = details.budget;

    // Set checkboxes
    details.interests.forEach(interest => {
        const checkbox = document.querySelector(`input[name="interests"][value="${interest}"]`);
        if (checkbox) checkbox.checked = true;
    });

    details.specialNeeds.forEach(need => {
        const checkbox = document.querySelector(`input[name="special"][value="${need}"]`);
        if (checkbox) checkbox.checked = true;
    });
}

function clearData() {
    if (!confirm('Are you sure you want to clear all trip data? This cannot be undone.')) {
        return;
    }

    if (state.tripCode) {
        localStorage.removeItem(`trip_${state.tripCode}`);
        localStorage.removeItem('lastTripCode');
    }

    // Reset state
    state.tripCode = null;
    state.tripDetails = null;
    state.checklist = [];
    state.ideas = [];
    state.chatHistory = [];
    state.rejectedItems = new Set();

    // Reset UI
    location.reload();
}

// ============================================================================
// UTILITY FUNCTIONS
// ============================================================================

function showLoading(show) {
    const overlay = document.getElementById('loadingOverlay');
    if (show) {
        overlay.classList.remove('hidden');
    } else {
        overlay.classList.add('hidden');
    }
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        background: ${type === 'success' ? 'var(--mint)' : type === 'error' ? 'var(--rose)' : 'var(--royal-purple)'};
        color: white;
        border-radius: var(--radius-md);
        box-shadow: var(--shadow-lg);
        z-index: 10000;
        animation: slideIn 0.3s ease-out;
    `;

    document.body.appendChild(notification);

    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease-out';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// ============================================================================
// EXPORT FUNCTIONS TO GLOBAL SCOPE (for onclick handlers)
// ============================================================================

window.createTrip = createTrip;
window.joinTrip = joinTrip;
window.changeTrip = changeTrip;
window.switchTab = switchTab;
window.toggleChecklistItem = toggleChecklistItem;
window.deleteChecklistItem = deleteChecklistItem;
window.findForgottenItems = findForgottenItems;
window.toggleFilters = toggleFilters;
window.generateIdeas = generateIdeas;
window.sendMessage = sendMessage;
window.saveData = saveData;
window.clearData = clearData;

console.log('✨ Disney Trip Planner Ready!');
