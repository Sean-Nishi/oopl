/*
Sean Nishi
Homework 6
12/11/2021
*/

import React from 'react';
import {VictoryLine, VictoryChart, VictoryTheme} from 'victory';

//StockChart takes Tesla stock data as a prop and render
//a Victory Line Chart

//Properties
interface ChartProps{
    data: number[]
}

//StockChart extends the ChartProps
class StockChart extends React.Component<ChartProps>{
    //Render and return a JSX.Element
    render(): JSX.Element{
        return (
            <div className='victory_chart'>
                <VictoryChart theme={VictoryTheme.material }>
                    <VictoryLine data={this.props.data} />
                </VictoryChart>   
          </div>          
        );
    }
}

export default StockChart;