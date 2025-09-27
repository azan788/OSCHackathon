const express = require("express");
const { exec, execFile } = require("child_process");
const path = require("path");
const fs = require("fs");

const app = express();
const PORT = process.env.PORT || 5000;

// Serve the static frontend from "public" folder
app.use(express.static(path.join(__dirname, "public")));

// Run Python greeting script
app.get("/api/greeting", (req, res) => {
  exec(`python3 ${path.join(__dirname, "apps/greeting.py")}`, (err, stdout) => {
    if (err) return res.status(500).json({ error: err.message });
    try {
      res.json(JSON.parse(stdout));
    } catch {
      res.json({ output: stdout.trim() });
    }
  });
});

// Helper: read JSON file
function readJSON(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

// Helper: write JSON file
function writeJSON(filePath, data) {
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2), "utf8");
}

// Find free 15-min intervals where both calendars are free
function findFreeIntervals(events1, events2) {
  const allEvents = [...events1, ...events2].map(e => ({
    start: new Date(e.StartDate),
    end: e.EndDate === "0000/00/00" ? null : new Date(e.EndDate)
  }));

  // Sort events by start time
  allEvents.sort((a, b) => a.start - b.start);

  const freeSlots = [];
  const dayStart = new Date();
  dayStart.setHours(0, 0, 0, 0);
  const dayEnd = new Date(dayStart);
  dayEnd.setHours(23, 59, 59, 999);

  let currentTime = new Date(dayStart);

  while (currentTime < dayEnd) {
    const nextTime = new Date(currentTime.getTime() + 15 * 60000); // 15 min
    const overlap = allEvents.some(
      e => e.end && e.start < nextTime && e.end > currentTime
    );
    if (!overlap) {
      freeSlots.push({
        Start: currentTime.toISOString(),
        End: nextTime.toISOString()
      });
    }
    currentTime = nextTime;
  }

  return freeSlots;
}

// Run C++ calendar program and find free slots
app.get("/api/free-slots", (req, res) => {
  // Example: run Makefile rules to convert .ics -> JSON
  exec("both", (err) => {
    if (err) return res.status(500).json({ error: err.message });

    try {
      const events1 = readJSON(path.join(__dirname, "calendar1.json"));
      const events2 = readJSON(path.join(__dirname, "calendar2.json"));

      const freeSlots = findFreeIntervals(events1, events2);

      writeJSON(path.join(__dirname, "free_slots.json"), freeSlots);

      res.json(freeSlots);
    } catch (error) {
      res.status(500).json({ error: error.message });
    }
  });
});



app.listen(PORT, '0.0.0.0', () => {
  console.log(`🚀 Server running on port ${PORT}`);
});
