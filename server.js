const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
const crypto = require('crypto');

const app = express();
const PORT = process.env.PORT || 3000;

// Enable CORS and JSON parsing
app.use(cors());
app.use(express.json({ limit: '10mb' }));

// Ensure database directory exists
const DB_DIR = path.join(__dirname, 'data', 'db');
const USERS_FILE = path.join(DB_DIR, 'users.json');
const RECORDS_FILE = path.join(DB_DIR, 'records.json');

if (!fs.existsSync(DB_DIR)) {
  fs.mkdirSync(DB_DIR, { recursive: true });
}

// Helpers for reading/writing persistent store
function readData(file, defaultVal = []) {
  try {
    if (!fs.existsSync(file)) {
      fs.writeFileSync(file, JSON.stringify(defaultVal, null, 2), 'utf-8');
      return defaultVal;
    }
    const content = fs.readFileSync(file, 'utf-8');
    return JSON.parse(content || '[]');
  } catch (err) {
    console.error(`Error reading ${file}:`, err);
    return defaultVal;
  }
}

function writeData(file, data) {
  try {
    fs.writeFileSync(file, JSON.stringify(data, null, 2), 'utf-8');
  } catch (err) {
    console.error(`Error writing to ${file}:`, err);
  }
}

// Hash password with salt using built-in crypto
function hashPassword(password, salt = 'class10_maths_secure_salt') {
  return crypto.pbkdf2Sync(password, salt, 10000, 64, 'sha512').toString('hex');
}

// ===================================================================
// API ROUTES
// ===================================================================

// Health Check
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', serverTime: new Date().toISOString() });
});

// 1. SIGN UP (Works across all devices)
app.post('/api/auth/signup', (req, res) => {
  const { username, password, name } = req.body;

  if (!username || !password || !name) {
    return res.status(400).json({ success: false, message: 'All fields (Name, Username, Password) are required.' });
  }

  const cleanUser = username.trim().toLowerCase();
  const cleanName = name.trim();

  if (cleanUser.length < 3) {
    return res.status(400).json({ success: false, message: 'Username must be at least 3 characters long.' });
  }
  if (password.length < 3) {
    return res.status(400).json({ success: false, message: 'Password must be at least 3 characters long.' });
  }

  const users = readData(USERS_FILE, []);

  // Check if username already exists
  const existing = users.find(u => u.username.toLowerCase() === cleanUser);
  if (existing) {
    return res.status(409).json({ success: false, message: 'This username is already taken. Please choose another.' });
  }

  const newUser = {
    id: 'user_' + Date.now() + '_' + Math.random().toString(36).substring(2, 7),
    username: cleanUser,
    name: cleanName,
    passwordHash: hashPassword(password),
    createdAt: new Date().toISOString()
  };

  users.push(newUser);
  writeData(USERS_FILE, users);

  res.status(201).json({
    success: true,
    message: 'Account created successfully!',
    user: {
      username: newUser.username,
      name: newUser.name
    }
  });
});

// 2. SIGN IN (Access same account from any device)
app.post('/api/auth/signin', (req, res) => {
  const { username, password } = req.body;

  if (!username || !password) {
    return res.status(400).json({ success: false, message: 'Please enter both username and password.' });
  }

  const cleanUser = username.trim().toLowerCase();
  const users = readData(USERS_FILE, []);

  const user = users.find(u => u.username.toLowerCase() === cleanUser);
  if (!user) {
    return res.status(401).json({ success: false, message: 'Username not found. Please sign up first.' });
  }

  const inputHash = hashPassword(password);
  if (user.passwordHash !== inputHash) {
    return res.status(401).json({ success: false, message: 'Incorrect password. Please try again.' });
  }

  // Load user records
  const allRecords = readData(RECORDS_FILE, []);
  const userRecords = allRecords.filter(r => r.username.toLowerCase() === cleanUser);

  res.json({
    success: true,
    message: 'Welcome back!',
    user: {
      username: user.username,
      name: user.name
    },
    records: userRecords
  });
});

// 3. UPDATE PROFILE
app.post('/api/auth/profile', (req, res) => {
  const { username, newName, newPassword } = req.body;

  if (!username) {
    return res.status(400).json({ success: false, message: 'Username is required.' });
  }

  const cleanUser = username.trim().toLowerCase();
  const users = readData(USERS_FILE, []);
  const userIndex = users.findIndex(u => u.username.toLowerCase() === cleanUser);

  if (userIndex === -1) {
    return res.status(404).json({ success: false, message: 'User not found.' });
  }

  if (newName && newName.trim()) {
    users[userIndex].name = newName.trim();
  }

  if (newPassword && newPassword.trim()) {
    if (newPassword.trim().length < 3) {
      return res.status(400).json({ success: false, message: 'Password must be at least 3 characters.' });
    }
    users[userIndex].passwordHash = hashPassword(newPassword.trim());
  }

  writeData(USERS_FILE, users);

  res.json({
    success: true,
    message: 'Profile updated successfully!',
    user: {
      username: users[userIndex].username,
      name: users[userIndex].name
    }
  });
});

// 4. GET USER QUIZ RECORDS
app.get('/api/records', (req, res) => {
  const username = req.query.username;
  if (!username) {
    return res.status(400).json({ success: false, message: 'Username query parameter is required.' });
  }

  const cleanUser = username.trim().toLowerCase();
  const allRecords = readData(RECORDS_FILE, []);
  const userRecords = allRecords.filter(r => r.username && r.username.toLowerCase() === cleanUser);

  res.json({
    success: true,
    records: userRecords
  });
});

// 5. SAVE QUIZ RECORD
app.post('/api/records', (req, res) => {
  const { username, record } = req.body;

  if (!username || !record) {
    return res.status(400).json({ success: false, message: 'Username and record are required.' });
  }

  const cleanUser = username.trim().toLowerCase();
  const allRecords = readData(RECORDS_FILE, []);

  const newRecord = {
    ...record,
    username: cleanUser,
    savedAt: new Date().toISOString()
  };

  // Prepend newest first
  allRecords.unshift(newRecord);
  writeData(RECORDS_FILE, allRecords);

  res.status(201).json({
    success: true,
    message: 'Record saved successfully!',
    record: newRecord
  });
});

// Serve static frontend files
app.use(express.static(__dirname));

// Single Page Application fallback to index.html (Express 5 compatible)
app.use((req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Start Server
app.listen(PORT, () => {
  console.log(`===============================================`);
  console.log(`Class 10 MCQ Practice Server running on port ${PORT}`);
  console.log(`Ready for multi-device login & Render deployment`);
  console.log(`===============================================`);
});
