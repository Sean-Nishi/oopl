//Sean Nishi
//Homework 5: Homework 3 but in typescript.
//11/18/2021

enum NewsCategory {
	BUSINESS,
	POLITICS,
	TECH,
	ENTERTAINMENT,
	SPORTS
}

abstract class Publisher {
	//Base class that publishes updates to all subscribers to pick up

	//attach method
	abstract attach(subscriber: Subscriber): void;
	//Attach a Subscriber to the Publisher

	//detach method
	abstract detach(subscriber: Subscriber): void;
	//Detach a Subscriber from the Publisher

	abstract notify(newsCategory: NewsCategory, newsTitle: string): void;
	//Notify all Subscribers about an event

}//Publisher

class NewYorkTimesBreakingNews extends Publisher {
	//Derived from Publisher. Will update Subscribers with NYTimes news
	_subscribers: Subscriber[]

	constructor() {
		//Constructor for class. Extends Publisher
		super();
		this._subscribers = new Array();
	}

	attach(subscriber: Subscriber): void {
		//Implementation of attach method from Publisher. Pushes new subscriber into array
		this._subscribers.push(subscriber);
	}

	detach(subscriber: Subscriber): void {
		//Implementation of detach method from Pubisher. Uses filter() to create new array without Subscriber
		this._subscribers = this._subscribers.filter(item => item !== subscriber);
	}

	notify(newsCategory: NewsCategory, newsTitle: string): void{
		//Implementation of notify. Sends Subscribers news
		this._subscribers.forEach(function (sub){
			sub.breakingNews(newsCategory, newsTitle);
		});
	}

	publishNewsItem(newsCategory: NewsCategory, newsTitle: string) : void {
		//Publishes a new news item
		this.notify(newsCategory, newsTitle);
	}
}//NewYorkTimesBreakingNews

interface Subscriber {
	//Base Subscriber interface
	breakingNews(newsCategory: NewsCategory, newsTitle: string): void;
	//Notifies the Subscriber of new news

}//Subscriber

class BusinessNewsSubscriber implements Subscriber{
	//Subscriber for Business news only

	breakingNews(newsCategory: NewsCategory, newsTitle: string): void {
		//Prints the news if it is business news
		if (newsCategory === NewsCategory.BUSINESS){
			console.log("Subscriber: Business Breaking: " + newsTitle);
		}
	}
}//BusinessNewsSubscriber

class PoliticsNewsSubscriber implements Subscriber{
	//Subscriber for Business news only

	breakingNews(newsCategory: NewsCategory, newsTitle: string): void {
		//prints the news if it is politics news
		if (newsCategory === NewsCategory.POLITICS){
			console.log("Subscriber: Politics Breaking: " + newsTitle);
		}
	}
}//PoliticsNewsSubscriber

class KeyWordSubscriber implements Subscriber{
	//Subscriber that filters news by a keyword
	_keyword: string

	constructor(keyword: string){
		//sets the keyword upon instantiation
		this._keyword = keyword;
	}

	breakingNews(newsCategory: NewsCategory, newsTitle: string): void {
		//prints the news if it contains keyword
		if (newsTitle.toLowerCase().includes(this._keyword.toLowerCase())){
			console.log("Subscriber: Keyword Breaking: " + newsTitle)
		}
	}
}//KeyWordSubscriber

/******************************************************************************/
//client code
let NYT = new NewYorkTimesBreakingNews();

let sub_a = new BusinessNewsSubscriber();
NYT.attach(sub_a);

let sub_b = new PoliticsNewsSubscriber();
NYT.attach(sub_b);

let sub_c = new KeyWordSubscriber("Biden");
NYT.attach(sub_c);

NYT.publishNewsItem(NewsCategory.BUSINESS, "J&J plans to split into two companies.");
NYT.publishNewsItem(NewsCategory.POLITICS, "Biden and Xi to Hold Virtual Summit.")

