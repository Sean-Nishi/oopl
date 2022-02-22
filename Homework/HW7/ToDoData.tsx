import ToDoEntry from './ToDoEntry'

/**
 * ToDo Data Interface
 * Contains text and a list of entries.
 */
interface ToDoData{
    currentText: string;
    todoList: ToDoEntry[];
}

export default ToDoData;