/**
 * Class 10 MCQ Mastery Portal - Core Application Logic
 * Supports: Sign In / Sign Up, Dashboard Today Tracker, 5 Subjects, 3 Math Modes,
 * Real-time Quiz Evaluation with dynamic explanation display, Calendar History & Reports, Profile.
 */

// Global State
const STATE = {
  currentUser: null,
  activePage: 'dashboard',
  activeSubject: 'Mathematics',
  activeMathMode: 'chapterwise',
  currentQuiz: null,
  selectedCalendarDate: getTodayString(), // YYYY-MM-DD
  calendarMonth: new Date().getMonth(),
  calendarYear: new Date().getFullYear(),
  theme: localStorage.getItem('class10_theme') || 'dark'
};

// ===================================================================
// INITIALIZATION
// ===================================================================
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initAuth();
  initNavigation();
  initDashboard();
  initSubjectAndModes();
  initCalendar();
  initProfile();
});

// Helper: Formatted date string YYYY-MM-DD
function getTodayString() {
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, '0');
  const day = String(now.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

// Format friendly date: "Monday, November 9, 2026"
function formatFriendlyDate(dateStr) {
  const [year, month, day] = dateStr.split('-').map(Number);
  const date = new Date(year, month - 1, day);
  return date.toLocaleDateString('en-US', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });
}

// ===================================================================
// THEME MANAGEMENT
// ===================================================================
function initTheme() {
  if (STATE.theme === 'light') {
    document.body.classList.remove('theme-dark');
    document.body.classList.add('theme-light');
    const toggleIcon = document.querySelector('#themeToggleBtn i');
    if (toggleIcon) toggleIcon.className = 'fa-solid fa-sun';
  }

  const themeBtn = document.getElementById('themeToggleBtn');
  if (themeBtn) {
    themeBtn.addEventListener('click', () => {
      if (document.body.classList.contains('theme-light')) {
        document.body.classList.remove('theme-light');
        document.body.classList.add('theme-dark');
        STATE.theme = 'dark';
        themeBtn.querySelector('i').className = 'fa-solid fa-moon';
      } else {
        document.body.classList.remove('theme-dark');
        document.body.classList.add('theme-light');
        STATE.theme = 'light';
        themeBtn.querySelector('i').className = 'fa-solid fa-sun';
      }
      localStorage.setItem('class10_theme', STATE.theme);
    });
  }
}

// ===================================================================
// AUTHENTICATION & USER MANAGEMENT
// ===================================================================
function initAuth() {
  // Ensure default demo user exists
  let users = getUsers();
  if (users.length === 0) {
    const demoUser = {
      username: 'karpagam',
      password: '123',
      name: 'Karpagam Shan',
      joinedDate: 'November 2026'
    };
    users.push(demoUser);
    saveUsers(users);
  }

  // Check logged in user
  const savedUserJson = localStorage.getItem('class10_currentUser');
  if (savedUserJson) {
    try {
      STATE.currentUser = JSON.parse(savedUserJson);
      updateUserUI();

      // Sync latest records from cloud server for this user
      if (STATE.currentUser && STATE.currentUser.username) {
        fetch(`/api/records?username=${encodeURIComponent(STATE.currentUser.username)}`)
          .then(res => res.json())
          .then(data => {
            if (data.success && Array.isArray(data.records) && data.records.length > 0) {
              localStorage.setItem(getUserRecordsKey(), JSON.stringify(data.records));
              renderDashboardToday();
              renderCalendar();
              renderDayRecords(STATE.selectedCalendarDate);
            }
          })
          .catch(() => {});
      }
    } catch (e) {
      STATE.currentUser = { username: 'student', name: 'Class 10 Student', isGuest: true };
      updateUserUI();
    }
  } else {
    // Default active student session so attended quizzes are always saved immediately!
    STATE.currentUser = { username: 'student', name: 'Class 10 Student', isGuest: true };
    localStorage.setItem('class10_currentUser', JSON.stringify(STATE.currentUser));
    updateUserUI();
  }

  // Setup Form Handlers
  const signInForm = document.getElementById('signInForm');
  if (signInForm) {
    signInForm.addEventListener('submit', (e) => {
      e.preventDefault();
      handleSignIn();
    });
  }

  const signUpForm = document.getElementById('signUpForm');
  if (signUpForm) {
    signUpForm.addEventListener('submit', (e) => {
      e.preventDefault();
      handleSignUp();
    });
  }

  // Quick Demo Login
  const btnQuickDemo = document.getElementById('btnQuickDemo');
  if (btnQuickDemo) {
    btnQuickDemo.addEventListener('click', async () => {
      document.getElementById('loginUsername').value = 'karpagam';
      document.getElementById('loginPassword').value = 'password123';
      handleSignIn();
    });
  }

  // Logout buttons
  const navLogoutBtn = document.getElementById('navLogoutBtn');
  if (navLogoutBtn) {
    navLogoutBtn.addEventListener('click', handleLogout);
  }

  const btnProfileSignOut = document.getElementById('btnProfileSignOut');
  if (btnProfileSignOut) {
    btnProfileSignOut.addEventListener('click', handleLogout);
  }
}

function getUsers() {
  try {
    return JSON.parse(localStorage.getItem('class10_users')) || [];
  } catch (e) {
    return [];
  }
}

function saveUsers(users) {
  localStorage.setItem('class10_users', JSON.stringify(users));
}

// SIGN IN (Cross-device cloud authentication)
async function handleSignIn() {
  const username = document.getElementById('loginUsername').value.trim().toLowerCase();
  const password = document.getElementById('loginPassword').value.trim();

  if (!username || !password) {
    setAuthAlert('Please enter both username and password.', 'error');
    return;
  }

  // Show loading indicator on submit button
  const submitBtn = document.querySelector('#signInForm button[type="submit"]');
  const originalHtml = submitBtn ? submitBtn.innerHTML : '';
  if (submitBtn) {
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Signing in...';
  }

  try {
    const res = await fetch('/api/auth/signin', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
    const data = await res.json();

    if (data.success && data.user) {
      STATE.currentUser = data.user;
      localStorage.setItem('class10_currentUser', JSON.stringify(data.user));

      // Synchronize all quiz records for this user across all devices!
      if (Array.isArray(data.records)) {
        localStorage.setItem(getUserRecordsKey(), JSON.stringify(data.records));
      }

      hideAuthModal();
      updateUserUI();
      showToast(`Welcome back, ${data.user.name}!`, 'success');
      refreshAllViews();
      return;
    } else {
      setAuthAlert(data.message || 'Invalid username or password.', 'error');
      return;
    }
  } catch (err) {
    console.warn('Server offline, checking local storage:', err);
    // Offline fallback
    const users = getUsers();
    const found = users.find(u => u.username.toLowerCase() === username && u.password === password);
    if (found) {
      STATE.currentUser = found;
      localStorage.setItem('class10_currentUser', JSON.stringify(found));
      hideAuthModal();
      updateUserUI();
      showToast(`Welcome back, ${found.name}!`, 'success');
      refreshAllViews();
    } else {
      setAuthAlert('Invalid username or password. Please try again.', 'error');
    }
  } finally {
    if (submitBtn) {
      submitBtn.disabled = false;
      submitBtn.innerHTML = originalHtml;
    }
  }
}

// SIGN UP (Cross-device cloud account creation)
async function handleSignUp() {
  const name = document.getElementById('signupName').value.trim();
  const username = document.getElementById('signupUsername').value.trim().toLowerCase();
  const password = document.getElementById('signupPassword').value.trim();

  if (!name || !username || !password) {
    setAuthAlert('Please fill in all fields.', 'error');
    return;
  }

  if (password.length < 3) {
    setAuthAlert('Password must be at least 3 characters.', 'error');
    return;
  }

  const submitBtn = document.querySelector('#signUpForm button[type="submit"]');
  const originalHtml = submitBtn ? submitBtn.innerHTML : '';
  if (submitBtn) {
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Creating Account...';
  }

  try {
    const res = await fetch('/api/auth/signup', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password, name })
    });
    const data = await res.json();

    if (data.success && data.user) {
      STATE.currentUser = data.user;
      localStorage.setItem('class10_currentUser', JSON.stringify(data.user));

      hideAuthModal();
      updateUserUI();
      showToast(`Account created successfully! Welcome, ${data.user.name}.`, 'success');
      refreshAllViews();
      return;
    } else {
      setAuthAlert(data.message || 'Unable to create account.', 'error');
      return;
    }
  } catch (err) {
    console.warn('Server offline, saving locally:', err);
    const users = getUsers();
    if (users.some(u => u.username.toLowerCase() === username)) {
      setAuthAlert('Username already taken. Please choose another username.', 'error');
      return;
    }
    const newUser = {
      username,
      password,
      name,
      joinedDate: new Date().toLocaleDateString('en-US', { month: 'long', year: 'numeric' })
    };
    users.push(newUser);
    saveUsers(users);

    STATE.currentUser = newUser;
    localStorage.setItem('class10_currentUser', JSON.stringify(newUser));
    hideAuthModal();
    updateUserUI();
    showToast(`Account created successfully! Welcome, ${newUser.name}.`, 'success');
    refreshAllViews();
  } finally {
    if (submitBtn) {
      submitBtn.disabled = false;
      submitBtn.innerHTML = originalHtml;
    }
  }
}

function handleLogout() {
  localStorage.removeItem('class10_currentUser');
  STATE.currentUser = null;
  showAuthModal('signin');
  showToast('You have been signed out.', 'info');
}

function showAuthModal(tab = 'signin') {
  switchAuthTab(tab);
  document.getElementById('authModal').classList.remove('hidden');
}

function hideAuthModal() {
  document.getElementById('authModal').classList.add('hidden');
  clearAuthAlert();
}

function switchAuthTab(tab) {
  clearAuthAlert();
  const tabSignIn = document.getElementById('tabBtnSignIn');
  const tabSignUp = document.getElementById('tabBtnSignUp');
  const formSignIn = document.getElementById('signInForm');
  const formSignUp = document.getElementById('signUpForm');

  if (tab === 'signin') {
    tabSignIn.classList.add('active');
    tabSignUp.classList.remove('active');
    formSignIn.classList.remove('hidden');
    formSignIn.classList.add('active');
    formSignUp.classList.add('hidden');
  } else {
    tabSignUp.classList.add('active');
    tabSignIn.classList.remove('active');
    formSignUp.classList.remove('hidden');
    formSignUp.classList.add('active');
    formSignIn.classList.add('hidden');
  }
}

function setAuthAlert(msg, type = 'error') {
  const alertEl = document.getElementById('authAlert');
  alertEl.textContent = msg;
  alertEl.className = `auth-alert ${type}`;
  alertEl.classList.remove('hidden');
}

function clearAuthAlert() {
  const alertEl = document.getElementById('authAlert');
  alertEl.classList.add('hidden');
  alertEl.textContent = '';
}

function togglePasswordVisibility(inputId, btn) {
  const input = document.getElementById(inputId);
  if (!input) return;
  if (input.type === 'password') {
    input.type = 'text';
    btn.innerHTML = '<i class="fa-solid fa-eye-slash"></i>';
  } else {
    input.type = 'password';
    btn.innerHTML = '<i class="fa-solid fa-eye"></i>';
  }
}

function updateUserUI() {
  if (!STATE.currentUser) return;
  const initial = STATE.currentUser.name.charAt(0).toUpperCase();

  const navUserAvatar = document.getElementById('navUserAvatar');
  const navUserName = document.getElementById('navUserName');
  const dashUserName = document.getElementById('dashUserName');
  const profileAvatar = document.getElementById('profileAvatar');
  const profileDisplayName = document.getElementById('profileDisplayName');
  const profileDisplayUsername = document.getElementById('profileDisplayUsername');
  const editFullName = document.getElementById('editFullName');
  const editUsername = document.getElementById('editUsername');

  if (navUserAvatar) navUserAvatar.textContent = initial;
  if (navUserName) navUserName.textContent = STATE.currentUser.name.split(' ')[0];
  if (dashUserName) dashUserName.textContent = STATE.currentUser.name;
  if (profileAvatar) profileAvatar.textContent = initial;
  if (profileDisplayName) profileDisplayName.textContent = STATE.currentUser.name;
  if (profileDisplayUsername) profileDisplayUsername.textContent = `@${STATE.currentUser.username}`;
  if (editFullName) editFullName.value = STATE.currentUser.name;
  if (editUsername) editUsername.value = STATE.currentUser.username;
}

// ===================================================================
// NAVIGATION & PAGE ROUTING
// ===================================================================
function initNavigation() {
  const navTabs = document.querySelectorAll('.nav-tab');
  navTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const targetPage = tab.getAttribute('data-page');
      navigateToPage(targetPage);
    });
  });

  // Hero Quick Buttons
  const btnDashStartQuiz = document.getElementById('btnDashStartQuiz');
  if (btnDashStartQuiz) {
    btnDashStartQuiz.addEventListener('click', () => navigateToPage('quizzes'));
  }

  const btnDashViewHistory = document.getElementById('btnDashViewHistory');
  if (btnDashViewHistory) {
    btnDashViewHistory.addEventListener('click', () => navigateToPage('records'));
  }

  const btnDashViewAllRecords = document.getElementById('btnDashViewAllRecords');
  if (btnDashViewAllRecords) {
    btnDashViewAllRecords.addEventListener('click', () => navigateToPage('records'));
  }
}

function navigateToPage(pageId) {
  STATE.activePage = pageId;

  // Update nav tabs
  document.querySelectorAll('.nav-tab').forEach(tab => {
    if (tab.getAttribute('data-page') === pageId) {
      tab.classList.add('active');
    } else {
      tab.classList.remove('active');
    }
  });

  // Update page views
  document.querySelectorAll('.page-view').forEach(view => {
    view.classList.remove('active');
  });

  const targetView = document.getElementById(`page${capitalizeFirstLetter(pageId)}`);
  if (targetView) {
    targetView.classList.add('active');
  }

  // Refresh data for the page
  if (pageId === 'dashboard') {
    renderDashboardToday();
  } else if (pageId === 'records') {
    renderCalendar();
    renderDayRecords(STATE.selectedCalendarDate);
  } else if (pageId === 'profile') {
    renderProfileStats();
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function navigateToQuizzesWithSubject(subjectName) {
  switchSubject(subjectName);
  navigateToPage('quizzes');
}

function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

// ===================================================================
// QUIZ RECORDS STORAGE HELPER (Always saves & syncs across devices)
// ===================================================================
function getUserRecordsKey() {
  const username = (STATE.currentUser && STATE.currentUser.username) ? STATE.currentUser.username : 'student';
  return `class10_records_${username}`;
}

function getAllUserRecords() {
  const userKey = getUserRecordsKey();
  let records = [];
  try {
    records = JSON.parse(localStorage.getItem(userKey)) || [];
  } catch (e) {
    records = [];
  }

  // If user is signed into an account, merge any previous student/guest practice
  if (STATE.currentUser && STATE.currentUser.username && STATE.currentUser.username !== 'student') {
    try {
      const guestKey = 'class10_records_student';
      const guestRecords = JSON.parse(localStorage.getItem(guestKey)) || [];
      if (guestRecords.length > 0) {
        guestRecords.forEach(gr => {
          if (!records.some(r => r.id === gr.id)) {
            records.push(gr);
            // Also sync to server for this user
            fetch('/api/records', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ username: STATE.currentUser.username, record: gr })
            }).catch(() => {});
          }
        });
        localStorage.setItem(userKey, JSON.stringify(records));
        localStorage.removeItem(guestKey);
      }
    } catch (e) {}
  }

  return records;
}

function saveQuizRecord(record) {
  const records = getAllUserRecords();
  records.unshift(record); // newest first
  localStorage.setItem(getUserRecordsKey(), JSON.stringify(records));

  // Sync to cloud backend across all devices
  if (STATE.currentUser && STATE.currentUser.username) {
    fetch('/api/records', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: STATE.currentUser.username,
        record: record
      })
    }).catch(err => console.warn('Record stored locally, cloud sync pending:', err));
  }
}

// Helper to save attended session when exiting or ending quiz
function saveAttendedQuizSession(quiz) {
  if (!quiz || !quiz.userAnswers || quiz.userAnswers.length === 0) return;

  const total = quiz.userAnswers.length;
  const score = quiz.score;
  const percentage = Math.round((score / total) * 100);
  const now = new Date();
  const timeFormatted = now.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit', hour12: true });

  const record = {
    id: quiz.id || ('quiz_' + Date.now()),
    subject: quiz.subject || 'Mathematics',
    mode: quiz.mode || 'chapterwise',
    modeName: quiz.modeName || 'Practice',
    chapterNumbers: quiz.chapterNumbers || [1],
    chapterDisplayName: quiz.chapterDisplayName || 'Class 10 Practice',
    date: getTodayString(),
    time: timeFormatted,
    score: score,
    totalQuestions: total,
    percentage: percentage,
    answers: quiz.userAnswers
  };

  saveQuizRecord(record);
  showToast(`Attended quiz saved (${score}/${total})!`, 'success');
}

// ===================================================================
// 1. DASHBOARD: TODAY'S ACTIVITY TRACKER
// ===================================================================
function initDashboard() {
  const dateEl = document.getElementById('dashCurrentDate');
  if (dateEl) {
    dateEl.textContent = formatFriendlyDate(getTodayString());
  }
  renderDashboardToday();
}

function renderDashboardToday() {
  if (!STATE.currentUser) return;

  const todayStr = getTodayString();
  const allRecords = getAllUserRecords();
  const todayRecords = allRecords.filter(r => r.date === todayStr);

  // Update Counters
  const countEl = document.getElementById('dashTodayQuizzesCount');
  const accEl = document.getElementById('dashTodayAccuracy');
  const qSolvedEl = document.getElementById('dashTodayQuestionsSolved');
  const allTimeEl = document.getElementById('dashTotalPracticedAllTime');
  const badgeCountEl = document.getElementById('dashTodayBadgeCount');

  const totalQuizzesToday = todayRecords.length;
  let totalScoreToday = 0;
  let totalMaxScoreToday = 0;
  let totalQuestionsToday = 0;

  todayRecords.forEach(r => {
    totalScoreToday += r.score;
    totalMaxScoreToday += r.totalQuestions;
    totalQuestionsToday += r.totalQuestions;
  });

  const avgAccuracy = totalMaxScoreToday > 0 ? Math.round((totalScoreToday / totalMaxScoreToday) * 100) : 0;

  if (countEl) countEl.textContent = totalQuizzesToday;
  if (accEl) accEl.textContent = totalQuizzesToday > 0 ? `${avgAccuracy}%` : '0%';
  if (qSolvedEl) qSolvedEl.textContent = totalQuestionsToday;
  if (allTimeEl) allTimeEl.textContent = allRecords.length;
  if (badgeCountEl) badgeCountEl.textContent = `${totalQuizzesToday} Completed`;

  // Render List of Today's Quizzes
  const listContainer = document.getElementById('dashTodayQuizList');
  if (!listContainer) return;

  if (todayRecords.length === 0) {
    listContainer.innerHTML = `
      <div class="empty-state">
        <div class="empty-icon"><i class="fa-solid fa-calendar-xmark"></i></div>
        <h3>No Quizzes Practiced Today Yet</h3>
        <p>You haven't taken any quizzes today (${formatFriendlyDate(todayStr)}). Start practicing chapter-wise mathematics questions now!</p>
        <button class="btn-primary" onclick="navigateToPage('quizzes')">
          <i class="fa-solid fa-play"></i> Start Today's First Quiz
        </button>
      </div>
    `;
    return;
  }

  let html = '';
  todayRecords.forEach(record => {
    const badgeClass = getBadgeClass(record.percentage);
    html += `
      <div class="quiz-record-item">
        <div class="record-main-info">
          <div class="record-score-badge ${badgeClass}">
            <span class="score-val">${record.score}/${record.totalQuestions}</span>
            <span class="score-pct">${record.percentage}%</span>
          </div>
          <div class="record-details">
            <h4 class="record-title">${record.chapterDisplayName}</h4>
            <div class="record-meta-line">
              <span class="meta-pill"><i class="fa-solid fa-calculator"></i> ${record.subject}</span>
              <span class="meta-pill"><i class="fa-solid fa-sliders"></i> ${record.modeName}</span>
              <span><i class="fa-solid fa-clock"></i> ${record.time}</span>
            </div>
          </div>
        </div>
        <div class="record-actions">
          <button class="btn-secondary-sm" onclick="openReportModalById('${record.id}')">
            <i class="fa-solid fa-eye"></i> View Report
          </button>
        </div>
      </div>
    `;
  });

  listContainer.innerHTML = html;
}

function getBadgeClass(pct) {
  if (pct >= 85) return 'badge-excellent';
  if (pct >= 65) return 'badge-good';
  if (pct >= 50) return 'badge-average';
  return 'badge-practice';
}

// ===================================================================
// 2. QUIZZES PAGE: 5 SUBJECTS & 3 MATHEMATICS MODES
// ===================================================================
function initSubjectAndModes() {
  // 5 Subject Buttons
  const subjectBtns = document.querySelectorAll('#subjectButtonsGroup .subject-btn');
  subjectBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const subject = btn.getAttribute('data-subject');
      switchSubject(subject);
    });
  });

  // 3 Mode Buttons (Chapter-wise, All Chapters, Selected Chapters)
  const modeBtns = document.querySelectorAll('.modes-btn-group .mode-btn');
  modeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const mode = btn.getAttribute('data-mode');
      switchMathMode(mode);
    });
  });

  // Render Chapters Grid
  renderChaptersGrid();
  renderSelectedChaptersCheckboxes();

  // Mode 2: All chapters start button
  const btnStartAllChaptersQuiz = document.getElementById('btnStartAllChaptersQuiz');
  if (btnStartAllChaptersQuiz) {
    btnStartAllChaptersQuiz.addEventListener('click', startAllChaptersQuiz);
  }

  // Mode 3: Selected chapters start button & tools
  const btnStartSelectedChaptersQuiz = document.getElementById('btnStartSelectedChaptersQuiz');
  if (btnStartSelectedChaptersQuiz) {
    btnStartSelectedChaptersQuiz.addEventListener('click', startSelectedChaptersQuiz);
  }

  const btnSelectAllChapters = document.getElementById('btnSelectAllChapters');
  if (btnSelectAllChapters) {
    btnSelectAllChapters.addEventListener('click', () => {
      document.querySelectorAll('#chapterCheckboxList input[type="checkbox"]').forEach(cb => {
        cb.checked = true;
        cb.closest('.chapter-checkbox-item').classList.add('checked');
      });
      updateSelectedChaptersCount();
    });
  }

  const btnClearSelectedChapters = document.getElementById('btnClearSelectedChapters');
  if (btnClearSelectedChapters) {
    btnClearSelectedChapters.addEventListener('click', () => {
      document.querySelectorAll('#chapterCheckboxList input[type="checkbox"]').forEach(cb => {
        cb.checked = false;
        cb.closest('.chapter-checkbox-item').classList.remove('checked');
      });
      updateSelectedChaptersCount();
    });
  }
}

function switchSubject(subject) {
  STATE.activeSubject = subject;

  // Update tabs
  document.querySelectorAll('#subjectButtonsGroup .subject-btn').forEach(btn => {
    if (btn.getAttribute('data-subject') === subject) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  const mathSection = document.getElementById('mathQuizSection');
  const csSection = document.getElementById('subjectComingSoonView');
  const csTitle = document.getElementById('csSubjectTitle');

  if (subject === 'Mathematics') {
    mathSection.style.display = 'block';
    csSection.classList.add('hidden');
  } else {
    mathSection.style.display = 'none';
    csSection.classList.remove('hidden');
    csTitle.textContent = `${subject} Questions Coming Soon!`;
  }
}

function switchMathMode(mode) {
  STATE.activeMathMode = mode;

  // Update mode buttons
  document.querySelectorAll('.modes-btn-group .mode-btn').forEach(btn => {
    if (btn.getAttribute('data-mode') === mode) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  // Switch view containers
  const v1 = document.getElementById('viewChapterwise');
  const v2 = document.getElementById('viewAllChapters');
  const v3 = document.getElementById('viewSelectedChapters');

  v1.classList.add('hidden');
  v2.classList.add('hidden');
  v3.classList.add('hidden');

  if (mode === 'chapterwise') {
    v1.classList.remove('hidden');
  } else if (mode === 'allchapters') {
    v2.classList.remove('hidden');
  } else if (mode === 'selectedchapters') {
    v3.classList.remove('hidden');
  }
}

// Render the 8 chapters cards (Mode 1)
function renderChaptersGrid() {
  const container = document.getElementById('chaptersGrid');
  if (!container || !window.MATHS_CHAPTERS) return;

  let html = '';
  window.MATHS_CHAPTERS.forEach(ch => {
    html += `
      <div class="chapter-card" style="--card-accent: ${ch.color}">
        <div class="chapter-card-top">
          <span class="ch-number-badge">Chapter ${ch.chapterNumber}</span>
          <span class="ch-q-count"><i class="fa-solid fa-list-check"></i> ${ch.questions.length} MCQs</span>
        </div>
        <h4>Chapter ${ch.chapterNumber}: ${ch.chapterName}</h4>
        <p>${ch.description}</p>
        <button class="btn-take-quiz" onclick="startSingleChapterQuiz(${ch.chapterNumber})">
          <i class="fa-solid fa-play"></i> Take Chapter Quiz
        </button>
      </div>
    `;
  });

  container.innerHTML = html;
}

// Render Checkboxes for Mode 3 (Selected Chapters)
function renderSelectedChaptersCheckboxes() {
  const container = document.getElementById('chapterCheckboxList');
  if (!container || !window.MATHS_CHAPTERS) return;

  let html = '';
  window.MATHS_CHAPTERS.forEach(ch => {
    html += `
      <label class="chapter-checkbox-item" data-chapter="${ch.chapterNumber}">
        <input type="checkbox" value="${ch.chapterNumber}" onchange="onChapterCheckboxChange(this)">
        <div class="ch-cb-details">
          <span class="ch-cb-tag">Chapter ${ch.chapterNumber}</span>
          <span class="ch-cb-title">${ch.chapterName}</span>
          <span class="ch-cb-count">${ch.questions.length} Questions</span>
        </div>
      </label>
    `;
  });

  container.innerHTML = html;
}

function onChapterCheckboxChange(checkbox) {
  const item = checkbox.closest('.chapter-checkbox-item');
  if (checkbox.checked) {
    item.classList.add('checked');
  } else {
    item.classList.remove('checked');
  }
  updateSelectedChaptersCount();
}

function updateSelectedChaptersCount() {
  const checked = document.querySelectorAll('#chapterCheckboxList input[type="checkbox"]:checked');
  const countText = document.getElementById('selectedChaptersCountText');
  const startBtn = document.getElementById('btnStartSelectedChaptersQuiz');

  const count = checked.length;
  countText.textContent = `${count} chapter${count === 1 ? '' : 's'} selected`;
  startBtn.disabled = count === 0;
}

// ===================================================================
// QUIZ GAMEPLAY ENGINE
// ===================================================================
// Start Chapter-wise Quiz (Questions shuffled in random order)
function startSingleChapterQuiz(chapterNum) {
  const chapter = window.MATHS_CHAPTERS.find(c => c.chapterNumber === chapterNum);
  if (!chapter) return;

  const quizSession = {
    id: 'quiz_' + Date.now(),
    subject: 'Mathematics',
    mode: 'chapterwise',
    modeName: 'Chapter-wise',
    chapterNumbers: [chapter.chapterNumber],
    chapterDisplayName: `Chapter ${chapter.chapterNumber}: ${chapter.chapterName}`,
    questions: shuffleArray(JSON.parse(JSON.stringify(chapter.questions))), // RANDOM ORDER!
    currentIndex: 0,
    userAnswers: [], // { questionId, selectedOption, isCorrect }
    score: 0,
    startTime: new Date()
  };

  launchQuizModal(quizSession);
}

// Start All Chapters Quiz (Questions shuffled in random order)
function startAllChaptersQuiz() {
  const lengthRadio = document.querySelector('input[name="allChCount"]:checked');
  const countVal = lengthRadio ? lengthRadio.value : '15';

  // Pool all questions from all 8 chapters
  let allQuestions = [];
  window.MATHS_CHAPTERS.forEach(ch => {
    allQuestions.push(...ch.questions);
  });

  // Shuffle questions randomly
  allQuestions = shuffleArray(allQuestions);

  let selectedQuestions = allQuestions;
  if (countVal !== 'all') {
    const limit = parseInt(countVal, 10);
    selectedQuestions = allQuestions.slice(0, limit);
  }

  const quizSession = {
    id: 'quiz_' + Date.now(),
    subject: 'Mathematics',
    mode: 'allchapters',
    modeName: 'All Chapters',
    chapterNumbers: [1, 2, 3, 4, 5, 6, 7, 8],
    chapterDisplayName: 'All 8 Chapters Comprehensive Quiz',
    questions: shuffleArray(JSON.parse(JSON.stringify(selectedQuestions))), // RANDOM ORDER!
    currentIndex: 0,
    userAnswers: [],
    score: 0,
    startTime: new Date()
  };

  launchQuizModal(quizSession);
}

// Start Selected Chapters Quiz (Questions shuffled in random order)
function startSelectedChaptersQuiz() {
  const checkedBoxes = document.querySelectorAll('#chapterCheckboxList input[type="checkbox"]:checked');
  if (checkedBoxes.length === 0) return;

  const selectedChNums = Array.from(checkedBoxes).map(cb => parseInt(cb.value, 10));
  const selectedChapters = window.MATHS_CHAPTERS.filter(c => selectedChNums.includes(c.chapterNumber));

  let pooledQuestions = [];
  selectedChapters.forEach(c => {
    pooledQuestions.push(...c.questions);
  });

  pooledQuestions = shuffleArray(pooledQuestions);

  const chapterNamesList = selectedChapters.map(c => `Ch ${c.chapterNumber}`).join(', ');

  const quizSession = {
    id: 'quiz_' + Date.now(),
    subject: 'Mathematics',
    mode: 'selectedchapters',
    modeName: 'Selected Chapters',
    chapterNumbers: selectedChNums,
    chapterDisplayName: `Selected Chapters (${chapterNamesList})`,
    questions: shuffleArray(JSON.parse(JSON.stringify(pooledQuestions))), // RANDOM ORDER!
    currentIndex: 0,
    userAnswers: [],
    score: 0,
    startTime: new Date()
  };

  launchQuizModal(quizSession);
}

function shuffleArray(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

// Launch Quiz Modal
function launchQuizModal(quizSession) {
  STATE.currentQuiz = quizSession;
  STATE.currentQuiz.selectedOption = null;
  STATE.currentQuiz.isAnswerSubmitted = false;

  const modal = document.getElementById('quizModal');
  modal.classList.remove('hidden');

  // Setup Exit Quiz confirmation: Saves attended questions!
  const btnExit = document.getElementById('btnExitQuiz');
  btnExit.onclick = () => {
    const answeredCount = quizSession.userAnswers.length;
    if (answeredCount > 0) {
      if (confirm(`Do you want to save your progress and exit? You have answered ${answeredCount} question(s).`)) {
        saveAttendedQuizSession(quizSession);
        modal.classList.add('hidden');
        STATE.currentQuiz = null;
        renderDashboardToday();
        renderCalendar();
        renderDayRecords(STATE.selectedCalendarDate);
        renderProfileStats();
      }
    } else {
      modal.classList.add('hidden');
      STATE.currentQuiz = null;
    }
  };

  // Primary action button (dynamically morphs between Submit -> Next Question -> Finish Quiz)
  const btnAction = document.getElementById('btnSubmitAnswer');
  if (btnAction) {
    btnAction.onclick = handleSubmitCurrentAnswer;
  }

  renderCurrentQuestion();
}

// ===================================================================
// MATHEMATICAL FORMATTING HELPER (Stacked Fractions & Sqrt with Vinculum Overbar)
// ===================================================================
function formatMathText(str) {
  if (!str) return '';
  if (typeof str !== 'string') return String(str);

  // 1. Format square roots: extend vinculum bar over all variables inside it
  if (str.includes('√')) {
    // Case A: √(expr) e.g. √(1 + x²) -> overbar over all variables inside
    str = str.replace(/√\(([^)]+)\)/g, (match, inner) => {
      return `<span class="math-sqrt"><svg class="sqrt-surd" viewBox="0 0 12 24" preserveAspectRatio="none"><path d="M1 14.5 L3.5 13 L6.5 22.5 L12 1.5" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="miter"/></svg><span class="sqrt-radicand">${inner.trim()}</span></span>`;
    });
    // Case B: √token e.g. √3, √2
    str = str.replace(/√([0-9a-zA-Z²³⁴⁵⁶⁷⁸⁹¹⁰θπ]+)/g, (match, inner) => {
      return `<span class="math-sqrt"><svg class="sqrt-surd" viewBox="0 0 12 24" preserveAspectRatio="none"><path d="M1 14.5 L3.5 13 L6.5 22.5 L12 1.5" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="miter"/></svg><span class="sqrt-radicand">${inner.trim()}</span></span>`;
    });
  }

  // 2. Format fractions if not already formatted with .math-fraction
  if (!str.includes('math-fraction')) {
    str = str.replace(/([A-Za-z0-9_²³⁴⁵⁶⁷⁸⁹¹⁰θπ√|\+\-]+)\s*\/\s*([A-Za-z0-9_²³⁴⁵⁶⁷⁸⁹¹⁰θπ√|\+\-]+)/g, (match, num, den) => {
      return `<span class="math-fraction"><span class="math-numerator">${num.trim()}</span><span class="math-denominator">${den.trim()}</span></span>`;
    });
  }

  return str;
}

// Render the active question
function renderCurrentQuestion() {
  const quiz = STATE.currentQuiz;
  if (!quiz) return;

  const qIndex = quiz.currentIndex;
  const currentQ = quiz.questions[qIndex];
  const totalQ = quiz.questions.length;

  // Reset per-question state: No option chosen yet, not submitted yet
  quiz.selectedOption = null;
  quiz.isAnswerSubmitted = false;

  // Header tags (mentioning chapter number and name!)
  document.getElementById('activeQuizChapterTag').textContent = `Chapter ${currentQ.chapterNumber}: ${currentQ.chapterName}`;
  document.getElementById('quizQuestionCounter').textContent = `Question ${qIndex + 1} of ${totalQ}`;
  document.getElementById('quizActiveModePill').textContent = quiz.modeName;
  // USER REQUIREMENT: "number from 1 and not the nuumbers from the pdf"
  document.getElementById('questionNumberBadge').textContent = `Q${qIndex + 1}`;
  document.getElementById('qChapterNameDisplay').textContent = `Chapter ${currentQ.chapterNumber}: ${currentQ.chapterName}`;

  // Progress Bar
  const pct = Math.round(((qIndex) / totalQ) * 100);
  document.getElementById('quizProgressBar').style.width = `${pct}%`;

  // Question Text: formatted with stacked vertical fractions
  document.getElementById('activeQuestionText').innerHTML = formatMathText(currentQ.question);

  // Question Diagram (if present)
  const diagramContainer = document.getElementById('qDiagramContainer');
  const diagramImg = document.getElementById('qDiagramImage');
  if (currentQ.diagram) {
    diagramImg.src = currentQ.diagram;
    diagramContainer.classList.remove('hidden');
  } else {
    diagramContainer.classList.add('hidden');
    diagramImg.src = '';
  }

  // Options: Clean state, nothing locked, nothing selected
  const optionsContainer = document.getElementById('optionsContainer');
  optionsContainer.innerHTML = '';

  currentQ.options.forEach(opt => {
    const box = document.createElement('div');
    box.className = 'option-box';
    box.setAttribute('data-option-id', opt.id);
    box.innerHTML = `
      <div class="option-letter">${opt.id}</div>
      <div class="option-text">${formatMathText(opt.text)}</div>
      <i class="fa-solid fa-check option-status-icon status-correct"></i>
      <i class="fa-solid fa-xmark option-status-icon status-wrong"></i>
    `;
    box.onclick = () => handleSelectOption(opt.id, box);
    optionsContainer.appendChild(box);
  });

  // USER REQUIREMENT:
  // "submit button should be visible for each question. after submit is clicked, it shows the answer and the buutton changes to next question and for the last question after submit button it changes to finish"
  const btnSubmit = document.getElementById('btnSubmitAnswer');
  btnSubmit.classList.remove('hidden');
  btnSubmit.className = 'btn-primary';
  btnSubmit.innerHTML = '<i class="fa-solid fa-check"></i> Submit Answer';
  btnSubmit.disabled = true;
  btnSubmit.classList.remove('ready-to-submit');
  btnSubmit.onclick = handleSubmitCurrentAnswer;

  // Feedback prompt instructing user to choose an answer
  const feedbackMsg = document.getElementById('quizFeedbackMessage');
  feedbackMsg.innerHTML = '<span class="status-hint"><i class="fa-solid fa-hand-pointer"></i> Select an answer to enable Submit</span>';
  feedbackMsg.className = 'footer-left-status';
}

function handleSelectOption(optionId, boxElement) {
  const quiz = STATE.currentQuiz;
  if (!quiz) return;

  // If answer already submitted for this question, cannot change answer
  if (quiz.isAnswerSubmitted || boxElement.classList.contains('locked')) return;

  // Remove selected from all options
  document.querySelectorAll('.option-box').forEach(b => b.classList.remove('selected'));

  // Mark this option selected
  boxElement.classList.add('selected');
  quiz.selectedOption = optionId;

  // Enable submit button NOW that an answer is selected!
  const btnSubmit = document.getElementById('btnSubmitAnswer');
  btnSubmit.disabled = false;
  btnSubmit.classList.add('ready-to-submit');

  const feedbackMsg = document.getElementById('quizFeedbackMessage');
  feedbackMsg.innerHTML = `<span class="status-ready"><i class="fa-solid fa-circle-check"></i> Option (${optionId}) selected. Ready to Submit!</span>`;
  feedbackMsg.className = 'footer-left-status';
}

/**
 * Answer checking:
 * STRICT RULE 1: Only callable when an option is selected.
 * STRICT RULE 2: Only after submit is clicked can user proceed.
 * STRICT RULE 3: Only after last question is completed can user finish.
 */
function handleSubmitCurrentAnswer() {
  const quiz = STATE.currentQuiz;
  if (!quiz) return;

  // Double check an option was selected
  if (!quiz.selectedOption) {
    showToast('Please choose an answer (A, B, C, or D) before submitting!', 'error');
    return;
  }

  // Prevent multiple submits on the same question
  if (quiz.isAnswerSubmitted) return;
  quiz.isAnswerSubmitted = true;

  const currentQ = quiz.questions[quiz.currentIndex];
  const userChoice = quiz.selectedOption;
  const correctChoice = currentQ.correctAnswer;
  const isCorrect = (userChoice === correctChoice);

  // Lock all options so user cannot change answer after submission
  const optionBoxes = document.querySelectorAll('.option-box');
  optionBoxes.forEach(box => {
    box.classList.add('locked');
    const optId = box.getAttribute('data-option-id');

    if (optId === correctChoice) {
      // Correct answer always gets highlighted in green!
      box.classList.add('correct');
    }

    if (!isCorrect && optId === userChoice) {
      // If wrong, user choice gets highlighted in red!
      box.classList.add('wrong');
    }
  });

  // Record Answer with Diagram
  if (isCorrect) {
    quiz.score += 1;
  }
  quiz.userAnswers.push({
    questionIndex: quiz.currentIndex + 1,
    questionId: currentQ.id,
    questionNumber: quiz.currentIndex + 1,
    originalPdfNumber: currentQ.questionNumber,
    chapterNumber: currentQ.chapterNumber,
    chapterName: currentQ.chapterName,
    question: currentQ.question,
    diagram: currentQ.diagram || null,
    options: currentQ.options,
    selectedOption: userChoice,
    correctAnswer: correctChoice,
    isCorrect: isCorrect
  });

  // Handle Feedback
  const feedbackMsg = document.getElementById('quizFeedbackMessage');
  if (isCorrect) {
    feedbackMsg.innerHTML = '<i class="fa-solid fa-circle-check"></i> Correct Answer! Well done.';
    feedbackMsg.className = 'footer-left-status correct-msg';
  } else {
    feedbackMsg.innerHTML = '<i class="fa-solid fa-circle-xmark"></i> Incorrect Answer.';
    feedbackMsg.className = 'footer-left-status wrong-msg';
  }

  // USER REQUIREMENT:
  // "after submit is clicked, it shows the answer and the buutton changes to next question and for the last question after submit button it changes to finish"
  const isLast = (quiz.currentIndex === quiz.questions.length - 1);
  const btnAction = document.getElementById('btnSubmitAnswer');
  btnAction.disabled = false;
  btnAction.classList.remove('hidden');

  if (isLast) {
    // For the last question, the button changes to Finish Quiz
    btnAction.className = 'btn-success ready-to-submit';
    btnAction.innerHTML = '<i class="fa-solid fa-flag-checkered"></i> Finish Quiz';
    btnAction.onclick = handleFinishQuiz;
  } else {
    // For intermediate questions, the button changes to Next Question
    btnAction.className = 'btn-primary ready-to-submit';
    btnAction.innerHTML = 'Next Question <i class="fa-solid fa-arrow-right"></i>';
    btnAction.onclick = handleNextQuestion;
  }
}

// Strictly allow next question only after current question has been submitted
function handleNextQuestion() {
  const quiz = STATE.currentQuiz;
  if (!quiz) return;

  if (!quiz.isAnswerSubmitted) {
    showToast('Please submit your answer before proceeding to the next question.', 'error');
    return;
  }

  if (quiz.currentIndex < quiz.questions.length - 1) {
    quiz.currentIndex += 1;
    renderCurrentQuestion();
  }
}

// Allow finishing and saving quiz
function handleFinishQuiz() {
  const quiz = STATE.currentQuiz;
  if (!quiz) return;

  // If answer was selected on current question but not submitted yet, submit it now!
  if (quiz.selectedOption && !quiz.isAnswerSubmitted) {
    handleSubmitCurrentAnswer();
  }

  if (!quiz.userAnswers || quiz.userAnswers.length === 0) {
    showToast('Please answer at least one question before finishing the quiz.', 'error');
    return;
  }

  // Complete progress bar
  document.getElementById('quizProgressBar').style.width = '100%';

  // Hide quiz modal
  document.getElementById('quizModal').classList.add('hidden');

  // Calculate results on answered questions
  const total = quiz.userAnswers.length;
  const score = quiz.score;
  const percentage = Math.round((score / total) * 100);

  // Create persistent record
  const now = new Date();
  const timeFormatted = now.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit', hour12: true });

  const record = {
    id: quiz.id,
    subject: quiz.subject,
    mode: quiz.mode,
    modeName: quiz.modeName,
    chapterNumbers: quiz.chapterNumbers,
    chapterDisplayName: quiz.chapterDisplayName,
    date: getTodayString(), // YYYY-MM-DD
    time: timeFormatted,
    score: score,
    totalQuestions: total,
    percentage: percentage,
    answers: quiz.userAnswers
  };

  saveQuizRecord(record);

  // Show Result Celebration Modal
  showQuizResultCelebration(record);

  // Refresh Dashboard & Records
  renderDashboardToday();
  renderCalendar();
  renderDayRecords(STATE.selectedCalendarDate);
  renderProfileStats();

  STATE.currentQuiz = null;
}

// Result Celebration Modal
function showQuizResultCelebration(record) {
  const resultModal = document.getElementById('quizResultModal');
  resultModal.classList.remove('hidden');

  document.getElementById('resultScoreFraction').textContent = `${record.score}/${record.totalQuestions}`;
  document.getElementById('resultPercentage').textContent = `${record.percentage}%`;
  document.getElementById('resultChaptersSummary').textContent = record.chapterDisplayName;
  document.getElementById('resultCorrectCount').textContent = record.score;
  document.getElementById('resultWrongCount').textContent = record.totalQuestions - record.score;

  const gradePill = document.getElementById('resultGradePill');
  const title = document.getElementById('resultTitle');
  const sub = document.getElementById('resultSubtitle');

  if (record.percentage >= 90) {
    gradePill.textContent = '🌟 Outstanding Mastery';
    gradePill.className = 'score-grade-pill badge-excellent';
    title.textContent = 'Spectacular Score!';
    sub.textContent = 'You demonstrated complete mastery over these Class 10 questions.';
  } else if (record.percentage >= 70) {
    gradePill.textContent = '👍 Good Performance';
    gradePill.className = 'score-grade-pill badge-good';
    title.textContent = 'Well Done!';
    sub.textContent = 'Solid preparation. Review the few questions you missed to achieve 100%.';
  } else if (record.percentage >= 50) {
    gradePill.textContent = '📖 Room for Improvement';
    gradePill.className = 'score-grade-pill badge-average';
    title.textContent = 'Good Effort!';
    sub.textContent = 'Check the detailed explanations to clear your concepts and try again.';
  } else {
    gradePill.textContent = '💪 Needs More Practice';
    gradePill.className = 'score-grade-pill badge-practice';
    title.textContent = 'Keep Practicing!';
    sub.textContent = 'Review each question explanation carefully to strengthen your basics.';
  }

  // Result Actions
  document.getElementById('btnResultViewReport').onclick = () => {
    resultModal.classList.add('hidden');
    openDetailedReport(record);
  };

  document.getElementById('btnResultRetake').onclick = () => {
    resultModal.classList.add('hidden');
    if (record.mode === 'chapterwise' && record.chapterNumbers.length === 1) {
      startSingleChapterQuiz(record.chapterNumbers[0]);
    } else {
      navigateToPage('quizzes');
    }
  };

  document.getElementById('btnResultGoDashboard').onclick = () => {
    resultModal.classList.add('hidden');
    navigateToPage('dashboard');
  };
}

// ===================================================================
// 3. RECORDS PAGE: CALENDAR & DETAILED REPORTS
// ===================================================================
function initCalendar() {
  const prevBtn = document.getElementById('calPrevMonth');
  const nextBtn = document.getElementById('calNextMonth');

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      STATE.calendarMonth -= 1;
      if (STATE.calendarMonth < 0) {
        STATE.calendarMonth = 11;
        STATE.calendarYear -= 1;
      }
      renderCalendar();
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      STATE.calendarMonth += 1;
      if (STATE.calendarMonth > 11) {
        STATE.calendarMonth = 0;
        STATE.calendarYear += 1;
      }
      renderCalendar();
    });
  }

  renderCalendar();
  renderDayRecords(STATE.selectedCalendarDate);

  // Setup Report Modal Close
  const btnCloseReportModal = document.getElementById('btnCloseReportModal');
  if (btnCloseReportModal) {
    btnCloseReportModal.onclick = () => {
      document.getElementById('quizReportModal').classList.add('hidden');
    };
  }

  const btnReportCloseBottom = document.getElementById('btnReportCloseBottom');
  if (btnReportCloseBottom) {
    btnReportCloseBottom.onclick = () => {
      document.getElementById('quizReportModal').classList.add('hidden');
    };
  }
}

function renderCalendar() {
  const monthYearHeader = document.getElementById('calendarMonthYear');
  const daysGrid = document.getElementById('calendarDaysGrid');
  if (!monthYearHeader || !daysGrid) return;

  const year = STATE.calendarYear;
  const month = STATE.calendarMonth;

  const dateObj = new Date(year, month, 1);
  monthYearHeader.textContent = dateObj.toLocaleDateString('en-US', { month: 'long', year: 'numeric' });

  // Get active quiz records to place activity dots
  const allRecords = getAllUserRecords();
  const datesWithQuizzes = new Set(allRecords.map(r => r.date));

  const firstDayIndex = new Date(year, month, 1).getDay(); // 0 is Sunday
  const totalDaysInMonth = new Date(year, month + 1, 0).getDate();
  const prevMonthDays = new Date(year, month, 0).getDate();

  const todayStr = getTodayString();
  let daysHtml = '';

  // Previous month trailing days
  for (let x = firstDayIndex; x > 0; x--) {
    const dayNum = prevMonthDays - x + 1;
    daysHtml += `<div class="cal-day other-month">${dayNum}</div>`;
  }

  // Current month days
  for (let i = 1; i <= totalDaysInMonth; i++) {
    const dayStr = `${year}-${String(month + 1).padStart(2, '0')}-${String(i).padStart(2, '0')}`;
    const isToday = (dayStr === todayStr);
    const isSelected = (dayStr === STATE.selectedCalendarDate);
    const hasQuizzes = datesWithQuizzes.has(dayStr);

    let classes = 'cal-day';
    if (isToday) classes += ' today';
    if (isSelected) classes += ' selected';
    if (hasQuizzes) classes += ' has-quizzes';

    daysHtml += `
      <div class="${classes}" data-date="${dayStr}" onclick="handleCalendarDateClick('${dayStr}')">
        <span>${i}</span>
      </div>
    `;
  }

  daysGrid.innerHTML = daysHtml;
}

function handleCalendarDateClick(dateStr) {
  STATE.selectedCalendarDate = dateStr;
  renderCalendar();
  renderDayRecords(dateStr);
}

function renderDayRecords(dateStr) {
  const allRecords = getAllUserRecords();
  const dayRecords = allRecords.filter(r => r.date === dateStr);

  const titleEl = document.getElementById('selectedDateTitle');
  const countBadge = document.getElementById('selectedDateCountBadge');
  const listEl = document.getElementById('selectedDateQuizList');

  if (titleEl) {
    titleEl.textContent = `Quizzes on ${formatFriendlyDate(dateStr)}`;
  }
  if (countBadge) {
    countBadge.textContent = `${dayRecords.length} Quiz${dayRecords.length === 1 ? '' : 'zes'}`;
  }

  if (!listEl) return;

  if (dayRecords.length === 0) {
    listEl.innerHTML = `
      <div class="empty-state">
        <div class="empty-icon"><i class="fa-solid fa-calendar-day"></i></div>
        <h3>No Quizzes on This Date</h3>
        <p>No tests were recorded on ${formatFriendlyDate(dateStr)}. Select a date marked with a green indicator dot or start a quiz!</p>
        <button class="btn-primary" onclick="navigateToPage('quizzes')">
          <i class="fa-solid fa-play"></i> Take a Quiz Now
        </button>
      </div>
    `;
    return;
  }

  let html = '';
  dayRecords.forEach(record => {
    const badgeClass = getBadgeClass(record.percentage);
    html += `
      <div class="quiz-record-item">
        <div class="record-main-info">
          <div class="record-score-badge ${badgeClass}">
            <span class="score-val">${record.score}/${record.totalQuestions}</span>
            <span class="score-pct">${record.percentage}%</span>
          </div>
          <div class="record-details">
            <h4 class="record-title">${record.chapterDisplayName}</h4>
            <div class="record-meta-line">
              <span class="meta-pill"><i class="fa-solid fa-calculator"></i> ${record.subject}</span>
              <span class="meta-pill"><i class="fa-solid fa-sliders"></i> ${record.modeName}</span>
              <span><i class="fa-solid fa-clock"></i> ${record.time}</span>
            </div>
          </div>
        </div>
        <div class="record-actions">
          <button class="btn-primary" onclick="openReportModalById('${record.id}')">
            <i class="fa-solid fa-file-lines"></i> View Detailed Report
          </button>
        </div>
      </div>
    `;
  });

  listEl.innerHTML = html;
}

function openReportModalById(recordId) {
  const allRecords = getAllUserRecords();
  const record = allRecords.find(r => r.id === recordId);
  if (record) {
    openDetailedReport(record);
  }
}

/**
 * USER REQUIREMENT FOR REPORT:
 * "if we click that quiz, they get their report like their marks and the questions they got correct and wrong.
 * explanation for all both wrong and right should be viewed here, only when clicked."
 */
function openDetailedReport(record) {
  const modal = document.getElementById('quizReportModal');
  modal.classList.remove('hidden');

  // Header & summary
  document.getElementById('reportHeaderMeta').textContent = `${record.subject} • ${record.chapterDisplayName} • ${formatFriendlyDate(record.date)} at ${record.time}`;
  document.getElementById('reportScoreVal').textContent = `${record.score} / ${record.totalQuestions}`;
  document.getElementById('reportAccuracyVal').textContent = `${record.percentage}%`;
  document.getElementById('reportCorrectVal').textContent = record.score;
  document.getElementById('reportWrongVal').textContent = record.totalQuestions - record.score;

  const questionsList = document.getElementById('reportQuestionsList');
  questionsList.innerHTML = '';

  record.answers.forEach((ans, idx) => {
    const card = document.createElement('div');
    card.className = `report-q-card ${ans.isCorrect ? 'is-correct' : 'is-wrong'}`;

    // Find the text of user's chosen option and correct option
    const userOptObj = ans.options ? ans.options.find(o => o.id === ans.selectedOption) : null;
    const correctOptObj = ans.options ? ans.options.find(o => o.id === ans.correctAnswer) : null;

    const userText = userOptObj ? `(${userOptObj.id}) ${formatMathText(userOptObj.text)}` : ans.selectedOption;
    const correctText = correctOptObj ? `(${correctOptObj.id}) ${formatMathText(correctOptObj.text)}` : ans.correctAnswer;

    card.innerHTML = `
      <div class="report-q-top">
        <span class="report-q-badge ${ans.isCorrect ? 'correct' : 'wrong'}">
          ${ans.isCorrect ? '<i class="fa-solid fa-check"></i> Correct (+1)' : '<i class="fa-solid fa-xmark"></i> Incorrect (0)'}
        </span>
        <span class="report-q-chapter">Chapter ${ans.chapterNumber}: ${ans.chapterName}</span>
      </div>
      <div class="report-q-text">Q${idx + 1}. ${formatMathText(ans.question)}</div>
      ${ans.diagram ? `
        <div class="report-q-diagram">
          <img src="${ans.diagram}" alt="Diagram for Question ${idx + 1}">
        </div>
      ` : ''}
      <div class="report-answers-row">
        <div class="ans-box user-choice ${ans.isCorrect ? 'is-correct' : 'is-wrong'}">
          <span class="ans-label">Your Answer:</span>
          <strong>${userText}</strong>
        </div>
        <div class="ans-box correct-choice">
          <span class="ans-label">Correct Answer:</span>
          <strong>${correctText}</strong>
        </div>
      </div>
    `;

    questionsList.appendChild(card);
  });
}

// ===================================================================
// 4. PROFILE SECTION
// ===================================================================
function initProfile() {
  const editProfileForm = document.getElementById('editProfileForm');
  if (editProfileForm) {
    editProfileForm.addEventListener('submit', (e) => {
      e.preventDefault();
      handleSaveProfile();
    });
  }
}

async function handleSaveProfile() {
  if (!STATE.currentUser) return;

  const newName = document.getElementById('editFullName').value.trim();
  const newPassword = document.getElementById('editPassword').value.trim();
  const newPasswordConfirm = document.getElementById('editPasswordConfirm').value.trim();

  if (!newName) {
    showToast('Name cannot be empty.', 'error');
    return;
  }

  if (newPassword) {
    if (newPassword.length < 3) {
      showToast('Password must be at least 3 characters.', 'error');
      return;
    }
    if (newPassword !== newPasswordConfirm) {
      showToast('Passwords do not match.', 'error');
      return;
    }
  }

  // Update backend profile across devices
  try {
    const res = await fetch('/api/auth/profile', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: STATE.currentUser.username,
        newName: newName,
        newPassword: newPassword || undefined
      })
    });
    const data = await res.json();
    if (data.success && data.user) {
      STATE.currentUser.name = data.user.name;
    }
  } catch (err) {
    console.warn('Backend unavailable, updating locally:', err);
    STATE.currentUser.name = newName;
  }

  STATE.currentUser.name = newName;
  localStorage.setItem('class10_currentUser', JSON.stringify(STATE.currentUser));
  updateUserUI();

  // Clear password inputs
  document.getElementById('editPassword').value = '';
  document.getElementById('editPasswordConfirm').value = '';

  showToast('Profile details updated successfully across devices!', 'success');
  refreshAllViews();
}

function renderProfileStats() {
  if (!STATE.currentUser) return;

  const allRecords = getAllUserRecords();
  const totalQuizzes = allRecords.length;

  let totalQuestions = 0;
  let totalScore = 0;

  allRecords.forEach(r => {
    totalQuestions += r.totalQuestions;
    totalScore += r.score;
  });

  const avgAcc = totalQuestions > 0 ? Math.round((totalScore / totalQuestions) * 100) : 0;

  const qEl = document.getElementById('profileTotalQuizzes');
  const qsEl = document.getElementById('profileTotalQuestions');
  const scEl = document.getElementById('profileAvgScore');

  if (qEl) qEl.textContent = totalQuizzes;
  if (qsEl) qsEl.textContent = totalQuestions;
  if (scEl) scEl.textContent = `${avgAcc}%`;
}

// Refresh all views when user changes or quiz finishes
function refreshAllViews() {
  renderDashboardToday();
  renderCalendar();
  renderDayRecords(STATE.selectedCalendarDate);
  renderProfileStats();
}

// ===================================================================
// TOAST NOTIFICATIONS
// ===================================================================
function showToast(message, type = 'info') {
  const container = document.getElementById('toastContainer');
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;

  let icon = 'fa-circle-info';
  if (type === 'success') icon = 'fa-circle-check';
  if (type === 'error') icon = 'fa-triangle-exclamation';

  toast.innerHTML = `<i class="fa-solid ${icon}"></i> <span>${message}</span>`;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
    toast.style.transition = 'all 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}
