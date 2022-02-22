import React from "react";
import "./App.css";

/**
 * ToDoEntry Properties
 * Contains handlers for text and adding button.
 */
interface ToDoEntryProps{
    currentText: string;
    textHandler: (event: React.FormEvent<HTMLInputElement>) => void;
    addToDoHandler: () => void;
}

/**
 * ToDoEntryPanel Component
 * Component contains text handling and button.
 */
class ToDoEntryPanel extends React.Component<ToDoEntryProps>{
    /**
     * Render JSX Content
     */
    render(): JSX.Element{
        return (
			<div>
				<input
					className="pure-u-12-24"
					type="text"
					onChange={this.props.textHandler}
					value={this.props.currentText}
				/>
				<p />
				<button
					className="pure-button pure-button-primary"
					onClick={this.props.addToDoHandler}
				>
					Add new ToDo Item
				</button>
			</div>
		);
    }
}

export default ToDoEntryPanel;