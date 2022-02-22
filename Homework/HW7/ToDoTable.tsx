import React from "react";
import ToDoEntry from "./ToDoEntry"

/**
 * ToDo Table Properties
 * List of To Do items.
 * Handler for toggling status of an entry.
 * Handler for deleting and entry.
 */
interface ToDoTableProps{
    todoList: ToDoEntry[];
    toggleStatusEntryHandler: (index: number) => void;
    deleteToDoEntryHandler: (index: number) => void;
}

/**
 * ToDoTable Component
 * Contains handler for putting an entry on the screen.
 */
class ToDoTable extends React.Component<ToDoTableProps>{
    /**
     * Initializer
     */
    constructor(todoTableProps: ToDoTableProps){
        super(todoTableProps);

        this.getToDoRow = this.getToDoRow.bind(this);
    }

    /**
     * Render the Component. Maps entry data to a table.
     * @returns JSX Element
     */
    render(): JSX.Element{
        let todoRows = this.props.todoList.map(this.getToDoRow);
		return (
			<table className="pure-table">
				<thead>
					<tr>
                        <th>Status</th>
						<th>Timestamp</th>
						<th>Entry</th>
						<th>Action</th>
                        <th>Action</th>
					</tr>
				</thead>
				<tbody>{todoRows}</tbody>
			</table>
		);
    }

    
    /**
     * 
     * @param todoItem Input Item Entry Data
     * @param index Index of todoItem
     * @returns JSX Element
     */
    getToDoRow(todoItem: ToDoEntry, index: number){
        return (
			<tr key={todoItem.timeStamp.getSeconds()}>
                <td>{todoItem.status}</td>
				<td>
					{todoItem.timeStamp.toLocaleDateString()}{" "}
					{todoItem.timeStamp.toLocaleTimeString()}
				</td>
				<td>{todoItem.textEntry}</td>
                <td>
                    <button
                        className="pure-button"
                        onClick={this.props.toggleStatusEntryHandler.bind(this, index)}
                    >
                        Toggle Status
                    </button>
                </td>
				<td>
					<button
						className="pure-button"
						onClick={this.props.deleteToDoEntryHandler.bind(this, index)}
					>
						Delete
					</button>
				</td>
			</tr>
		);
    }

}

export default ToDoTable;