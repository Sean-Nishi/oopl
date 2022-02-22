/**
 * ToDo Entry Interface
 * Added a status to the Entry
 */
interface ToDoEntry{
    status: string;//added to base interface
    timeStamp: Date;
    textEntry: string;
}

export default ToDoEntry;