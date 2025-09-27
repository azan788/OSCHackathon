#ifndef CALENDAR_H
#define CALENDAR_H

#include <string>
#include <vector>
#include <optional>
#include <ctime>

// Event Struct (VEVENT)
struct Event {
    std::string uid;          // Unique ID
    std::string summary;      // Title
    std::string description;  // Details
    std::string location;     // Where
    std::tm dtStart{};        // Start time
    std::tm dtEnd{};          // End time

    Event();
};

// Task Struct (VTODO)
struct Task {
    std::string uid;          // Unique ID
    std::string summary;      // Title
    std::tm due{};            // Due date
    std::string status;       // "NEEDS-ACTION", "COMPLETED", etc.

    Task();
};

// -----------------------------
// Calendar Class
// -----------------------------
class Calendar {
private:
    std::vector<Event> events;
    std::vector<Task> tasks;

public:
    // --- Constructors / Load ---
    Calendar() = default;
    void loadFromICS(const std::string& filename);

    // --- Event Management ---
    void addEvent(const Event& e);
    bool removeEvent(const std::string& uid);
    std::optional<Event> getEventByUID(const std::string& uid) const;
    std::vector<Event> getEventsOnDate(const std::tm& date) const;

    // --- Task Management ---
    void addTask(const Task& t);
    bool removeTask(const std::string& uid);
    std::vector<Task> getTasksOnDate(const std::tm& date) const;
    std::vector<Task> getUncompletedTasks() const;
    void markTaskComplete(const std::string& uid);
    void markTaskIncomplete(const std::string& uid);
};

#endif // CALENDAR_H
