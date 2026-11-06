// Frontend CRUD logic: the browser talks to Django's REST API, never directly to PostgreSQL.
const API_URL = "/api/students/";
const form = document.getElementById("studentForm");
const rows = document.getElementById("studentRows");
const messageBox = document.getElementById("message");
let allStudents = [];

// Read the CSRF token from Django's form cookie so POST/PUT/PATCH/DELETE are protected.
function getCookie(name) {
  const match = document.cookie.match(new RegExp("(^| )" + name + "=([^;]+)"));
  return match ? decodeURIComponent(match[2]) : "";
}

// Central request helper: sends JSON and parses either JSON or empty responses.
async function apiRequest(url, method = "GET", payload = null) {
  const options = { method, headers: { "Accept": "application/json" } };
  if (payload !== null) {
    options.headers["Content-Type"] = "application/json";
    options.headers["X-CSRFToken"] = getCookie("csrftoken");
    options.body = JSON.stringify(payload);
  }
  const response = await fetch(url, options);
  const raw = await response.text();
  let data = null;
  try { data = raw ? JSON.parse(raw) : null; } catch { data = raw; }
  if (!response.ok) {
    const detail = data && typeof data === "object" ? JSON.stringify(data) : `HTTP ${response.status}`;
    throw new Error(detail);
  }
  return { data, status: response.status };
}

// Display success/error feedback without browser alert popups.
function showMessage(text, isError = false) {
  messageBox.textContent = text;
  messageBox.classList.toggle("error", isError);
}

// Escape values before inserting API data into HTML (prevents HTML injection).
function escapeHTML(value) {
  return String(value ?? "").replace(/[&<>"']/g, ch => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[ch]));
}

// Render the current student array into the directory table.
function renderStudents(list) {
  document.getElementById("totalCount").textContent = allStudents.length;
  document.getElementById("recordCount").textContent = `${list.length} record${list.length === 1 ? "" : "s"}`;
  if (!list.length) {
    rows.innerHTML = '<tr><td colspan="4" class="empty">No students found. Add your first student.</td></tr>';
    return;
  }
  rows.innerHTML = list.map(student => `
    <tr>
      <td><strong>${escapeHTML(student.name)}</strong><small>${escapeHTML(student.email)}</small></td>
      <td><span class="course-tag">${escapeHTML(student.course)}</span></td>
      <td>${escapeHTML(student.age)}</td>
      <td class="actions">
        <button class="action-btn" data-action="edit" data-id="${student.id}">Edit</button>
        <button class="action-btn delete" data-action="delete" data-id="${student.id}">Delete</button>
      </td>
    </tr>`).join("");
}

// GET: fetch records from PostgreSQL through the list API endpoint.
async function loadStudents() {
  rows.innerHTML = '<tr><td colspan="4" class="empty">Loading...</td></tr>';
  try {
    const result = await apiRequest(API_URL);
    allStudents = result.data;
    applySearch();
  } catch (error) {
    rows.innerHTML = `<tr><td colspan="4" class="empty">Could not load records: ${escapeHTML(error.message)}</td></tr>`;
    showMessage("Check that PostgreSQL is running and Django migrations are applied.", true);
  }
}

// Client-side search filters the records already retrieved from the API.
function applySearch() {
  const term = document.getElementById("searchInput").value.toLowerCase().trim();
  const filtered = allStudents.filter(s =>
    [s.name, s.course, s.email].some(value => value.toLowerCase().includes(term))
  );
  renderStudents(filtered);
}

// Reset form to create mode after save or cancel.
function resetForm() {
  form.reset();
  document.getElementById("studentId").value = "";
  document.getElementById("formTitle").textContent = "Add a student";
  document.getElementById("submitBtn").textContent = "＋ Add student";
  document.getElementById("cancelBtn").classList.add("hidden");
}

// POST creates a record; PUT updates the selected record.
form.addEventListener("submit", async event => {
  event.preventDefault(); // Prevent full-page form submission; use fetch API instead.
  const id = document.getElementById("studentId").value;
  const payload = {
    name: document.getElementById("name").value.trim(),
    age: Number(document.getElementById("age").value),
    course: document.getElementById("course").value.trim(),
    email: document.getElementById("email").value.trim()
  };
  try {
    if (id) {
      await apiRequest(`${API_URL}${id}/`, "PUT", payload);
      showMessage("Student updated successfully.");
    } else {
      await apiRequest(API_URL, "POST", payload);
      showMessage("Student added successfully.");
    }
    resetForm();
    await loadStudents();
  } catch (error) {
    showMessage(`Save failed: ${error.message}`, true);
  }
});

// Event delegation handles Edit and Delete buttons for all rendered table rows.
rows.addEventListener("click", async event => {
  const button = event.target.closest("button[data-action]");
  if (!button) return;
  const student = allStudents.find(s => String(s.id) === button.dataset.id);
  if (!student) return;

  if (button.dataset.action === "edit") {
    // Populate the form; submitting it will issue a PUT request.
    document.getElementById("studentId").value = student.id;
    document.getElementById("name").value = student.name;
    document.getElementById("age").value = student.age;
    document.getElementById("course").value = student.course;
    document.getElementById("email").value = student.email;
    document.getElementById("formTitle").textContent = `Edit student #${student.id}`;
    document.getElementById("submitBtn").textContent = "Save changes";
    document.getElementById("cancelBtn").classList.remove("hidden");
    window.scrollTo({ top: 0, behavior: "smooth" });
  } else if (button.dataset.action === "delete") {
    // DELETE removes the row from PostgreSQL after user confirmation.
    if (!window.confirm(`Delete ${student.name}? This cannot be undone.`)) return;
    try {
      await apiRequest(`${API_URL}${student.id}/`, "DELETE");
      showMessage("Student deleted successfully.");
      await loadStudents();
    } catch (error) {
      showMessage(`Delete failed: ${error.message}`, true);
    }
  }
});

document.getElementById("cancelBtn").addEventListener("click", resetForm);
document.getElementById("refreshBtn").addEventListener("click", loadStudents);
document.getElementById("searchInput").addEventListener("input", applySearch);

// Load the PostgreSQL-backed student list as soon as the dashboard opens.
loadStudents();
