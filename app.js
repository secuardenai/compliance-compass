// ComplianceCompass App Logic

let complianceData = [];

fetch('app-data.json')
    .then(response => response.json())
    .then(data => {
        complianceData = data;
        currentData = [...complianceData];
        initializeStats();
        populateFilters();
        renderResults();
    })
    .catch(error => {
        console.error('Error loading data:', error);
        // Fall back to sample data if needed
    });

// Application state
let currentData = [...complianceData];
let currentFilters = {
    search: '',
    standard: '',
    category: ''
};

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    initializeStats();
    populateFilters();
    renderResults();
    attachEventListeners();
});

// Initialize statistics
function initializeStats() {
    const controlCount = document.getElementById('controlCount');
    const mappingCount = document.getElementById('mappingCount');
    
    if (controlCount) {
        animateNumber(controlCount, complianceData.length);
    }
    
    if (mappingCount) {
        // Count unique cross-standard mappings
        const totalMappings = complianceData.reduce((sum, item) => {
            const mappingKeys = Object.keys(item.mappings || {});
            const mappingValues = mappingKeys.reduce((count, key) => {
                return count + (item.mappings[key]?.length || 0);
            }, 0);
            return sum + mappingValues;
        }, 0);
        animateNumber(mappingCount, totalMappings);
    }
}

// Animate number counting
function animateNumber(element, target) {
    let current = 0;
    const increment = target / 50;
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            element.textContent = target;
            clearInterval(timer);
        } else {
            element.textContent = Math.floor(current);
        }
    }, 30);
}

// Populate filter dropdowns
function populateFilters() {
    const categoryFilter = document.getElementById('categoryFilter');
    if (!categoryFilter) return;
    
    // Get unique categories
    const categories = [...new Set(complianceData.map(item => item.category))].sort();
    
    categories.forEach(category => {
        const option = document.createElement('option');
        option.value = category;
        option.textContent = category;
        categoryFilter.appendChild(option);
    });
}

// Render results
function renderResults() {
    const container = document.getElementById('resultsContainer');
    const resultCount = document.getElementById('resultCount');
    
    if (!container) return;
    
    // Apply filters
    currentData = complianceData.filter(item => {
        const searchMatch = !currentFilters.search || 
            item.title.toLowerCase().includes(currentFilters.search.toLowerCase()) ||
            item.description.toLowerCase().includes(currentFilters.search.toLowerCase()) ||
            item.id.toLowerCase().includes(currentFilters.search.toLowerCase());
        
        const standardMatch = !currentFilters.standard || 
            item.standard === currentFilters.standard;
        
        const categoryMatch = !currentFilters.category || 
            item.category === currentFilters.category;
        
        return searchMatch && standardMatch && categoryMatch;
    });
    
    // Update count
    if (resultCount) {
        resultCount.textContent = currentData.length;
    }
    
    // Render cards
    if (currentData.length === 0) {
        container.innerHTML = `
            <div class="loading">
                No controls found matching your criteria.
                <br>Try adjusting your filters.
            </div>
        `;
        return;
    }
    
    container.innerHTML = currentData.map(item => createControlCard(item)).join('');
}

// Create control card HTML
function createControlCard(item) {
    const badges = [];
    badges.push(`<span class="badge badge-${item.standard.toLowerCase()}">${item.standard}</span>`);
    
    // Add mapping badges
    if (item.mappings) {
        Object.keys(item.mappings).forEach(key => {
            const standardName = key.toUpperCase().replace('27001', '27001');
            if (item.mappings[key].length > 0) {
                badges.push(`<span class="badge badge-${key}">${standardName}</span>`);
            }
        });
    }
    
    const mappingRows = item.mappings ? Object.entries(item.mappings)
        .filter(([key, values]) => values && values.length > 0)
        .map(([key, values]) => {
            const label = key.toUpperCase().replace('27001', '27001');
            return `
                <div class="mapping-row">
                    <div class="mapping-label">${label}</div>
                    <div class="mapping-value">${values.join(', ')}</div>
                </div>
            `;
        }).join('') : '';
    
    return `
        <div class="control-card">
            <div class="control-header">
                <div class="control-id">${item.id}</div>
                <div class="control-badges">
                    ${badges.join('')}
                </div>
            </div>
            <h3 class="control-title">${item.title}</h3>
            <p class="control-description">${item.description}</p>
            ${mappingRows ? `
                <div class="control-mappings">
                    <strong style="color: var(--text-muted); font-size: 0.9rem; display: block; margin-bottom: 0.75rem;">Cross-Standard Mappings:</strong>
                    ${mappingRows}
                </div>
            ` : ''}
            ${item.recommendation ? `
                <details style="margin-top: 1rem; padding: 1rem; background: var(--bg-elevated); border-radius: 8px;">
                    <summary style="cursor: pointer; color: var(--accent-primary); font-weight: 600;">
                        Implementation Recommendations
                    </summary>
                    <p style="margin-top: 1rem; color: var(--text-secondary); line-height: 1.7;">
                        ${item.recommendation}
                    </p>
                </details>
            ` : ''}
        </div>
    `;
}

// Attach event listeners
function attachEventListeners() {
    // Search input
    const searchInput = document.getElementById('searchInput');
    const clearSearch = document.getElementById('clearSearch');
    
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            currentFilters.search = e.target.value;
            renderResults();
            
            if (clearSearch) {
                clearSearch.style.display = e.target.value ? 'block' : 'none';
            }
        });
    }
    
    if (clearSearch) {
        clearSearch.addEventListener('click', () => {
            if (searchInput) {
                searchInput.value = '';
                currentFilters.search = '';
                clearSearch.style.display = 'none';
                renderResults();
            }
        });
    }
    
    // Standard filter
    const standardFilter = document.getElementById('standardFilter');
    if (standardFilter) {
        standardFilter.addEventListener('change', (e) => {
            currentFilters.standard = e.target.value;
            renderResults();
        });
    }
    
    // Category filter
    const categoryFilter = document.getElementById('categoryFilter');
    if (categoryFilter) {
        categoryFilter.addEventListener('change', (e) => {
            currentFilters.category = e.target.value;
            renderResults();
        });
    }
    
    // Export button
    const exportBtn = document.getElementById('exportBtn');
    if (exportBtn) {
        exportBtn.addEventListener('click', exportResults);
    }
    
    // Smooth scroll for navigation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Export results to JSON
function exportResults() {
    const dataStr = JSON.stringify(currentData, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(dataBlob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `compliance-compass-export-${new Date().toISOString().split('T')[0]}.json`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
}

// Add loading fade-in effect
window.addEventListener('load', () => {
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease';
        document.body.style.opacity = '1';
    }, 100);
});
