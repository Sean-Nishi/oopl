/**
 * Sean Nishi
 * Homework 6
 * 12/11/2021
 */

//Take Tesla stock data as a prop and render a Pure-CSS
//table of data

import React from "react";

interface TableProps{
    data: number[]
};

class StockTable extends React.Component<TableProps>{
    render(): JSX.Element{
        let stockTable = this.getStockTable(this.props.data);
        return (
            //get Pure CSS table and then display data
            //like with Car table example in class
            <div>
                {stockTable}
            </div>
        )
    }

    //Iterate through elements is JSX
    private getStockTable(stockPrices: number[]): JSX.Element{
        var tableData = stockPrices.map(this.getStockRow);
        return (
            <table className="pure-table-horizontal">
                <thead>
                    <tr>
                        <th>Stock Close</th>
                    </tr>
                </thead>
                <tbody>
                    {tableData}
                </tbody>
            </table>
        );
    }

    //get single row of data
    private getStockRow(stockPrice: number){
        return (
            <tr>
                <td>{stockPrice}</td>
            </tr>
        );
    }
}

export default StockTable;