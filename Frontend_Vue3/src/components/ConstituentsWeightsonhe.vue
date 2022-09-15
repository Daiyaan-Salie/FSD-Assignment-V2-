<template>
  <div class = "hello">
  <h1>Index Constituents and Weights of {{this.stock}}</h1>
    <!-- call the function -->
    <form @submit.prevent="updateStock">
    <input type="submit" value="Submit" class ="btn-primary">
    <input type ="text" v-model= "stock" name ="stock" placeholder="Select Ticker" >
  
    </form >
       <!-- call the variable -->
    <div class="row" v-if="loaded">
       
    </div>
    
    <div class ='col-md-5'>
      <b-table :items="item" :fields="fields">
      </b-table>
    </div>

    <div class = "col-md-5">
        <div id="TimeSeries"></div>
    </div>

  </div>
    </template>
    
    <script> 
    

import axios from 'axios'
import Plotly from 'plotly.js-dist';


    
    export default {
        name:'ConstituentsWeights',
        props: {
          msg: String
        },
        data(){

          // initialise all variables
            return{
                url: '',
                url2: '',
                allfinancials:[],
                financials: [],
                stock: '',
                loaded: '',
                item:[],
                fields:[],
                close: [],
                x:[],
                opentemp:'',
                xi: '',
                trace1:{}
            }
        },

        // divide number by R1m to make it more readable
        // methods contain the logic 
        
        methods: {

          getChart(stock){
            this.url2 = 'https://financialmodelingprep.com/api/v3/historical-price-full/'+this.stock+'?serietype=line&apikey=fc5921fae23cf964208ebb686edbc5a6' 
            console.log(this.url2)
                axios.get(this.url2)
                .then( res => {
              
              this.close=[]
              this.x=[]  
              this.xi= ''
              this.opentemp = res.data.historical
              for (this.xi of this.opentemp){
               
                this.close.push(this.xi.close)
            
                this.x.push(this.xi.date)
              }
              console.log(this.close)

            })
            .catch(err => console.log(err))
             
            var trace1 = {
  type: "scatter",

  mode: "lines",
  name: 'stock' ,
  x: this.date,
  y: this.close,
  line: {color: '#17BECF'}
}

var data = [trace1];

var layout = {
  title: 'Time Series with Rangeslider',
  xaxis: {
    autorange: true,
    range:  [this.x[0], this.x[10]],
    rangeselector: {buttons: [
        {
          count: 1,
          label: '1d',
          step: 'day',
          stepmode: 'backward'
        },
        {
          count: 6,
          label: '6d',
          step: 'day',
          stepmode: 'backward'
        },
        {step: 'all'}
      ]},
    rangeslider: {range: [this.x[0], this.x[10]]},
    type: 'date'
  },
  yaxis: {
    autorange: true,
    range: [100, 300],
    type: 'linear'
  }
};

Plotly.newPlot('TimeSeries', data, layout);
}

            

  

            },
            formatNumber(number){
                number = (number/1000000).toFixed(2).replace('.',',')
                return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g,".")

            },
            updateStock(){
                this.url = 'https://financialmodelingprep.com/api/v3/income-statement/'+this.stock+'?limit=120&apikey=fc5921fae23cf964208ebb686edbc5a6' 
               
                console.log(this.url)
                axios.get(this.url)
                .then( res => {
                    this.allfinancials = res.data,
                    this.financials = res.data[1];
                    this.loaded = true,
                    // define column labels
                    this.fields=['IS_Item', 'in_MillionsCY','in_MillionsPY']
                    // get variables from dictionary
                    this.item=[
                      { in_MillionsCY: "a",in_MillionsPY : "q", IS_Item: "a"},
                      {in_MillionsCY: this.allfinancials[0].date, in_MillionsPY : this.allfinancials[1].date, IS_Item: Object.keys(this.financials)[0]},
                      {in_MillionsCY: this.formatNumber(this.allfinancials[0].revenue), in_MillionsPY : this.formatNumber(this.allfinancials[1].revenue), IS_Item: Object.keys(this.financials)[8]},
                      {in_MillionsCY: this.formatNumber(this.allfinancials[0].costofRevenue), in_MillionsPY : this.formatNumber(this.allfinancials[1].costofRevenue), IS_Item: Object.keys(this.financials)[9]}
                    //     // each object will be a row and each key must match the column headings
                    // {in_MillionsCY: this.allfinancials[1].date,item:Object.keys(this.financials[1]),
                    //     in_MillionsPY:this.allfinancials[2].date},

                    //     // can only use .revenue when there are no spaces in the data
                    // {in_MillionsCY: this.formatnumber(this.allfinancials[1].revenue),item:Object.keys(this.financials[1]),
                    //     in_MillionsPY:this.formatNumber(this.allfinancials[2].revenue)},
 
                    
                    // {in_MillionsCY: this.formatnumber(this.allfinancials[1]["costofrevenue"]),item:Object.keys(this.financials[1]),
                    //     in_MillionsPY:this.formatNumber(this.allfinancials[2]["costofrevenue"])}

                    ]
                 
                    this.getChart(this.stock)
                })
                .catch (err => console.log(err))
            
            }
        }
    
    
    </script>
    
    <style>
    
    
    </style>