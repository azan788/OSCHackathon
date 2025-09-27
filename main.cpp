#include <iostream>

//Implement Calender class that can
//Read a .isc file
//Add individual events
//export a .isc file
//store location data of events
//Given a time/date check if there is an event
//store notes on the events
//Return a list of events for the a certain time period/day with times
//So like [name, location, notes, time1, time2]

//Implement an eventTask class that takes location, up to two times, name, notes
//events have a given time
//tasks don't have a given time just a date

//Implement a Tasklist class
//Return list of events + tasks uncompleted
//Complete eventTask function
//Add eventTask function
//Edit eventTask function

//Calendar class stores just events

//add event
//add task
//remove event
//remove task
//edit task/event
//get task/event list for day


int main() {
    // TIP Press <shortcut actionId="RenameElement"/> when your caret is at the <b>lang</b> variable name to see how CLion can help you rename it.
    auto lang = "C++";
    std::cout << "Hello and welcome to " << lang << "!\n";

    for (int i = 1; i <= 5; i++) {
        // TIP Press <shortcut actionId="Debug"/> to start debugging your code. We have set one <icon src="AllIcons.Debugger.Db_set_breakpoint"/> breakpoint for you, but you can always add more by pressing <shortcut actionId="ToggleLineBreakpoint"/>.
        std::cout << "i = " << i << std::endl;
    }

    return 0;
    // TIP See CLion help at <a href="https://www.jetbrains.com/help/clion/">jetbrains.com/help/clion/</a>. Also, you can try interactive lessons for CLion by selecting 'Help | Learn IDE Features' from the main menu.
}