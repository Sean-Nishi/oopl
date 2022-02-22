import React from "react";
import ToDoTable from "./ToDoTable"
import ToDoData from "./ToDoData"
import ToDoEntry from "./ToDoEntry"
import ToDoEntryPanel from "./ToDoEntryPanel"

/**
 * Class for the ToDoPanel.
 * State contains currentText and a list of things To Do.
 * Has handlers for text, adding entry, toggling status of entry, and deleting entry
 */
class ToDoPanel extends React.Component<{}, ToDoData>{

    /**
     * Initialize Log State.
     */
    constructor(props: {}){
        super(props);
        this.state = {
            currentText: "",
            todoList: []
        };

        //Binding event handlers
        this.textHandler = this.textHandler.bind(this);
        this.addToDoHandler = this.addToDoHandler.bind(this);
        this.toggleStatus = this.toggleStatus.bind(this);
        this.deleteToDoEntryHandler = this.deleteToDoEntryHandler.bind(this);
    }

    /**
     * Render JSX Content
     * @returns JSX Element
     */
    render(): JSX.Element{
        return (
			<div>
				<h1 className="post-title">Super ToDo!</h1>
				<div>
					<ToDoEntryPanel 
						currentText={this.state.currentText}
						textHandler={this.textHandler}
						addToDoHandler={this.addToDoHandler}/>
				</div>
				<p/>
				<div className="pure-u-1-2">
					<ToDoTable 
						todoList={this.state.todoList}
                        toggleStatusEntryHandler={this.toggleStatus}
						deleteToDoEntryHandler = {this.deleteToDoEntryHandler} />
				</div>
			</div>
		);
    }

    /**
     * Triggers when user enters text into the Text Box.
     */
    textHandler(event: React.FormEvent<HTMLInputElement>){
        let newTextValue = event.currentTarget.value;
		console.log("Got Text Change:  " + newTextValue);
		let todoList = this.state.todoList;
		this.setState({
			currentText: newTextValue,
			todoList: todoList,
		});
    }

    /**
     * Triggers when user clicks the Add Button
     */
    addToDoHandler(){
        let todoList = this.state.todoList;
		if (this.state.currentText) {
			console.log("Adding new ToDo item:  " + this.state.currentText);
			let currentTime = new Date();
			let newEntry: ToDoEntry = {
                status: "Pending",
				timeStamp: currentTime,
				textEntry: this.state.currentText,
			};
			todoList.push(newEntry);
			this.setState({
				currentText: "",
				todoList: todoList,
			});
		}
    }

    /**
     * Triggers when user clicks the Toggle Status Button
     */
    toggleStatus(index: number){
        console.log("Toggling status")
        //get the current ToDo list as is
        let todoList = this.state.todoList;
        //instead of splicing/removing like for the delete button,
        //copy state, change data, then reset the state
        if (todoList[index].status.toString() === "Pending"){
            todoList[index].status = "Done";
        }
        else {
            todoList[index].status = "Pending";
        }

        this.setState({
            currentText: this.state.currentText,
            todoList: todoList
        })
    }

    /**
     * Triggers when user wants to delete an item
     */
    deleteToDoEntryHandler(index: number){
        console.log("Deleting ToDo item: " + index);
        let todoList = this.state.todoList;

        //Note that there is no remove method in JavaScript; we use splice instead.
        todoList.splice(index, 1);
        this.setState({
            currentText: this.state.currentText,
            todoList: todoList
        });
    }

}

export default ToDoPanel;