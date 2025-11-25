/**
 * Disney Trip Planner - Royal Princess Edition
 * Main Application Logic
 */

// Global state
let tripData = {
    destination: 'Walt Disney World',
    partySize: 4,
    startDate: '2025-12-06',
    endDate: '2025-12-13',
    checklist: [],
    createdAt: null
};

// Function to scroll to character dining section
function scrollToCharacterDining() {
    const section = document.getElementById('character-dining-section');
    if (section) {
        section.style.display = 'block';
        scrollToID('#character-dining-section', 750);
    }
}

// Function to scroll to shows schedule section
function scrollToShowsSchedule() {
    const section = document.getElementById('shows-schedule-section');
    if (section) {
        section.style.display = 'block';
        scrollToID('#shows-schedule-section', 750);
    }
}

// Function to scroll to photo locations section
function scrollToPhotoLocations() {
    const section = document.getElementById('photo-locations-section');
    if (section) {
        section.style.display = 'block';
        scrollToID('#photo-locations-section', 750);
    }
}

// Initialize app when DOM is ready
$(document).ready(function() {
    loadData();
    initializeEventListeners();
    updateUI();
});

/**
 * Initialize all event listeners
 */
function initializeEventListeners() {
    // Trip form submission
    $('#trip-form').on('submit', function(e) {
        e.preventDefault();
        createTrip();
    });

    // Set minimum date to today for date inputs
    const today = new Date().toISOString().split('T')[0];
    $('#startDate').attr('min', today);
    $('#endDate').attr('min', today);

    // Update end date minimum when start date changes
    $('#startDate').on('change', function() {
        $('#endDate').attr('min', $(this).val());
    });
}

/**
 * Create a new trip plan
 */
function createTrip() {
    const destination = $('#destination').val();
    const partySize = parseInt($('#partySize').val());
    const startDate = $('#startDate').val();
    const endDate = $('#endDate').val();

    // Validation
    if (!destination || !startDate || !endDate) {
        alert('Please fill in all fields!');
        return;
    }

    if (new Date(endDate) < new Date(startDate)) {
        alert('End date must be after start date!');
        return;
    }

    // Update trip data
    tripData.destination = destination;
    tripData.partySize = partySize;
    tripData.startDate = startDate;
    tripData.endDate = endDate;
    tripData.createdAt = new Date().toISOString();

    // Generate checklist
    tripData.checklist = generateChecklist(destination, partySize, startDate, endDate);

    // Save and update UI
    saveData();
    updateUI();

    // Scroll to dashboard to see stats
    scrollToID('#summary', 750);

    // Show success message
    showNotification('✨ Your magical trip plan has been created!', 'success');
}

/**
 * Generate checklist items based on trip parameters
 */
function generateChecklist(destination, partySize, startDate, endDate) {
    const tripLengthDays = Math.ceil((new Date(endDate) - new Date(startDate)) / (1000 * 60 * 60 * 24)) + 1;
    const checklist = [];

    // Haulbrook Family Specific Items
    checklist.push({
        id: generateId(),
        title: '🎟️ Mickey\'s Very Merry Christmas Party Tickets',
        description: 'Confirm party tickets for Tuesday, Dec 9. Enter at 4:00 PM',
        category: 'Planning',
        daysBeforeTrip: 30,
        completed: false
    });

    checklist.push({
        id: generateId(),
        title: '⛳ Mini Golf Passes',
        description: 'Free mini golf passes included! Fantasia Gardens or Winter Summerland',
        category: 'Planning',
        daysBeforeTrip: 0,
        completed: false
    });

    checklist.push({
        id: generateId(),
        title: '🏨 Check-In at Coronado Springs',
        description: 'Resort check-in at 3:00 PM on Saturday, Dec 6',
        category: 'Planning',
        daysBeforeTrip: 1,
        completed: false
    });

    // Pre-trip planning items
    checklist.push({
        id: generateId(),
        title: '🎟️ Book Park Tickets',
        description: `Purchase ${partySize}-day park tickets for ${destination}`,
        category: 'Planning',
        daysBeforeTrip: 60,
        completed: false
    });

    checklist.push({
        id: generateId(),
        title: '🏨 Reserve Hotel',
        description: `Book accommodations for ${tripLengthDays} nights near ${destination}`,
        category: 'Planning',
        daysBeforeTrip: 45,
        completed: false
    });

    checklist.push({
        id: generateId(),
        title: '🍽️ Make Dining Reservations',
        description: 'Book character dining and popular restaurants (reservations open 60 days in advance)',
        category: 'Planning',
        daysBeforeTrip: 60,
        completed: false
    });

    if (destination === 'Walt Disney World') {
        checklist.push({
            id: generateId(),
            title: '⚡ Book Genie+ Lightning Lanes',
            description: 'Set up Disney Genie+ and Individual Lightning Lane selections',
            category: 'Planning',
            daysBeforeTrip: 7,
            completed: false
        });
    }

    checklist.push({
        id: generateId(),
        title: '✈️ Arrange Transportation',
            description: 'Book flights, rental car, or airport shuttle service',
        category: 'Travel',
        daysBeforeTrip: 30,
        completed: false
    });

    // Packing items
    checklist.push({
        id: generateId(),
        title: '🎒 Pack Comfortable Shoes',
        description: `Bring ${partySize} pairs of broken-in walking shoes (you'll walk 10+ miles/day!)`,
        category: 'Packing',
        daysBeforeTrip: 3,
        completed: false
    });

    checklist.push({
        id: generateId(),
        title: '🧴 Sunscreen & Toiletries',
        description: 'Pack sunscreen, hand sanitizer, medications, and daily essentials',
        category: 'Packing',
        daysBeforeTrip: 3,
        completed: false
    });

    checklist.push({
        id: generateId(),
        title: '📱 Download My Disney Experience App',
        description: 'Install app, link tickets, make park reservations, and check wait times',
        category: 'Technology',
        daysBeforeTrip: 7,
        completed: false
    });

    checklist.push({
        id: generateId(),
        title: '🔋 Pack Portable Chargers',
        description: 'Bring power banks to keep phones charged for photos and mobile ordering',
        category: 'Packing',
        daysBeforeTrip: 3,
        completed: false
    });

    checklist.push({
        id: generateId(),
        title: '💳 Prepare MagicBands or Park Tickets',
        description: 'Set up MagicBands (WDW) or have park tickets ready on phone',
        category: 'Technology',
        daysBeforeTrip: 7,
        completed: false
    });

    // Weather-specific items
    checklist.push({
        id: generateId(),
        title: '☂️ Pack Rain Gear',
        description: 'Bring ponchos or light rain jackets (Florida afternoon showers are common)',
        category: 'Packing',
        daysBeforeTrip: 3,
        completed: false
    });

    if (partySize > 2) {
        checklist.push({
            id: generateId(),
            title: '🚸 Prepare Child Safety Plan',
            description: 'Take photos of kids in daily outfits, have meeting spots, consider wristbands with contact info',
            category: 'Safety',
            daysBeforeTrip: 7,
            completed: false
        });
    }

    // Day-of items
    checklist.push({
        id: generateId(),
        title: '🎫 Check-In for Park Reservations',
        description: 'Verify park reservations and Lightning Lane bookings in My Disney Experience',
        category: 'Day-Of',
        daysBeforeTrip: 0,
        completed: false
    });

    checklist.push({
        id: generateId(),
        title: '🥤 Pack Refillable Water Bottles',
        description: 'Bring water bottles to stay hydrated (free water refills at quick-service locations)',
        category: 'Packing',
        daysBeforeTrip: 1,
        completed: false
    });

    checklist.push({
        id: generateId(),
        title: '🍿 Bring Snacks',
        description: 'Pack granola bars, crackers, or fruit for quick energy between meals',
        category: 'Packing',
        daysBeforeTrip: 1,
        completed: false
    });

    checklist.push({
        id: generateId(),
        title: '📸 Charge Camera/Phone',
        description: 'Fully charge all devices the night before park days',
        category: 'Technology',
        daysBeforeTrip: 0,
        completed: false
    });

    return checklist;
}

/**
 * Find forgotten items using AI-like suggestions
 */
function findForgottenItems() {
    if (!tripData.startDate || tripData.checklist.length === 0) {
        alert('Please create your trip plan first!');
        return;
    }

    const commonForgottenItems = [
        {
            title: '🩹 First Aid Kit',
            description: 'Band-aids, pain relievers, blister treatment, allergy medication',
            category: 'Health'
        },
        {
            title: '🕶️ Sunglasses & Hats',
            description: 'Sun protection for everyone in your party',
            category: 'Packing'
        },
        {
            title: '👕 Extra Clothes',
            description: 'Change of clothes in case of spills, rain, or water rides',
            category: 'Packing'
        },
        {
            title: '💰 Budget Extra Cash',
            description: 'Plan for souvenirs, snacks, and unexpected purchases',
            category: 'Planning'
        },
        {
            title: '🎁 Autograph Book',
            description: 'Bring book and Sharpie for character meet-and-greets',
            category: 'Fun'
        },
        {
            title: '📦 Ship Souvenirs Home',
            description: 'Consider having large purchases shipped to avoid packing them',
            category: 'Planning'
        }
    ];

    // Find items not already in checklist
    const newItems = [];
    commonForgottenItems.forEach(item => {
        const exists = tripData.checklist.some(checkItem =>
            checkItem.title.toLowerCase().includes(item.title.toLowerCase().substring(2))
        );

        if (!exists) {
            newItems.push({
                id: generateId(),
                title: item.title,
                description: item.description,
                category: item.category,
                daysBeforeTrip: 7,
                completed: false
            });
        }
    });

    if (newItems.length > 0) {
        tripData.checklist = [...tripData.checklist, ...newItems];
        saveData();
        updateUI();
        showNotification(`✨ Added ${newItems.length} helpful items to your checklist!`, 'success');
        scrollToID('#checklist', 750);
    } else {
        showNotification('🎉 You\'re all set! No forgotten items found.', 'info');
    }
}

/**
 * Toggle checklist item completion
 */
function toggleChecklistItem(itemId) {
    const item = tripData.checklist.find(i => i.id === itemId);
    if (item) {
        item.completed = !item.completed;
        saveData();
        updateUI();
    }
}

/**
 * Delete checklist item
 */
function deleteChecklistItem(itemId) {
    if (confirm('Are you sure you want to remove this item?')) {
        tripData.checklist = tripData.checklist.filter(i => i.id !== itemId);
        saveData();
        updateUI();
        showNotification('Item removed from checklist', 'info');
    }
}

/**
 * Update all UI elements
 */
function updateUI() {
    updateChecklistDisplay();
    updateCountdown();
    updateSummary();
    updateProgressDisplay();
}

/**
 * Update checklist display
 */
function updateChecklistDisplay() {
    const container = $('#checklist-container');

    if (tripData.checklist.length === 0) {
        container.html(`
            <div class="col-md-12">
                <div class="empty-state" style="text-align: center; padding: 60px 20px;">
                    <i class="fa fa-magic" style="font-size: 72px; color: #B8A4D9; margin-bottom: 20px;"></i>
                    <h3>Create Your Trip Plan First!</h3>
                    <p style="font-size: 18px;">Fill out the form above to generate your personalized checklist</p>
                </div>
            </div>
        `);
        return;
    }

    // Sort by category and completion status
    const sortedChecklist = [...tripData.checklist].sort((a, b) => {
        if (a.completed !== b.completed) return a.completed ? 1 : -1;
        return a.category.localeCompare(b.category);
    });

    let html = '<div class="col-md-12">';

    sortedChecklist.forEach(item => {
        const completedClass = item.completed ? 'completed' : '';
        const checkedAttr = item.completed ? 'checked' : '';

        html += `
            <div class="checklist-item ${completedClass}" data-id="${item.id}">
                <h4>${item.title}</h4>
                <p>${item.description}</p>
                <div class="checklist-meta">
                    <span><i class="fa fa-tag"></i> ${item.category}</span>
                    ${item.daysBeforeTrip > 0 ? `<span style="margin-left: 15px;"><i class="fa fa-clock-o"></i> ${item.daysBeforeTrip} days before trip</span>` : '<span style="margin-left: 15px;"><i class="fa fa-calendar-check-o"></i> Day of trip</span>'}
                </div>
                <div class="checkbox-wrapper" style="margin-top: 15px;">
                    <input type="checkbox"
                           id="check-${item.id}"
                           ${checkedAttr}
                           onchange="toggleChecklistItem('${item.id}')">
                    <label for="check-${item.id}" style="margin: 0; cursor: pointer;">
                        ${item.completed ? 'Completed ✓' : 'Mark as complete'}
                    </label>
                    <button class="delete-btn"
                            onclick="deleteChecklistItem('${item.id}')"
                            style="margin-left: auto;">
                        <i class="fa fa-trash"></i> Remove
                    </button>
                </div>
            </div>
        `;
    });

    html += '</div>';
    container.html(html);
}

/**
 * Update countdown timer
 */
function updateCountdown() {
    if (!tripData.startDate) {
        $('#countdown-text').html('Create your trip to see the countdown!');
        return;
    }

    const now = new Date();
    const tripStart = new Date(tripData.startDate + 'T00:00:00');
    const diff = tripStart - now;

    if (diff < 0) {
        $('#countdown-text').html('🎉 Your magical adventure has begun! 🎉');
        return;
    }

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));

    $('#countdown-text').html(`
        <strong>${days}</strong> days,
        <strong>${hours}</strong> hours,
        <strong>${minutes}</strong> minutes
    `);

    // Update every minute
    setTimeout(updateCountdown, 60000);
}

/**
 * Update trip summary
 */
function updateSummary() {
    if (!tripData.startDate) {
        $('#trip-details-summary').html('<p>Create your trip to see details here</p>');
        return;
    }

    const tripLengthDays = Math.ceil((new Date(tripData.endDate) - new Date(tripData.startDate)) / (1000 * 60 * 60 * 24)) + 1;
    const startDateFormatted = new Date(tripData.startDate).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
    const endDateFormatted = new Date(tripData.endDate).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });

    $('#trip-details-summary').html(`
        <p style="margin: 10px 0;"><strong>🎯 Destination:</strong><br>${tripData.destination}</p>
        <p style="margin: 10px 0;"><strong>👥 Party Size:</strong><br>${tripData.partySize} guests</p>
        <p style="margin: 10px 0;"><strong>📅 Dates:</strong><br>${startDateFormatted} - ${endDateFormatted}</p>
        <p style="margin: 10px 0;"><strong>⏱️ Trip Length:</strong><br>${tripLengthDays} days</p>
    `);
}

/**
 * Update progress display
 */
function updateProgressDisplay() {
    const total = tripData.checklist.length;
    const completed = tripData.checklist.filter(i => i.completed).length;
    const percentage = total > 0 ? Math.round((completed / total) * 100) : 0;

    $('#progress-percentage').text(percentage + '%');
    $('#completed-count').text(completed);
    $('#total-count').text(total);
}

/**
 * Save data to localStorage
 */
function saveData() {
    try {
        localStorage.setItem('disneyTripData', JSON.stringify(tripData));
        console.log('Trip data saved successfully');
    } catch (e) {
        console.error('Error saving trip data:', e);
        showNotification('Error saving data. Please try again.', 'error');
    }
}

/**
 * Load data from localStorage
 */
function loadData() {
    try {
        const saved = localStorage.getItem('disneyTripData');
        if (saved) {
            tripData = JSON.parse(saved);

            // Populate form fields
            if (tripData.destination) $('#destination').val(tripData.destination);
            if (tripData.partySize) $('#partySize').val(tripData.partySize);
            if (tripData.startDate) $('#startDate').val(tripData.startDate);
            if (tripData.endDate) $('#endDate').val(tripData.endDate);

            console.log('Trip data loaded successfully');
        }
    } catch (e) {
        console.error('Error loading trip data:', e);
    }
}

/**
 * Clear all data
 */
function clearData() {
    if (confirm('Are you sure you want to clear all trip data? This cannot be undone.')) {
        localStorage.removeItem('disneyTripData');
        tripData = {
            destination: '',
            partySize: 4,
            startDate: '',
            endDate: '',
            checklist: [],
            createdAt: null
        };

        // Clear form
        $('#trip-form')[0].reset();

        updateUI();
        showNotification('All trip data has been cleared', 'info');
        scrollToID('#top', 750);
    }
}

/**
 * Show notification message
 */
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = $(`
        <div class="disney-notification" style="
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'success' ? 'linear-gradient(135deg, #8B5FBF 0%, #FFB6C1 100%)' : type === 'error' ? 'linear-gradient(135deg, #ff69b4 0%, #ff1493 100%)' : 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'};
            color: white;
            padding: 20px 30px;
            border-radius: 15px;
            box-shadow: 0 8px 32px rgba(139, 95, 191, 0.3);
            z-index: 9999;
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            max-width: 400px;
            animation: slideInRight 0.3s ease;
        ">
            ${message}
        </div>
    `);

    // Add animation styles
    if (!$('#notification-styles').length) {
        $('head').append(`
            <style id="notification-styles">
                @keyframes slideInRight {
                    from {
                        transform: translateX(400px);
                        opacity: 0;
                    }
                    to {
                        transform: translateX(0);
                        opacity: 1;
                    }
                }
                @keyframes slideOutRight {
                    from {
                        transform: translateX(0);
                        opacity: 1;
                    }
                    to {
                        transform: translateX(400px);
                        opacity: 0;
                    }
                }
            </style>
        `);
    }

    $('body').append(notification);

    // Auto-remove after 4 seconds
    setTimeout(() => {
        notification.css('animation', 'slideOutRight 0.3s ease');
        setTimeout(() => notification.remove(), 300);
    }, 4000);
}

/**
 * Generate unique ID
 */
function generateId() {
    return 'item_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
}

/**
 * Scroll to element (used by multiple functions)
 */
function scrollToID(id, speed) {
    var offSet = 0;
    var targetOffset = $(id).offset().top - offSet;
    $('html,body').animate({scrollTop:targetOffset}, speed);
}
